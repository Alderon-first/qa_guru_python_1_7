from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure
from allure import attachment_type
from allure_commons.types import Severity


url = "https://github.com"
user_rep = "eroshenkoam/allure-example"
num = "#76"


# аннотации
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ushkoev")
@allure.feature("Задача проверки Issue")
@allure.story("Проверяем Issue в нашем репозитории")
@allure.link("https://github.com", name="test")
# прсто тест на селене + анотации
def test_github():
    browser.open(url)
    s(".header-search-input").click()
    s(".header-search-input").send_keys(user_rep).submit()
    s(by.link_text(user_rep)).click()
    s("#issues-tab").click()
    #browser.save_screenshot("screen")
    #allure.attach(browser.last_screenshot, name='Скриншот', attachment_type=allure.attachment_type.PNG)
    # сохраняется почему-то пустой файл
    s(by.partial_text(num)).should(be.visible)


# тест на селене через лямбда шаги через with allure.step
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open(url)

    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys(user_rep)
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text(user_rep)).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером "+num):
        s(by.partial_text(num)).should(be.visible)

# тест на селене с декоратором @allure.step
def test_decorator_steps():
    open_main_page(url)
    search_for_repository(user_rep)
    go_to_repository(user_rep)
    open_issue_tab()
    should_see_issue_with_number(num)


@allure.step("Открываем главную страницу")
def open_main_page(url_str):
    browser.open(url_str)


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
