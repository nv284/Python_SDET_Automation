from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/html/html_tables.asp")

rows = driver.find_elements(
    By.XPATH,
    "//table[@id='customers']//tr"
)
for row in rows[1:]:
    print(row.text)

    #Find the country of "Alfreds Futterkiste".
    country = driver.find_element(
    By.XPATH,
    "//td[text()='Alfreds Futterkiste']/following-sibling::td[2]"
)

print(country.text)

#read complte table data 
rows = driver.find_elements(
    By.XPATH,
    "//table[@id='customers']//tr[position()>1]"
)

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")

    company = cols[0].text
    contact = cols[1].text
    country = cols[2].text

    print(company, contact, country)

# row count 
rows = len(driver.find_elements(
    By.XPATH,
    "//table[@id='customers']//tr"
))
print(rows)

#column count 
cols = len(driver.find_elements(
    By.XPATH,
    "//table[@id='customers']//tr[2]/td"
))
print(cols)

# find comapany name based on country name
company = "Island Trading"

country = driver.find_element(
    By.XPATH,
    f"//td[text()='{company}']/following-sibling::td[2]"
)

print(country.text)
driver.quit()