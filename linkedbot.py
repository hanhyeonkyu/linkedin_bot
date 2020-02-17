from selenium import webdriver
from time import sleep
from secret import username, password

class LinkedBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.linkedin.com/home")
        login_open=self.driver.find_element_by_xpath('/html/body/nav/a[3]')
        login_open.click()

        sleep(1.5)

        email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_in.send_keys(username)
        pw_in= self.driver.find_element_by_xpath('//*[@id="password"]')
        pw_in.send_keys(password)
        login_btn = self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
        login_btn.click()

        sleep(1)

    def go_people_view(self):
        people_sect_btn = self.driver.find_element_by_xpath('//*[@id="mynetwork-nav-item"]/a')
        people_sect_btn.click()

        sleep(2)

    def auto_add(self):
        self.go_people_view()
        sleep(1)
        i = 1
        while True:
            try:
                people_add=self.driver.find_element_by_xpath('//*[@id="ember{}"]'.format(str(i)))
                people_add.click()
            except Exception:
                i += 1
                print(i)
                pass
    
    def auto_send(self):
        pass

bot = LinkedBot()
bot.login()
