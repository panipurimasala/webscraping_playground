import requests
from bs4 import BeautifulSoup
income_statement = {}
url = "https://finance.yahoo.com/quote/AMD/financials"
headers = {"User-Agent":"Mozilla/5.0 Firefox"}
page = requests.get(url, headers=headers)
# print(page.headers)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")
tabl = soup.find_all("div", {"class":"tableBody svelte-1pgoo1f"})
for t in tabl:
    rows = t.find_all("div", {"class":"row lv-0 svelte-1xjz32c"})
    for row in rows:
        # income_statement[row.get_text(separator="|").split("|")[1]] =  row.get_text(separator="|").split("|")[3]
        s = row.get_text(separator="|").split("|")
        if(s[1] == ' ' and s[2] == ' '):
          income_statement[s[3]] =  row.get_text(separator="|").split("|")[5]
        else:
           income_statement[s[1]] =  row.get_text(separator="|").split("|")[3]

print(income_statement)