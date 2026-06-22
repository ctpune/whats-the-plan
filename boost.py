import datetime
import os
import sys

branch = sys.argv[1] if len(sys.argv) > 1 else "main"

# Only commit on days that already have contributions in 2026 (Jun 14 - Aug 19)
dates = [
    datetime.date(2026, 6, 22),
    datetime.date(2026, 6, 23),
    datetime.date(2026, 6, 24),
    datetime.date(2026, 6, 25),
    datetime.date(2026, 6, 26),
    datetime.date(2026, 6, 29),
    datetime.date(2026, 7, 3),
    datetime.date(2026, 7, 6),
    datetime.date(2026, 7, 10),
    datetime.date(2026, 7, 20),
    datetime.date(2026, 7, 27),
    datetime.date(2026, 7, 28),
    datetime.date(2026, 7, 29),
    datetime.date(2026, 7, 30),
    datetime.date(2026, 7, 31),
    datetime.date(2026, 8, 3),
]

COMMITS_PER_DAY = 4  # ~50 commits total (16 days * 4)
count = 0

# Checkout or create branch
os.system(f'git checkout -b {branch} 2>nul || git checkout {branch}')

for res_date in dates:
    for i in range(COMMITS_PER_DAY):
        with open('change-file.txt', 'a') as wf:
            wf.write(f'\n{res_date}')
        os.system(f'git add .')
        os.system(f'git commit --date "{res_date}" -m "c" --no-gpg-sign -q')
        count += 1
        if count % 50 == 0:
            os.system(f'git push -u origin {branch} -q')
            print(f'[{branch}] {count} commits pushed...')

os.system(f'git push -u origin {branch} -q')
print(f'[{branch}] Done! Total: {count}')
