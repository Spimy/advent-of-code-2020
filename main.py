import os

days = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d) and d != '.git']
paths = [os.path.join(os.getcwd(), day) for day in days]

for index, day in enumerate(days):
    print(f'{index + 1}. {day}')

while True:
    selected_day = int(input('Run script for day: '))

    if not 1 <= selected_day <= len(days):
        print('Exiting for entering an inexistent day...')
        break

    exec(open(f'{paths[selected_day - 1]}\\main.py').read())
    print()
