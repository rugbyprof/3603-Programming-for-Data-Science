from pathlib import Path

for module in sorted(p for p in Path("03-Completed").iterdir() if p.is_dir()):
    original = Path("02-Assignments") / module.name
    if not original.is_dir():
        print(
            f"❌ {module.name}: no folder with this name in 02-Assignments (check the spelling)"
        )
        continue
    required = sorted(
        p.name
        for p in original.iterdir()
        if p.suffix == ".ipynb" or p.name in ("quiz.md", "worksheet.md")
    )
    missing = [name for name in required if not (module / name).exists()]
    extra = sorted(
        p.name
        for p in module.iterdir()
        if p.suffix == ".ipynb" and not (original / p.name).exists()
    )
    if missing or extra:
        print(f"❌ {module.name}")
        for name in missing:
            print(f"     missing:          {name}")
        for name in extra:
            print(f"     unexpected name:  {name}")
    else:
        print(f"✅ {module.name}: all {len(required)} required files present")
