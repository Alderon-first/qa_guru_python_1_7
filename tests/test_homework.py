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
    #allure.attach(browser.save_screenshot(), name='Скриншот', attachment_type=allure.attachment_type.PNG)- почему-то
    # сохраняется пустой файл
    s(by.partial_text(num)).should(be.visible)

# тест на селене через лямбда шаги через with allure.step

# тест на селене с декоратором @allure.step