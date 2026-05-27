import os

from selenium import webdriver


class DriverFactory:

    @staticmethod
    def get_driver(config):

        browser = config.get("browser", "name")
        headless = config.get("browser", "headless")
        implicit_wait = config.get("browser", "implicit_wait")

        remote_url = config.get(
            "selenium",
            "remote_url"
        )

        if browser.lower() == "chrome":

            options = webdriver.ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-notifications")
            options.add_argument("--remote-allow-origins=*")

            driver = webdriver.Remote(
                command_executor=remote_url,
                options=options
            )

        else:
            raise Exception(f"Browser '{browser}' not supported")

        driver.implicitly_wait(implicit_wait)

        return driver