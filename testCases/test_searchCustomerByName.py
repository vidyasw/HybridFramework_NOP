import time
from pageObjects.LoginPage import Login
from pageObjects.AddcustomersPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readPropertiesini import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.set_UserName(self.username)
        self.lp.set_Password(self.password)
        self.lp.click_Login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
        self.driver.close()
