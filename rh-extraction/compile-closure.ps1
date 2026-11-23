# compile-closure.ps1
# Builds from source only the 705 modules that our two lemma files need, then has Lean check both files.
# No AI credits needed. It can take from under an hour to a few hours. Leave the window open.
#
# Run it either way:
#   - Right-click this file > "Run with PowerShell", or
#   - powershell -ExecutionPolicy Bypass -File "C:\Users\timmy\OneDrive\Desktop\XPostCode\rh-extraction\compile-closure.ps1"
#
# Everything is written to compile-log.txt next to this script. When it ends, tell Claude "done".
# Uses C:\rhc only, never D:. Stops if free space on C: falls below 25 GB.

$ErrorActionPreference = 'Continue'
$Here      = $PSScriptRoot
$Root      = 'C:\rhc'
$Repo      = 'https://github.com/homeowmorphism/riemann-hypothesis-original'
$Commit    = '4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e'
$Tree      = '24df20b62d9976ccd20da819bc20b16f808f0fdd'
$Target    = 'Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen'
$Expected  = 705
$MinFreeGB = 25
$Log       = Join-Path $Here 'compile-log.txt'
$Utf8      = New-Object System.Text.UTF8Encoding($false)

function Say([string]$msg) {
  $line = '[{0}] {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $msg
  Write-Host $line
  Add-Content -Path $Log -Value $line -Encoding UTF8
}
function FreeGB { [math]::Round((Get-PSDrive C).Free / 1GB, 1) }
function Stop-Run([string]$msg) {
  Say "STOPPED: $msg"
  Copy-Item "$Root\*.log", "$Root\*.out" $Here -Force -ErrorAction SilentlyContinue
  Say 'Tell Claude "stopped". The details are in compile-log.txt.'
  Read-Host 'Press Enter to close'
  exit 1
}
function Check-Disk { $f = FreeGB; if ($f -lt $MinFreeGB) { Stop-Run "C: has only $f GB free (the limit is $MinFreeGB GB)." } }
# Runs a command through cmd.exe with all output sent to a log file in C:\rhc (a path with no spaces).
function Run-Logged([string]$label, [string]$cmdline, [string]$outfile) {
  Say "$label ..."
  $t0 = Get-Date
  cmd /c "$cmdline > $outfile 2>&1"
  $code = $LASTEXITCODE
  $mins = [math]::Round(((Get-Date) - $t0).TotalMinutes, 1)
  Say "$label finished: exit code $code, $mins min, C: free $(FreeGB) GB"
  return $code
}
function Verdict([string]$name, [int]$code, [string]$file) {
  $out = ''
  if (Test-Path $file) { $out = [IO.File]::ReadAllText($file, $Utf8) }
  Add-Content -Path $Log -Value ("----- output of $name -----`r`n" + $out + "`r`n----- end -----") -Encoding UTF8
  $ok = ($code -eq 0) -and ($out -notmatch 'error:') -and ($out -notmatch 'sorryAx')
  $allowed = @('propext', 'Classical.choice', 'Quot.sound')
  foreach ($m in [regex]::Matches($out, 'depends on axioms: \[([^\]]*)\]')) {
    foreach ($ax in ($m.Groups[1].Value -split ',')) {
      if ($allowed -notcontains $ax.Trim()) { $ok = $false; Say "Unexpected axiom in ${name}: $($ax.Trim())" }
    }
  }
  if ($ok) { Say "PASS: $name" } else { Say "FAIL: $name" }
  return $ok
}

# ---------------------------------------------------------------- 0. start
Set-Content -Path $Log -Value ('compile-closure.ps1 log, started ' + (Get-Date -Format 's')) -Encoding UTF8
$ramGB = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 1)
Say "Machine: cores $([Environment]::ProcessorCount), RAM $ramGB GB, C: free $(FreeGB) GB"
Check-Disk

foreach ($f in @('CommonPeriodMap.lean', 'CommonPeriodMap2.lean', 'closure-files.txt')) {
  $p = Join-Path $Here $f
  if (-not (Test-Path $p)) { Stop-Run "Missing $f next to this script." }
  Say ('sha256 {0}: {1}' -f $f, (Get-FileHash $p -Algorithm SHA256).Hash.ToLower())
}

