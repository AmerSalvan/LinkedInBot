

import time

from HomePage import *
from SignPage import *
from Driver import Driver
import unittest


class TestLinkedin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        Driver.initialize()

    def test_StartBot(self):
        SignInPage.goToLinkedinHome()
        SignInPage.login()
        HomePage.searchQaEngeners()
        HomePage.filterQaEngineersInSerbia()
        HomePage.addNewEngineers()
        time.sleep(500)

    @classmethod
    def tearDown(cls):
        Driver.quitdriver()