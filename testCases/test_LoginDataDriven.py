from pageObjects.LoginPage import Login
from utilities.readPropertiesini import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time
import pytest


class Test_002_DDT_Login:

    baseurl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self,setup):
        self.logger.info('*********************** Test_002_DDT_Login ***********************')
        self.logger.info('*********************** Verifying Login DDT test ***********************')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("Number of rows :" ,self.rows)

        lst_status=[]   #empty list variable

        self.logger.info("******* Reading data from excel **********")
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_UserName(self.user)
            self.lp.set_Password(self.password)
            self.lp.click_Login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Passed****")
                    self.lp.click_Logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****Failed****")
                    self.lp.click_Logout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Failed****")
                    self.lp.click_Logout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("****Passed****")
                    # self.lp.click_Logout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*****Login DDT test Passed*****")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****Login DDT test Failed*****")
            self.driver.close()
            assert False

        self.logger.info('*********************** End of Test_002_DDT_Login ***********************')
        self.logger.info('*********************** Completed Test_002_DDT_Login ***********************')

