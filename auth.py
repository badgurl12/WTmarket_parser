from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# create a Firefox webdriver instance
driver = webdriver.Firefox()

# navigate to trade.gaijin.net
driver.get("https://trade.gaijin.net/")

time.sleep(1)

# find the login button and click it
signin_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Sign-in with Gaijin.Net')]")
signin_button.click()

time.sleep(1)

email_input = driver.find_element(By.ID, "email")
email_input.send_keys("oleksijspiluk@gmail.com")

pass_input = driver.find_element(By.ID, "password")
pass_input.send_keys("7894563210los")

login_button = driver.find_element(By.XPATH, "//input[@class='submit js-anti-several-clicks btn btn-blue']")
login_button.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, "searchInput")))

buyorderbutton = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[3]/div[1]/div/div/div[1]/div/ul[1]/li[3]/a/div")
buyorderbutton.click()



html = driver.page_source