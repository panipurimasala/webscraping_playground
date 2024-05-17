from selenium import webdriver
from selenium.webdriver.common.by import By

path = "/Users/anirudhkrishnakumar/Desktop/chromedriver-mac-arm64/chromedriver"

service = webdriver.chrome.service.Service(path)
service.start()

ticker = "AAPL"
url = "https://finance.yahoo.com/quote/{}/financials".format(ticker)

#created driver of chrome type
driver = webdriver.Chrome(service=service)
#hgets data from chrome webpage 
driver.get(url)

#waits 3 seconds so that if tere is a lag the selenium will wait 3 seconds until it opens the page to check if it has been rendered
driver.implicitly_wait(3)

table = driver.find_element(By.XPATH, "//div[@class='table svelte-1pgoo1f']").text

#print(table)


income_st_dir = {}
table_heading = driver.find_elements(By.XPATH, "//*[contains(@class, 'column svelte-1ezv2n5') and (contains(@class, 'alt') or not(contains(@class, 'alt')))]")
headings = []
for cell in table_heading:
    headings.append(cell.text)

table = driver.find_elements(By.XPATH, "//*[contains(@class, 'row lv-0 svelte-1xjz32c')]")

for cell in table:
    s = cell.text.split("\n")
    income_st_dir[s[0]] = s[1:]

print(income_st_dir)