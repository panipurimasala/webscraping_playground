import requests
from bs4 import BeautifulSoup
import pandas as pd

income_statement_dict = {}
balance_sheet_dict = {}
cash_flow_dict = {}
tickers = ["AAPL", "AMD"]


for tick in tickers:
    headings = {}
    income_statement = {}
    url = "https://finance.yahoo.com/quote/{}/financials".format(tick)
    headers = {"User-Agent":"Mozilla/5.0 Firefox"}
    page = requests.get(url, headers=headers)
    # print(page.headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    tabl = soup.find_all("div", {"class":"table svelte-1pgoo1f"})
    for t in tabl:
        heading = t.find_all("div", {"class" : "row svelte-1ezv2n5"})
        for head in heading:
            headings[head.get_text(separator="|").split("|")[0]] = head.get_text(separator="|").split("|")[2:-1]
    # print(headings)
        rows = t.find_all("div", {"class":"row lv-0 svelte-1xjz32c"})
        for row in rows:
            # income_statement[row.get_text(separator="|").split("|")[1]] =  row.get_text(separator="|").split("|")[3]
            s = row.get_text(separator="|").split("|")
            if(s[1] == ' ' and s[2] == ' '):
                income_statement[s[3]] =  row.get_text(separator="|").split("|")[5:]
            else:
                income_statement[s[1]] =  row.get_text(separator="|").split("|")[3:]
    datF = pd.DataFrame(income_statement).T
    datF.columns = headings["Breakdown"]
    income_statement_dict[tick] = datF
    # print(s)
# print(income_statement_dict)




#Balance sheet
for tick in tickers:
    headings = {}
    balance_sheet = {}
    url = "https://finance.yahoo.com/quote/{}/balance-sheet".format(tick)
    headers = {"User-Agent":"Mozilla/5.0 Firefox"}
    page = requests.get(url, headers=headers)
    # print(page.headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    tabl = soup.find_all("div", {"class":"table svelte-1pgoo1f"})
    for t in tabl:
        heading = t.find_all("div", {"class" : "row svelte-1ezv2n5"})
        for head in heading:
            headings[head.get_text(separator="|").split("|")[0]] = head.get_text(separator="|").split("|")[2:-1]
    # print(headings)
        rows = t.find_all("div", {"class":"row lv-0 svelte-1xjz32c"})
        for row in rows:
            # income_statement[row.get_text(separator="|").split("|")[1]] =  row.get_text(separator="|").split("|")[3]
            s = row.get_text(separator="|").split("|")
            if(s[1] == ' ' and s[2] == ' '):
                balance_sheet[s[3]] =  row.get_text(separator="|").split("|")[5:]
            else:
                balance_sheet[s[1]] =  row.get_text(separator="|").split("|")[3:]
    datF = pd.DataFrame(balance_sheet).T
    # print(datF)
    datF.columns = headings["Breakdown"]
    balance_sheet_dict[tick] = datF


for tick in tickers:
    headings = {}
    cash_flow = {}
    url = "https://finance.yahoo.com/quote/{}/balance-sheet".format(tick)
    headers = {"User-Agent":"Mozilla/5.0 Firefox"}
    page = requests.get(url, headers=headers)
    # print(page.headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    tabl = soup.find_all("div", {"class":"table svelte-1pgoo1f"})
    for t in tabl:
        heading = t.find_all("div", {"class" : "row svelte-1ezv2n5"})
        for head in heading:
            headings[head.get_text(separator="|").split("|")[0]] = head.get_text(separator="|").split("|")[2:-1]
    # print(headings)
        rows = t.find_all("div", {"class":"row lv-0 svelte-1xjz32c"})
        for row in rows:
            # income_statement[row.get_text(separator="|").split("|")[1]] =  row.get_text(separator="|").split("|")[3]
            s = row.get_text(separator="|").split("|")
            if(s[1] == ' ' and s[2] == ' '):
                cash_flow[s[3]] =  row.get_text(separator="|").split("|")[5:]
            else:
                cash_flow[s[1]] =  row.get_text(separator="|").split("|")[3:]
    datF = pd.DataFrame(cash_flow).T
    # print(datF)
    datF.columns = headings["Breakdown"]
    cash_flow_dict[tick] = datF


for tick in tickers:
    for col in income_statement_dict[tick].columns:
        income_statement_dict[tick][col] = income_statement_dict[tick][col].str.replace(',', '')
        income_statement_dict[tick][col] = income_statement_dict[tick][col].str.replace('-', '')
        income_statement_dict[tick][col] = pd.to_numeric(income_statement_dict[tick][col],errors="coerce")
        print(income_statement_dict[tick][col])

for tick in tickers:
    for col in balance_sheet_dict[tick].columns:
        balance_sheet_dict[tick][col] = balance_sheet_dict[tick][col].str.replace(',', '')
        balance_sheet_dict[tick][col] = balance_sheet_dict[tick][col].str.replace('-', '')
        balance_sheet_dict[tick][col] = pd.to_numeric(balance_sheet_dict[tick][col],errors="coerce")
        print(balance_sheet_dict[tick][col])

for tick in tickers:
    for col in cash_flow_dict[tick].columns:
        cash_flow_dict[tick][col] = cash_flow_dict[tick][col].str.replace(',', '')
        cash_flow_dict[tick][col] = cash_flow_dict[tick][col].str.replace('-', '')
        cash_flow_dict[tick][col] = pd.to_numeric(cash_flow_dict[tick][col],errors="coerce")
        print(cash_flow_dict[tick][col])
# print(income_statement_dict)