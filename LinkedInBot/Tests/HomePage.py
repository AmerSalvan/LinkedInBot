import time
from selenium.webdriver.common.action_chains import ActionChains
from Driver import Driver
from selenium.webdriver.common.keys import Keys


class HomePage():

    @staticmethod
    def searchQaEngeners():
        searchInput = '//input[@aria-label="Search"]'
        Driver.instance.find_element_by_xpath(searchInput).send_keys('Qa engineers')
        Driver.instance.find_element_by_xpath(searchInput).send_keys(Keys.ENTER)

    @staticmethod
    def filterQaEngineersInSerbia():
        filterbutton = '//button[@aria-label="All filters"]'
        time.sleep(5)
        Driver.instance.find_element_by_xpath(filterbutton).click()
        addlocation = '/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[6]/button/span'
        time.sleep(2)
        Driver.instance.find_element_by_xpath(addlocation).click()
        addserbia = '//input[@placeholder="Add a location"]'
        time.sleep(2)
        Driver.instance.find_element_by_xpath(addserbia).send_keys("Serbia")
        time.sleep(5)
        Driver.instance.find_element_by_xpath(addserbia).send_keys(Keys.DOWN)
        Driver.instance.find_element_by_xpath(addserbia).send_keys(Keys.ENTER)
        showResults = '//button[@aria-label="Apply current filters to show results"]'
        time.sleep(2)
        Driver.instance.find_element_by_xpath(showResults).click()

    @staticmethod
    def addNewEngineers():
        connectButton = '/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[2]/div/div/div[3]/button'
        time.sleep(5)
        Driver.instance.find_element_by_xpath(connectButton).click()
        sendButton = '//button[@aria-label="Send now"]'
        time.sleep(2)
        Driver.instance.find_element_by_xpath(sendButton).click()
