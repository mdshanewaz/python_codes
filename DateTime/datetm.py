import datetime

print(datetime.datetime.now())

today = datetime.datetime.utcnow()
print(today)

print(datetime.date.today())


currect_date = datetime.datetime.now()
print(currect_date.timetuple())

stru_time_obj = currect_date.timetuple()
print(stru_time_obj[0])
print(stru_time_obj[1])
print(stru_time_obj[2])

curt_date = datetime.datetime.now()
print(curt_date)

#strftime method converts date to string
curt_date_2 = datetime.datetime.strftime(curt_date, "%d/%m/%Y %H:%M:%S")
print(type(curt_date_2))
print(curt_date_2)

#strptime method converts string to date 
book_creation_date = "03, march, 2023"
book_creation_date_2 = datetime.datetime.strptime(book_creation_date, "%d, %B, %Y")
print(type(book_creation_date_2))
print(book_creation_date_2)
