"""Check that 03-Completed mirrors 02-Assignments, file by file.

Usage (from anywhere inside the repository):
    python check_completed.py                     # check every module in 03-Completed
    python check_completed.py 05-Foundations      # check just one module
    python check_completed.py 03 03b              # check several (a unique prefix is enough)

Every required file gets a ✅ or ❌. The exit code is 0 when everything passes, 1 otherwise.

Names are matched WITHOUT regard to capitalization (01-lists.ipynb counts as 01-Lists.ipynb),
because Mac and Windows, and git on them, often can't tell the difference. A grading script
should match the same way: `from check_completed import find`, then open the path it returns.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSIGNMENTS = ROOT / '02-Assignments'
COMPLETED = ROOT / '03-Completed'
REQUIRED_DOCS = ('quiz.md', 'worksheet.md')
OUTPUT_FOLDER = re.compile(r'''['"]([\w-]+-OutputFiles)['"]''')

PASS, FAIL = '✅', '❌'


def find_all(folder, name):
    """Every entry in `folder` whose name matches `name`, ignoring capitalization."""
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir() if p.name.lower() == name.lower())


def find(folder, name):
    """The entry in `folder` matching `name` (ignoring capitalization), or None.

    Prefers an exact match. Returns None if nothing matches, or if several entries
    differ only by capitalization and none matches exactly (it's ambiguous which one).
    """
    matches = find_all(folder, name)
    exact = [p for p in matches if p.name == name]
    if exact:
        return exact[0]
    return matches[0] if len(matches) == 1 else None


# ---------------------------------------------------------------- output

# Emoji crash older Windows consoles that aren't using UTF-8
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except (AttributeError, ValueError):
    pass

USE_COLOR = sys.stdout.isatty() and 'NO_COLOR' not in os.environ
if USE_COLOR and os.name == 'nt':
    os.system('')  # turns on ANSI color codes in the Windows console


def color(text, code):
    return f'\033[{code}m{text}\033[0m' if USE_COLOR else text


def green(text):
    return color(text, '32')


def red(text):
    return color(text, '31')


def bold(text):
    return color(text, '1')


# ---------------------------------------------------------------- checks

def module_names():
    """The official module folder names, from 02-Assignments."""
    return sorted(p.name for p in ASSIGNMENTS.iterdir() if p.is_dir())


def required_items(original):
    """The notebooks, docs, and output folders a module must contain."""
    notebooks = sorted(p.name for p in original.glob('*.ipynb'))
    docs = [name for name in REQUIRED_DOCS if (original / name).exists()]
    folders = set()
    for name in notebooks:
        folders.update(OUTPUT_FOLDER.findall((original / name).read_text(encoding='utf-8')))
    return notebooks, docs, sorted(folders)


def found_note(path, name, extra=''):
    """'found', plus the real name when its capitalization differs."""
    note = 'found' if path.name == name else f'found as "{path.name}"'
    return note + extra


def check_entry(folder, name, is_dir=False):
    """One table row (passed, item, note) for a required file or folder."""
    label = name + '/' if is_dir else name
    matches = find_all(folder, name)
    path = find(folder, name)
    if path is None and len(matches) > 1:
        return False, label, 'more than one match: ' + ', '.join(f'"{p.name}"' for p in matches)
    if path is None:
        return False, label, 'missing' + (' (run the notebook that creates it)' if is_dir else '')
    if not is_dir:
        return True, label, found_note(path, name)
    count = sum(1 for p in path.rglob('*') if p.is_file())
    if count == 0:
        return False, label, 'empty (run the notebook that fills it)'
    return True, label, found_note(path, name, f' ({count} file{"s" * (count != 1)})')


def check_module(name):
    """Print a table for one module. Return True if every row passes."""
    rows = []  # (passed, item, note)
    official = find(ASSIGNMENTS, name)
    completed = find(COMPLETED, name)
    header = completed.name if completed else name

    if official is None:
        rows.append((False, name + '/', 'no module with this name in 02-Assignments (check the spelling)'))
    elif completed is None:
        rows.append((False, official.name + '/', 'not turned in: copy this module folder into 03-Completed'))
    else:
        notebooks, docs, folders = required_items(official)
        rows += [check_entry(completed, item) for item in notebooks + docs]
        rows += [check_entry(completed, item, is_dir=True) for item in folders]
        expected = {n.lower() for n in notebooks}
        for extra in sorted(p.name for p in completed.glob('*.ipynb')):
            if extra.lower() not in expected:
                rows.append((False, extra, 'unexpected name: rename it to match the original'))
        if find(completed, official.name):
            rows.append((False, f'{official.name}/{official.name}/', 'nested folder: move its contents up one level'))

    width = max([len('File')] + [len(item) for _, item, _ in rows])
    passed = sum(ok for ok, _, _ in rows)
    all_ok = passed == len(rows)

    print()
    print(bold(f'📂 03-Completed/{header}'))
    print(f'   {"":2}  {"File":<{width}}  Result')
    print(f'   {"":2}  {"-" * width}  {"-" * 40}')
    for ok, item, note in rows:
        print(f'   {PASS if ok else FAIL}  {item:<{width}}  {green(note) if ok else red(note)}')
    summary = f'{passed} of {len(rows)} checks passed'
    print(f'   {green(summary) if all_ok else red(summary)}')
    return all_ok


def resolve(arg):
    """Turn '05', '05-foundations', or '03-Completed/05-Foundations/' into a module name."""
    name = Path(arg.rstrip('/\\')).name
    known = module_names()
    exact = find(ASSIGNMENTS, name)
    if exact:
        return exact.name
    matches = [k for k in known if k.lower().startswith(name.lower())]
    if len(matches) == 1:
        return matches[0]
    hint = f'matches {", ".join(matches)}' if matches else 'matches no module'
    sys.exit(f'{FAIL} "{arg}" {hint}. Choose from:\n   ' + '\n   '.join(known))


def main(args):
    for folder in (ASSIGNMENTS, COMPLETED):
        if not folder.is_dir():
            sys.exit(f'{FAIL} Folder not found: {folder}')

    if args:
        modules = list(dict.fromkeys(resolve(a) for a in args))
    else:
        turned_in = sorted(p.name for p in COMPLETED.iterdir() if p.is_dir())
        if not turned_in:
            print('Nothing turned in yet: 03-Completed has no module folders.')
            return 0
        # Use the official name when one matches, so each module is checked once
        modules = list(dict.fromkeys((find(ASSIGNMENTS, n) or Path(n)).name for n in turned_in))

    results = [check_module(m) for m in modules]

    if not args:
        not_yet = [n for n in module_names() if not find_all(COMPLETED, n)]
        if not_yet:
            print(f'\nNot turned in yet: {", ".join(not_yet)}')

    ok = sum(results)
    print()
    line = f'{PASS if ok == len(results) else FAIL} {ok} of {len(results)} module(s) complete'
    print(bold(green(line) if ok == len(results) else red(line)))
    return 0 if ok == len(results) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
