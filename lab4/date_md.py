# subtract 5 days from current date

import datetime
current=datetime.datetime.now()

x = current - datetime.timedelta(days=5)
#ЗАМЕТКА:datetime.timedelta()- позволяет выполнять матюдействия с датами

print("current date: ",current.strftime("%Y-%m-%d"))
print("5 days ago: ",x.strftime("%Y-%m-%d"))


#yesterday,today,tomorrow

import datetime
current=datetime.datetime.now()

yesterday = current - datetime.timedelta(days=1)
tomorrow = current + datetime.timedelta(days=1)

#ЗАМЕТКА:datetime.timedelta()- позволяет выполнять матюдействия с датами

print("yesterday: ", yesterday.strftime("%Y-%m-%d"))
print("current date: ", current.strftime("%Y-%m-%d"))
print("tomorrow: ", tomorrow.strftime("%Y-%m-%d"))



#drop microseconds from datetime


import datetime 
current = datetime.datetime.now()
x = current.replace(microsecond=0)

print("Current date: ", current)
print("Without microsecinds: ", x)



#two date difference in seconds
import datetime


def get_datetime_input(x):
    date_string= input(x + "(format: YYYY-MM-DD HH:MM:SS): ")
    return datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")


date_1 = get_datetime_input("First date ")
date_2 = get_datetime_input("Second date ")

difference = abs((date_1 - date_2).total_seconds())

print("Difference in seconds: ", difference)

