# -*- coding: utf-8 -*-
import time
import json
import webbrowser
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
base_url = 'https://www.cesar.school/'


################################# cenario 1 ########################################
@given(u'que eu acesse o link do site')
def step_impl(context):
    context.web.get(base_url)
    context.web.maximize_window()
    context.web.add_cookie({"name": "test1", "value": "cookie1"})
    context.web.add_cookie({"name": "test2", "value": "cookie2"})

    print(context.web.get_cookies())
    time.sleep(5)
    # driver.quit()


@when(u'sou direcionada')
def step_impl(context):
    context.web.implicitly_wait(5)


@then(u'entro no site Cesar School')
def step_impl(context):
    context.web.get(base_url)
    time.sleep(5)

################################## cenario 2####################################


@given(u'que eu esteja na home do site Cesar School')
def step_impl(context):
    context.web.get(base_url)
    time.sleep(5)
    context.web.set_window_size(1294, 741)
    time.sleep(5)


@when(u'clico na opção "{texto}"')
def step_impl(context, texto):
    context.web.find_element(By.LINK_TEXT, "Blog").click()
    context.web.implicitly_wait(10)


@then(u'sou direcionada para a pagina Blog')
def step_impl(context):
    context.web.implicitly_wait(10)


################################## cenario 3####################################

@given(u'que esteja dentro da opção Blog')
def step_impl(context):
    context.web.implicitly_wait(10)


@when(u'scrollo até achar as opções de paginas')
def step_impl(context):
    time.sleep(10)
    context.web.set_window_size(1294, 741)
    time.sleep(5)


@then(u'clico para ir para proxima pagina')
def step_impl(context):
    context.web.implicitly_wait(10)
    context.web.find_element(By.LINK_TEXT, "Próxima página →").click()
    context.web.implicitly_wait(10)
################################## cenario 4####################################


@given(u'que eu esteja no segundo pagina de posts do blog')
def step_impl(context):
    time.sleep(10)


@when(u'navego pela pagina')
def step_impl(context):
    context.web.execute_script(
        "window.scrollTo(0, window.scrollY + 200)")
    context.web.implicitly_wait(10)


@then(u'imprimo o titulo "{texto}" da publicação do segundo posts')
def step_impl(context, texto):
    el1 = context.web.find_element(
        By.LINK_TEXT, "Grupo de Computação Física da CESAR School com resultado expressivo na IoT Student Contest")

    time.sleep(5)
    print('', el1.text)
    time.sleep(5)


@then(u'imprimo a data "{texto}" da publicação do segundo posts')
def step_impl(context, texto):
    el2 = context.web.find_element(
        By.CSS_SELECTOR, "#post-59799 .date-month")

    time.sleep(5)
    print('', el2.text)
    time.sleep(5)


@then(u'imprimo o titulo "{texto}" do terceiro posts')
def step_impl(context, texto):
    context.web.implicitly_wait(5)
    el3 = context.web.find_element(
        By.LINK_TEXT, "A defesa de dissertação de número 300 no Mestrado Profissional em Engenharia de Software")

    time.sleep(5)
    print('', el3.text)
    time.sleep(5)


@then(u'imprimo o autor "{texto}" do terceiro posts')
def step_impl(context, texto):
    el4 = context.web.find_element(
        By.LINK_TEXT, "Comunicação School")
    time.sleep(5)
    print('', el4.text)
    time.sleep(5)


@ then(u'navego até o final da pagina')
def step_impl(context):
    context.web.execute_script(
        "window.scrollTo(0, window.scrollY + 200)")
    context.web.implicitly_wait(10)


@ then(u'imprimo o endereço do Cesar School')
def step_impl(context):
    el5 = context.web.find_element(
        By.CSS_SELECTOR, ".onde > p")

    time.sleep(5)
    print('', el5.text)
    time.sleep(10)
