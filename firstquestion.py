import csv
import datetime
def GoToSeconds(s : str) -> int:
    """Описание функции GoToSeconds
    
    Описание аргументов:

    s - строка вида 02:42:31
    """
    splitted = reversed(s.split(':'))
    power = 0
    res = 0
    for i in splitted:
        res += int(i) * 60 ** power
        power += 1

    return res
def BackGoString(second:int) -> str:
    """Описание функции BackGoString

    Описание аргументов:

    second - количество секунд
    """
    return f"{(second // 60 // 60) % 24:0>2}:{(second % 3600) // 60:0>2}:{(second % 3600) % 60:0>2}"

f = open('astronaut_time.txt', 'r', encoding='utf8')
row_names = f.readline()
rows = [(line.split('>')) for line in f.readlines()]
headers = ["WatchNumber", "numberStation", "cabinNumber", "timeStop", "timeNow"]
with open('new_time.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers, delimiter=',')
    writer.writeheader()
    for row in rows:
        insrow = {headers[x] : row[x].replace('\n', '') for x in range(len(headers) - 1)}
        insrow['timeNow'] = BackGoString(GoToSeconds(row[-2]) + 3600 * int(row[-1]))
        writer.writerow(insrow)
        if row[2] == '98-OYE':
            print(f"{insrow['timeNow']} - действительное время для каюты: {row[2]}")
