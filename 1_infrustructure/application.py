# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_home_page(self, driver):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "home page").click()

    def return_to_groups(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
        # init group creation
        driver.find_element(By.NAME, "new").click()
        # fill group form
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit creation
        driver.find_element(By.NAME, "submit").click()
        self.return_to_groups()

    def create_contact(self, contact):
        driver = self.driver
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

    def open_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()