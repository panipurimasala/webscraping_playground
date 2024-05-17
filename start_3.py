import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://finance.yahoo.com/quote/AAPL/key-statistics"
temp_stats = {}



headers = {"User-Agent":"Mozilla/5.0 Firefox"}
page = requests.get(url, headers=headers)
# print(page.headers)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")
tables = soup.find_all("table", {"class":"table svelte-104jbnt"})
#print(tables)

for tabl in tables:
#     heading = t.find_all("div", {"class" : "row svelte-1ezv2n5"})
#     for head in heading:
#         headings[head.get_text(separator="|").split("|")[0]] = head.get_text(separator="|").split("|")[2:-1]
# # print(headings)
    rows = tabl.find_all("tr", {"class": "svelte-104jbnt alt"})
    for row in rows:
        temp_stats[row.get_text(separator="|").split("|")[0]] =  row.get_text(separator="|").split("|")[1:]
        temp_stats[row.get_text(separator="|").split("|")[0]] = [item for item in row.get_text(separator="|").split("|")[1:] if item.strip()]
print(temp_stats)


#         s = row.get_text(separator="|").split("|")
#         if(s[1] == ' ' and s[2] == ' '):
#             income_statement[s[3]] =  row.get_text(separator="|").split("|")[5:]
#         else:
#             income_statement[s[1]] =  row.get_text(separator="|").split("|")[3:]