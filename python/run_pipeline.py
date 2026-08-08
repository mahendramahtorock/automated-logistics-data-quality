"""
End-to-end local QA pipeline.
Run: python python/run_pipeline.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

steps = [
    ["python", str(ROOT/"python/data_cleaning.py")],
    ["python", str(ROOT/"python/data_quality_checks.py")],
    ["python", str(ROOT/"python/anomaly_detection.py")],
]

for step in steps:
    print("\n>>>", " ".join(step))
    result = subprocess.run(step, cwd=ROOT)
    if result.returncode != 0:
        sys.exit(result.returncode)

print("\nPipeline completed successfully.")
