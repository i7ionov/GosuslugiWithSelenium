from selenium import webdriver
import argparse
import os
import time


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--login', default='')
    parser.add_argument('-p', '--password', default='')
    return parser

parser = create_parser()
namespace = parser.parse_args()

# запускаем фаерфокс с профилем, в котором включена геолокация
profile = webdriver.FirefoxProfile()
profile.set_preference("geo.prompt.testing", True)
profile.set_preference("geo.prompt.testing.allow", True)
driver = webdriver.Firefox(profile)
# заходим на страницу создания заявления (ссылка "Получить услугу")
driver.get('https://59.gosuslugi.ru/service/5935932/5900000000161316865')
time.sleep(6)  # секунды
# заполняем телефон
tel = driver.find_element_by_class_name("flt_lbl_inp")
tel.click()
time.sleep(1)  # секунды
tel.send_keys(namespace.login)
# пароль
pas = driver.find_element_by_id("password")
pas.click()
time.sleep(1)  # секунды
pas.send_keys(namespace.password)
but = driver.find_element_by_class_name("button-big")
but.click()
time.sleep(4)  # секунды
person = driver.find_element_by_class_name("datalist-item")
assert person.get_attribute("onclick") == 'orgPage.selectPso();'
person.click()
time.sleep(10)  # секунды
# нажимаем кнопку новый черновик заявления
but = driver.find_element_by_class_name("draft-new-button")
but.click()
time.sleep(10)  # секунды
# next
f = driver.find_element_by_id("__nextStep")
f.click()
time.sleep(10)  # секунды
# next
f = driver.find_element_by_id("__nextStep")
f.click()
time.sleep(10)  # секунды
# Выдача квалификационного аттестата
f = driver.find_element_by_xpath("//div[@id='form_attestat.FormStep26.Panel_vidacha.FieldTextDate29']/div[1]/input")
f.send_keys("12.12.2012")
# next
f = driver.find_element_by_id("__nextStep")
f.click()
time.sleep(10)  # секунды
# загрузка файла
f = driver.find_element_by_xpath("//div[@id='form_attestat.FormStep75.Panel138.FieldUpload380']/div[3]/input")
f.send_keys(os.path.dirname(os.path.realpath(__file__))+"\\1.pdf")
time.sleep(2)  # секунды
# next
f = driver.find_element_by_id("__nextStep")
f.click()
time.sleep(10)  # секунды
# next
f = driver.find_element_by_id("__nextStep")
f.click()
time.sleep(10)  # секунды