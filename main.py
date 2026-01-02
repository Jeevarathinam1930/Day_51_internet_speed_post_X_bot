from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import os
from selenium.webdriver.support.wait import WebDriverWait
internet="https://www.speedtest.net/"
x_url="https://x.com/i/flow/login"
API_key=os.environ.get("API_Key")
API_secrete=os.environ.get("API_secrete")
Access_token=os.environ.get("Access_token")
Access_secrete=os.environ.get("Access_secrete")
Internet_provider="@airtelindia"
import tweepy

class InternetSpeedTwitterBot:
    def __init__(self):
        driver_options = Options()
        user_data_dir=os.path.join(os.getcwd(),"Chromeprofile")
        driver_options.add_argument(f"--user-data-dir={user_data_dir}")
        driver_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=driver_options)
        self.wait=WebDriverWait(self.driver,5)
        self.client=tweepy.Client(consumer_key=API_key,consumer_secret=API_secrete,access_token=Access_token, access_token_secret=Access_secrete)
        self.up = 0
        self.down = 0
    def get_internet_speed(self):
        try:
            self.driver.get(internet)
            go=self.wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')))
            go.click()
            sleep(65)
            upload=self.driver.find_element(by=By.CLASS_NAME,value="upload-speed")
            self.up=upload.text
            print(f"The Uploading speed of my wifi is : {self.up}")
            download=self.driver.find_element(by=By.CLASS_NAME,value="download-speed")
            self.down=download.text
            print(f"The downloading speed of my wifi is : {self.down}")
            self.driver.close()
        except Exception as e:
            print(f"Error:{e}")
    def tweet_at_provider(self):
        tweet=f"Hey! {Internet_provider} I have the good internet speed by connecting my laptop to mobile hotspot with the downloading speed of {self.down} and uploading speed of {self.up}"
        try:
            self.client.create_tweet(text=tweet)
            print("✅ Tweet posted successfully.")
        except Exception as e:
            print("❌ Error posting tweet:", e)

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

