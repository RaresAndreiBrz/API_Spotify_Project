from seleniumbase import Driver


class Browser():

    chrome = Driver(browser="chrome", headless=False)
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.set_page_load_timeout(10)

    def close(self):
        self.chrome.quit()
