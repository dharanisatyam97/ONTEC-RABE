from selenium import webdriver


from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



from webdriver_manager.chrome import ChromeDriverManager

url ="https://www.karriere.at/jobs/java-developers"

driver = webdriver.Chrome() 

driver. get(url)
# class ="m-jobsListItem__dataContainer"
# //*[@id="jobsearchListing"]/div[1]/div[1]/div[6]/ol/li[1]/div/div/div[2]/h2 title
# //*[@id="jobsearchListing"]/div[1]/div[1]/div[6]/ol/li[1]/div/div/div[2]/div[1]/div[1] companny
# //*[@id="jobsearchListing"]/div[1]/div[1]/div[6]/ol/li[1]/div/div/div[2]/p snipet


data = driver.find_elements(By.CLASS_NAME,"m-jobsListItem__dataContainer")

for d in data:
	title = d.find_elements(By.XPATH,'//*[@id="jobsearchListing"]/div[1]/div[1]/div[6]/ol/li[1]/div/div/div[2]/h2')
	company = d.find_elements(By.XPATH,'//*[@id="jobsearchListing"]/div[1]/div[1]/div[6]/ol/li[1]/div/div/div[2]/div[1]/div[1]')
    # snipet =  d.find_elements(By.XPATH,'//*[@id="jobsearchListing"]/div[1]/div[1]/div[6]/ol/li[1]/div/div/div[2]/p')
	# print(title, company, snippet)
