from datetime import date, datetime, timedelta

def weekdays(year, month_name, day):
    date_list = []
    delta = timedelta(days=1)
    month_num = datetime.strptime(month_name, '%b').month
    start_date = date(int(year), int(month_num), int(day))
    for _ in range(0,5):
        date_list.append(start_date)
        start_date = start_date + delta
    return date_list

# print(weekdays(2000, 'Mar', 9))

import csv

# with open("henry_hub.csv") as csv_file:
#     writer = csv.writer(file)

# f = open("henry_hub.csv", "w")

# writer = csv.writer(f)
# writer.writerow(["SN", "Name", "Contribution"])
# writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
# writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
# writer.writerow([3, "Guido van Rossum", "Python Programming"])

# f.close()