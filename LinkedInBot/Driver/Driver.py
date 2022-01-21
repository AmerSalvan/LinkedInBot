from selenium import webdriver
import time

instance = None

def initialize():
    global instance
    instance = webdriver.Chrome()
    time.sleep(2)
    return instance


def quitdriver():
    global instance
    instance.quit()

