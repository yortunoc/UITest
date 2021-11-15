from datetime import datetime

import pytest

from core.drivers.DriverManager import DriverManager


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        DriverManager().driver.save_screenshot(f".\\Screenshots\\fail_{item.name}_{now}.png")