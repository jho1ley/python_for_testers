from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self, driver):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home page").click()

    def create(self, contact):
        driver = self.app.driver
        # open contact form
        driver.find_element(By.LINK_TEXT, "add new").click()
        # adding fistname
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        # adding lastname
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").clear()
        driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        # adding nickname
        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").clear()
        driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        # adding information about company
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").clear()
        driver.find_element(By.NAME, "company").send_keys(contact.company)
        # adding information about address
        driver.find_element(By.NAME, "address").click()
        driver.find_element(By.NAME, "address").clear()
        driver.find_element(By.NAME, "address").send_keys(contact.address)
        # adding home number
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").clear()
        driver.find_element(By.NAME, "home").send_keys(contact.home)
        # adding mobile number
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").clear()
        driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        # adding email address
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys(contact.email)
        # saving contact
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_home_page(driver)
