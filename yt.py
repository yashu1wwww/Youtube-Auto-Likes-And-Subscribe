https://github.com/xtekky/google-login-bypass/blob/main/login.py  #replace email and pass in 7 & 8 line and replace 13 line with these
'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
#See Screenshot Pic To Add Proxy
#remove 19 to 22 lines in 1 line code
#After Merge with 1st line code With Below Code 

time.sleep(3)

url = 'https://youtu.be/9VpeTiz81gc' #replace with your required url
driver.get(url)
time.sleep(5)
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
driver.find_element_by_css_selector('yt-icon.style-scope.ytd-toggle-button-renderer').click()
time.sleep(7)

url = 'https://www.youtube.com/c/DrBro' #replace with your required channel url
driver.get(url)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > tp-yt-paper-button > yt-formatted-string').click()
time.sleep(5)

url = 'https://www.youtube.com/c/DrBro/community'  #replace with your required channel community post url
driver.get(url)
driver.find_element_by_css_selector('yt-icon.style-scope.ytd-toggle-button-renderer').click()
time.sleep(10)
