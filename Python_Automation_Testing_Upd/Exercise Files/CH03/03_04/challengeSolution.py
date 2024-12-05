from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver= webdriver.Firefox()
driver.get("http://wiki.python.org/moin/FrontPage");

# Automating searching functionality
search = driver.find_element(By.ID, 'searchinput');
search.clear();
search.send_keys("Beginner");
time.sleep(2)
search.send_keys(Keys.RETURN);

time.sleep(3)

# Automating the selection of the search results on the dropdown
select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[5]/form/div/select'))
# select.select_by_index(1)
time.sleep(2)
select.select_by_visible_text("Raw Text")
time.sleep(5)

driver.close()