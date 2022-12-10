import datetime
import time

today = datetime.date.today()
print(today)
d1 = today.strftime('%d/%m/%Y')
d2 = today.strftime('%B %d, %Y')
print(f'{d1} \t- \t{d2}')

now = datetime.datetime.now()
timer = now.strftime('%H:%M:%S')
date = now.strftime('year= %Y,\tmonth=%m,\tday=%d')
print(f'{timer}\t{date}')
print("-" * 40)
print("Wynik")
for a in range(1, 10):
    print(f"report{datetime.datetime.now().strftime('%H%M%S')}.txt")
    time.sleep(2)
