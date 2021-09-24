from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 30
PROMISED_UP = 30
CHROME_DRIVER_PATH = "D:\Development\chromedriver.exe"
TWITTER_EMAIL = "yourTwitterEmail"
TWITTER_PASSWORD = "yourTwitterPassword"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """Opens speedtest by ookla, runs a speed test and returns download and upload speeds"""
        self.driver.get("https://www.speedtest.net/")

        time.sleep(2)
        start_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_button.click()

        time.sleep(60)
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '2]/div/div[2]/span')
        print(self.down.text)

        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '3]/div/div[2]/span')
        print(self.down.text)

    def tweet_at_provider(self):
        """ Logs in twitter, and creates a post if the retrived data speed is less than the global var"""
        self.driver.get("https://www.twitter.com/")

        # Log in
        time.sleep(3)
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div['
                                                         '1]/div/div[3]/a[2]/div')
        login_button.click()
        time.sleep(2)

        email_input = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        password_input = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password_input.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

        # Posts
        post_input = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        message = f"wag na hmpf slap uhm HA ha ha ha hehehe hehe tickle tickle"
        for word in message.split():
            post_input.send_keys(f"{word} ")
            time.sleep(0.2)

        time.sleep(1)
        send_tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        send_tweet.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# TODO make a if statement, if retrieved downlaod speed and upload speed is less than global variables,
#  PROMISED_DOWN and PROMISED UP, have bot message the provider
bot.get_internet_speed()

bot.tweet_at_provider()
