#!/usr/bin/env python3
"""25c entry point: the combined single-pass scanner lives in ../export-names/scan_export.py."""
import os, runpy, sys
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "export-names", "scan_export.py")
sys.argv[0] = p
runpy.run_path(p, run_name="__main__")