# ---------------------------------------------------------------- 1. tools
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { Stop-Run 'git is not installed. Get it from https://git-scm.com/download/win and run this again.' }
Say ('git: ' + (git --version))
$ElanBin = Join-Path $env:USERPROFILE '.elan\bin'
if (Test-Path $ElanBin) { $env:Path = "$ElanBin;$env:Path" }
if (-not (Get-Command elan -ErrorAction SilentlyContinue)) {
  Say 'Installing elan, the Lean version manager ...'
  $zip = Join-Path $env:TEMP 'elan.zip'
  $dir = Join-Path $env:TEMP 'elan-init'
  [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
  Invoke-WebRequest -UseBasicParsing -Uri 'https://github.com/leanprover/elan/releases/latest/download/elan-x86_64-pc-windows-msvc.zip' -OutFile $zip
  Expand-Archive -Force -Path $zip -DestinationPath $dir
  & (Join-Path $dir 'elan-init.exe') -y --default-toolchain none
  $env:Path = "$ElanBin;$env:Path"
  if (-not (Get-Command elan -ErrorAction SilentlyContinue)) { Stop-Run 'Installing elan failed.' }
}
Say ('elan: ' + (elan --version))

# ---------------------------------------------------------------- 2. sparse checkout of the pinned commit
if (-not (Test-Path (Join-Path $Root '.git'))) {
  Say 'Cloning the repository (commits and folder lists only, no file contents yet) ...'
  git -c core.longpaths=true clone --filter=blob:none --no-checkout $Repo $Root
  if ($LASTEXITCODE -ne 0) { Stop-Run 'git clone failed.' }
} else {
  Say "$Root already exists; reusing it."
}
Set-Location $Root
git config core.longpaths true
git config core.autocrlf false
git config core.sparseCheckout true
git config core.sparseCheckoutCone false
git cat-file -e "$Commit^{commit}" 2>$null
if ($LASTEXITCODE -ne 0) { git fetch --filter=blob:none origin $Commit; if ($LASTEXITCODE -ne 0) { Stop-Run "Could not fetch commit $Commit." } }

$patterns = @('/lakefile.toml', '/lake-manifest.json', '/lean-toolchain', '/scripts/')
$patterns += [IO.File]::ReadAllLines((Join-Path $Here 'closure-files.txt'), $Utf8) | Where-Object { $_.Trim() -ne '' } | ForEach-Object { '/' + $_.Trim() }
New-Item -ItemType Directory -Force -Path (Join-Path $Root '.git\info') | Out-Null
[IO.File]::WriteAllLines((Join-Path $Root '.git\info\sparse-checkout'), [string[]]$patterns, $Utf8)
Say "Wrote $($patterns.Count) sparse-checkout patterns."

Say 'Checking out the pinned commit (only the files we need) ...'
git read-tree -mu $Commit
if ($LASTEXITCODE -ne 0) { Stop-Run 'Checkout of the pinned commit failed.' }
git update-ref --no-deref HEAD $Commit
$head = (git rev-parse HEAD).Trim()
$tree = (git rev-parse 'HEAD:src').Trim()
Say "HEAD $head, src tree $tree"
if ($head -ne $Commit) { Stop-Run "HEAD is $head, expected $Commit." }
if ($tree -ne $Tree)   { Stop-Run "src tree is $tree, expected $Tree." }
$n = @(Get-ChildItem -Path (Join-Path $Root 'src') -Recurse -Filter '*.lean' -File).Count
Say "Source files present: $n (expected $Expected)"
if ($n -ne $Expected) { Stop-Run "Expected $Expected source files, found $n." }
Say ('lean-toolchain: ' + ([IO.File]::ReadAllText((Join-Path $Root 'lean-toolchain'))).Trim())
Check-Disk

# ---------------------------------------------------------------- 3. Lean and Mathlib
$env:LEAN_ABORT_ON_PANIC   = '1'
$env:LAKE_ARTIFACT_CACHE   = 'false'
$env:MATHLIB_CACHE_GET_URL = 'https://cache.mathlib.org/mathlib4'
$code = Run-Logged 'Lean toolchain check (downloads Lean 4.33.1 the first time)' 'lake --version' "$Root\lake-version.log"
Say ('lake: ' + ([IO.File]::ReadAllText("$Root\lake-version.log")).Trim())
if ($code -ne 0) { Stop-Run 'lake did not start.' }
$code = Run-Logged "Mathlib download (Mathlib's own cache; never the project cache)" 'lake exe mathlib/cache get' "$Root\mathlib-cache.log"
if ($code -ne 0) { Stop-Run 'The Mathlib download failed (see mathlib-cache.log).' }
Check-Disk

# ---------------------------------------------------------------- 4. build the 705 modules from source
$code = Run-Logged "Build of the $Expected modules from source" "lake build $Target" "$Root\build-closure.log"
Add-Content -Path $Log -Value ("----- last 40 lines of build-closure.log -----`r`n" + ((Get-Content "$Root\build-closure.log" -Tail 40) -join "`r`n") + "`r`n----- end -----") -Encoding UTF8
if ($code -ne 0) { Stop-Run 'The build failed (see build-closure.log).' }
Check-Disk

# ---------------------------------------------------------------- 5. Lean checks our two files
Copy-Item (Join-Path $Here 'CommonPeriodMap.lean')  $Root -Force
Copy-Item (Join-Path $Here 'CommonPeriodMap2.lean') $Root -Force
$c1 = Run-Logged 'Lean check of CommonPeriodMap.lean'  'lake env lean CommonPeriodMap.lean'  "$Root\common-period-map.out"
$c2 = Run-Logged 'Lean check of CommonPeriodMap2.lean' 'lake env lean CommonPeriodMap2.lean' "$Root\common-period-map2.out"
$ok1 = Verdict 'CommonPeriodMap.lean'  $c1 "$Root\common-period-map.out"
$ok2 = Verdict 'CommonPeriodMap2.lean' $c2 "$Root\common-period-map2.out"

Copy-Item "$Root\*.log", "$Root\*.out" $Here -Force -ErrorAction SilentlyContinue
$size = [math]::Round(((Get-ChildItem $Root -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum) / 1GB, 1)
Say "C:\rhc uses $size GB. It is kept so that later checks are fast."
if ($ok1 -and $ok2) { Say 'ALL PASSED. Tell Claude "done".' } else { Say 'Something failed. Tell Claude "done"; the details are in compile-log.txt.' }
Read-Host 'Press Enter to close'
