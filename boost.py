import datetime
import os

start = datetime.date(2024, 12, 1)
end = datetime.date(2024, 12, 31)
res_date = start
count = 0

while res_date <= end:
    for i in range(50000):  # 50k commits per day = 1.5M for Dec
        with open('change-file.txt', 'a') as wf:
            wf.write(f'\n{res_date}')
        os.system(f'git add . -q')
        os.system(f'git commit --date "{res_date}" -m "c" --no-gpg-sign -q')
        count += 1
        if count % 10000 == 0:
            os.system('git push -q')
            print(f'{count} commits pushed...')
    res_date += datetime.timedelta(days=1)

os.system('git push')
print('Done!')
