from selenium.webdriver.common.by import By

class HomePage:

    HEADING = (By.TAG_NAME, "h1")

    def get_heading_text(self):
        return self.find(self.HEADING).text
