
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\JAQ\Documents\\PROYECTO\\chromedriver_win32\\chromedriver")

# Puts an Implicit wait, Will wait for 10 seconds before throwing exception
driver.implicitly_wait(0.5)

# Launch website
driver.get("https://www.calculator.net")



# Click on Math Calculators
driver.find_element(By.XPATH, "//*[@id=\"contentout\"]/table/tbody/tr/td[3]/div[2]/a").click()

# Click on Percent Calculators
driver.find_element(By.XPATH, "//*[@id=\"content\"]/table[2]/tbody/tr/td/div[3]/a").click()

# Enter value 10 in the first number of the percent Calculator
driver.find_element(By.ID, "cpar1").send_keys("10")

# Enter value 50 in the second number of the percent Calculator
driver.find_element(By.ID, "cpar2").send_keys("50")

# Click Calculate Button
driver.find_element(By.XPATH, "//*[@id = 'content']/table/tbody/tr[2]/td/input[2]").click()



# Get the Result Text based on its xpath
result = driver.find_element(By.XPATH, "//*[@id = 'content']/p[2]/font/b").text

# Print a Log In message to the screen
print(" The Result is " + result)

driver.quit()