from datetime import date, datetime, timedelta


def weekdays(year, month_name, day):
    date_list = []
    delta = timedelta(days=1)
    month_num = datetime.strptime(month_name, "%b").month
    start_date = date(int(year), int(month_num), int(day))
    for _ in range(0, 5):
        date_list.append(start_date)
        start_date = start_date + delta
    return date_list
