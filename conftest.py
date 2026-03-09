#driver created once per test
#automatic cleanup after test execution

import pytest
from utils.driver_factory import get_driver
import sys
import os

sys.path.append(os.path.abspath("."))

@pytest.fixture(scope="function")
def driver():

    driver = get_driver()

    yield driver

    driver.quit()