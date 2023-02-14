import subprocess
import time

from appium.webdriver.common.appiumby import AppiumBy
from behave import *
from pom.home_screen import HomeScreen
from logger import get_logger

log = get_logger()


@then('I see amazon logo')
def check_amazon_logo_visibility(context):
    log.debug('asserting amazon logo visibility')
    assert context.home_screen.home_logo_visible()
