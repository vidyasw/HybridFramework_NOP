from pageObjects.LoginPage import Login
from utilities.readPropertiesini import ReadConfig
from utilities.customLogger import LogGen
from datetime import datetime
import pytest


class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('*********************** Start of test_homePageTitle ***********************')
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        print("Actual Title: ",act_title)
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.logger.error(
                '*********************** Title verification has failed in test_homePageTitle ***********************')
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle_" +
                                        datetime.now().strftime("%d-%m-%y_%H-%M-%S") + ".png")
            self.driver.close()
            self.logger.info(
                '*********************** test_homePageTitle Needs debugging as it has failed***********************')
            assert False
        self.logger.info('***********************End of test_homePageTitle ***********************')

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Login(self,setup):
        self.logger.info('*********************** Start of test_Login ***********************')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.set_UserName(self.username)
        self.lp.set_Password(self.password)
        self.lp.click_Login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.logger.error(
                '*********************** Title verification has failed in test_Login ***********************')
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login_" +
                                        datetime.now().strftime("%d-%m-%y_%H-%M-%S") + ".png")
            self.driver.close()
            self.logger.info(
                '*********************** test_Login Needs debugging as it has failed***********************')
            assert False
        self.logger.info('***********************End of test_Login ***********************')
