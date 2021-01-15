from selenium.webdriver.android import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)

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

    def open_home_page(self):
        self.driver.get("https://app.moviemethod.app/login")

    def destroy(self):
        self.driver.quit()