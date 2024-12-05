from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///Users/Bruk/Documents/Projects/PythonProjects/Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")
username = driver.find_element_by_name('username')
print("My input element is:")
print(username)
driver.close()
