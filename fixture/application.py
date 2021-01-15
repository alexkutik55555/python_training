from selenium.webdriver.android import webdriver


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".nav-dropdown-link:nth-child(4)").click()

    def open_users_dropdown(self):
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown-profile .nav__link").click()

    def open_cards_page(self):
        self.driver.find_element(By.LINK_TEXT, "Cards").click()
        element = self.driver.find_element(By.LINK_TEXT, "Cards")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.LINK_TEXT, "Suggested Edits")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def open_dashboard_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn--warmPink:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()

    def login(self, group):
        self.driver.set_window_size(1280, 742)
        self.driver.find_element(By.ID, "input-12").click()
        self.driver.find_element(By.ID, "input-12").send_keys(group.username)
        self.driver.find_element(By.ID, "input-15").send_keys(group.password)
        self.driver.find_element(By.CSS_SELECTOR, ".btn--warmPink:nth-child(1)").click()

    def open_home_page(self):
        self.driver.get("https://app.moviemethod.app/login")

    def destroy(self):
        self.driver.quit()