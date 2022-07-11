from selenium import webdriver
from selenium.webdriver.common.by import By
from acessar import *


def setup():
    return webdriver.Chrome()


def test_CesarSchool():
    driver = setup()

    driver.get("https://www.cesar.school/")

    acesso_form = Acesso(driver)
    acesso_form.acessoPag()

    demo_form = Blog(driver)
    demo_form.acessarBlog()

    scroll_form = PassarPag(driver)
    scroll_form.passarPag()

    imprimir_form = Imprimir(driver)
    imprimir_form.Titulo2Post()
    imprimir_form.Data2Post()
    imprimir_form.Titulo3Post()
    imprimir_form.Autor3Post()

    WebDriverWait(driver, 30)
    driver.close()


if __name__ == "__main__":
    test_CesarScholl()
