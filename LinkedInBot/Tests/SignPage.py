import time

from Driver import Driver


class SignInPage:
    @staticmethod
    def goToLinkedinHome():
        Driver.instance.get('https://www.linkedin.com/home')
        Driver.instance.maximize_window()

    @staticmethod
    def login():
        sign_in_button = '//a[@class="nav__button-secondary"]'
        Driver.instance.find_element_by_xpath(sign_in_button).click()
        username = 'username'
        password = 'password'
        Driver.instance.find_element_by_id(username).send_keys('') #enter valid email
        Driver.instance.find_element_by_id(password).send_keys('') #enter valid password
        login_button = '//button[@aria-label="Sign in"]'
        Driver.instance.find_element_by_xpath(login_button).click()


