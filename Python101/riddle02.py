from datetime import datetime


until = datetime.now().second + 2
while datetime.now().second != until:
    print('waiting...')

print(f'We are at {until} seconds!')
