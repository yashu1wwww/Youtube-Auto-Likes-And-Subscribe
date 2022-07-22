import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email = 'darshu@gmail.com\n'  #enter your mail
password = 'dash\n'           #enter your pass

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(3)

url = 'https://youtu.be/9VpeTiz81gc' #replace with your required url of the video
driver.get(url)
time.sleep(5)
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
driver.find_element_by_css_selector('yt-icon.style-scope.ytd-toggle-button-renderer').click()
time.sleep(5)

url = 'https://www.youtube.com/c/DrBro' #replace with your required channel url which you want subscribe 
driver.get(url)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > tp-yt-paper-button > yt-formatted-string').click()
time.sleep(5)

#if you want community post like below is the code

url = 'https://www.youtube.com/c/DrBro/community'  #replace with your required channel community post url
driver.get(url)
driver.find_element_by_css_selector('yt-icon.style-scope.ytd-toggle-button-renderer').click()
time.sleep(10)
