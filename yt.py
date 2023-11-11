import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email = 'darshu@gmail.com\n'  #enter your mail
password = 'dash123\n'           #enter your pass

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(3)



url = 'https://youtu.be/9VpeTiz81gc' #replace with your required url to auto like the video
driver.get(url)
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click() #pause the video 
time.sleep(1)

#like button
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()

time.sleep(4)

#the below code which auto sub after hitting the like....
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(3)

#the below code is which opens community tab of the channel and hit like for first post
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(4)
driver.close()

