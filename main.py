from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

service = Service(
    executable_path=r'I:\\py\\chromedriver\\chromedriver.exe',
    service_log_path=os.devnull,
)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)


url = 'https://icscalendar.com/preview/'

driver.get(url)
url_input = driver.find_element(By.ID, "ics_feed_url")
url_input.send_keys("webcal://api.hospitable.com/v1/team.ics?key=8dc2f2ae-d669-44b4-a30a-44f6fb10ec2f&token=e987ec0a-5265-4863-9623-2b1d2d2f6007&noCache")
button_input = driver.find_element(By.CLASS_NAME, "button")
button_input.click()

time.sleep(10)

driver.close()
driver.quit()
# driver.get("https://www.google.com")

# try:
#     # time.sleep(3)
#     url_input = driver.find_element(By.ID, "ics_feed_url")
#     url_input.clear()
#     url_input.send_keys("webcal://api.hospitable.com/v1/team.ics?key=8dc2f2ae-d669-44b4-a30a-44f6fb10ec2f&token=e987ec0a-5265-4863-9623-2b1d2d2f6007&noCache")
    
#     time.sleep(60)
# except Exception as ex: 
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()