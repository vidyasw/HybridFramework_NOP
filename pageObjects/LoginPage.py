class Login():

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_Login_xpath = ".//input[@value ='Log in']"
    link_Logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def set_UserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def set_Password(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_Login(self):
        self.driver.find_element_by_xpath(self.btn_Login_xpath).click()

    def click_Logout(self):
        self.driver.find_element_by_link_text(self.link_Logout_linktext).click()