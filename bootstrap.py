from pathlib import Path
from zipfile import ZipFile
import shutil

ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / "app_bundle.zip"
APP = ROOT / "app"

if not BUNDLE.is_file():
    raise SystemExit("app_bundle.zip not found")

if APP.exists():
    shutil.rmtree(APP)
APP.mkdir(parents=True, exist_ok=True)

with ZipFile(BUNDLE) as zf:
    for member in zf.infolist():
        target = (APP / member.filename).resolve()
        if APP.resolve() not in target.parents and target != APP.resolve():
            raise SystemExit(f"Unsafe zip entry: {member.filename}")
    zf.extractall(APP)

print(f"Extracted {BUNDLE.name} -> {APP}")
