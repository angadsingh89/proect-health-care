"""Root launcher for Streamlit Cloud.

This keeps deployment working even if the main file path is set to `app.py`.
It forwards execution to `pa_copilot/app.py`.
"""

import os
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_DIR = ROOT / "pa_copilot"
TARGET = APP_DIR / "app.py"

if not TARGET.exists():
    raise FileNotFoundError(f"Could not find app entrypoint at: {TARGET}")

# Ensure sibling imports like `from agents import ...` keep working.
sys.path.insert(0, str(APP_DIR))
os.chdir(APP_DIR)
runpy.run_path(str(TARGET), run_name="__main__")

