class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, group):
        self.app.driver.set_window_size(1280, 742)
        self.app.driver.find_element(By.ID, "input-12").click()
        self.app.driver.find_element(By.ID, "input-12").send_keys(group.username)
        self.app.driver.find_element(By.ID, "input-15").send_keys(group.password)
        self.app.driver.find_element(By.CSS_SELECTOR, ".btn--warmPink:nth-child(1)").click()

    def logout(self):
        self.app.driver.find_element(By.CSS_SELECTOR, ".nav-dropdown-link:nth-child(4)").click()
