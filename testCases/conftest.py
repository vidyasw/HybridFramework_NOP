from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome()     # executable_path="E:\\chromedriver_win32\\chromedriver.exe")
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):                  # this will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):                             # this will return the browser value to setup method
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Vidya'
    config._metadata['Status'] = 'Pass'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
