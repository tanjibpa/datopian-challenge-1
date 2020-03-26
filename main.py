import re
import csv
import requests
from bs4 import BeautifulSoup

from utils import weekdays

url = "https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm"

response = requests.get(url)

response_str = response.content.decode("utf-8")
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all("table")[5]
rows = table.find_all("tr")

f = open("henry_hub_natural_daily_price.csv", "w")
writer = csv.writer(f)

for row in rows[1:]:
    tds = [td.string for td in row.find_all("td")]
    if tds[0]:
        date_string = tds[0].strip()

        start_date_dict = re.match(
            r"(?P<year>\d{4}) (?P<month>\w{3})\s*-\s*(?P<day>\d+)", date_string
        ).groupdict()

        dates = weekdays(
            start_date_dict["year"], start_date_dict["month"], start_date_dict["day"]
        )

        for dt, price in zip(dates, tds[1:]):
            writer.writerow([dt.strftime("%b %d, %Y"), price])

f.close()
print("Done!")