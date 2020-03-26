import re
import csv
from datetime import datetime, date

import requests
from bs4 import BeautifulSoup

from utils import weekdays

url = "https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm"

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

response = requests.get(url)

response_str = response.content.decode("utf-8")
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all("table")[4]
rows = table.find_all("tr")

f = open("henry_hub_natural_monthly_price.csv", "w")
writer = csv.writer(f)

writer.writerow(["Date", "Price"])

for row in rows[1:]:
    tds = [td.string for td in row.find_all("td")]
    if tds[0]:
        year = tds[0].strip()

        for month, price in zip(months, tds[1:]):
            if price:
                month_num = datetime.strptime(month, '%b').month
                date_obj = date(int(year), month_num, 1)
                writer.writerow([f"{date_obj.strftime('%Y-%m-%d')}", price])

f.close()
print("Done!")
