import datetime

currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
#print(currentdate.day)
# Allow you to specify the date fromat
print(currentDate.strftime('%d,%b,%y'))
print(currentDate.strftime('%D,%B,%Y'))
print(currentDate.strftime('%D'))