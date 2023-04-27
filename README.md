# Youtube-Auto-Likes-And-Subscribe

Youtube Auto Likes,Subscribe & Also Community Post Like With Python

Replace "Email" and "Pass" in lines 7 and 8, respectively. Also, replace line 21 with the URL of the video you want to use. The script will automatically pause the video and hit the "like" and "subscribe" buttons. If you don't want to auto-post to the community tab, simply remove lines 30 to 31, save the file, and run it.

Note: Use accounts that don't have two-factor authentication.

After downloading the folder, extract it and open the command prompt. Enter "python" and check your Python version. Then enter "pip install undetected_chromedriver" and "pip install proxy" in the command prompt.

Next, download the appropriate chromedriver version that matches your PC's Chrome version from https://chromedriver.chromium.org/downloads. Extract the downloaded file to the same folder.

Open the command prompt in that folder and enter "yt.py" or double-click on the "yt.py" file to run the script.

👉Python Install Setup=https://youtu.be/4bUOrMj88Pc

👉Auto Yt Like Video=https://youtu.be/SO107aa8GMQ

👉Auto Yt Sub & Auto Community Post Like=https://youtu.be/t74knyA8ZQ0

👉Auto Yt Likes+Auto Sub +Auto Community Post Like=https://youtu.be/yre_drbKjss

👉 YouTube Auto Vote In Community Tab-https://youtu.be/DMHzxN-rZXg

If You Want Auto Community Vote Add Below Code In last Line Of Script 

url = 'https://www.youtube.com/channel/UCyDKApmpEVmESSue7v3qy3g/community' #put your community vote post url here

driver.get(url)

time.sleep(2)

driver.find_element_by_css_selector('#sign-in > tp-yt-paper-item > div > div.text-area.style-scope.ytd-backstage-poll-renderer > yt-formatted-string.choice-text.style-scope.ytd-backstage-poll-renderer').click()

time.sleep(15)

#it only vote first line only and for which vote tab is starting post in community tab

👉Note:-

👉if your selenium version is in latest version then 
the code never run 

👉open cmd and enter pip uninstall selenium

And enter 

pip install selenium==4.2.1
or
pip install selenium==4.2.0

and hit enter 

and 

python -c "import selenium; print(selenium.__version__)"
<to check the current version of selenium>

𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.






