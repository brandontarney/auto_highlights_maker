# Script to write date time to file
from datetime import datetime

now_date = datetime.now()
now_date_str = now_date.strftime("%y.%m.%d - %H.%M.%S")
#file = open("~/tarney/Videos/Fortnite/Fortnite/uploads/date_list.txt", "a") #Append
file = open("date_list.txt", "a") #Append
file.write(now_date_str)
file.write("\n")
file.close()
