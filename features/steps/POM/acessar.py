
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
import webbrowser
import time


def test_CesarScholl():
    driver = webbrowser.Chrome("")
    driver.get("https://www.cesar.school/")


class Acesso(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(20)

    locators = {
        "AcessarLink": ('css', '.header__btn-login'),
    }

    def acessoPag(self):
        self.AcessarLink.click_button()


class Blog(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        time.sleep(3)
        driver.implicitly_wait(10)

    locators = {
        "Blog": ('LINK_TEXT', 'Blog')
    }

    def acessarBlog(self):
        self.Demo.click_button()


class PassarPag(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(20)

    locators = {
        "PassarPagina": ('LINK_TEXT', 'Próxima página →')
    }

    def passarPag(self):
        self.PassarPagina.click_button()


class Imprimir:
    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(20)

    locators = {
        "Titulo2Post":
        ('LINK_TEXT', 'Grupo de Computação Física da CESAR School com resultado expressivo na IoT Student Contest'),
        "Data2Post": ('CSS_SELECTOR', '#post-59799 .date-month'),
        "Titulo3Post":
        ('LINK_TEXT', 'A defesa de dissertação de número 300 no Mestrado Profissional em Engenharia de Software'),
        "Autor3Post":
        ('LINK_TEXT', 'Comunicação School')

    }

    def Titulo2Post(self):
        self.Titulo2Post
        try:
            self.Titulo2Post
        except NoSuchElementException:
            return False
        return True
        print('', 'title')

    def Data2Post(self):
        self.Data2Post
        try:
            self.Data2Post
        except NoSuchElementException:
            return False
        return True
        print('', 'title')

    def Titulo3Post(self):
        self.Titulo3Post
        try:
            self.Titulo3Post
        except NoSuchElementException:
            return False
        return True
        print('', 'title')

    def Autor3Post(self):
        self.Autor3Post
        try:
            self.Autor3Post
        except NoSuchElementException:
            return False
        return True
        print('', 'title')
