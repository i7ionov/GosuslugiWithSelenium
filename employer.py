from selenium import webdriver
import argparse
import time
import os


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
driver.get('https://59.gosuslugi.ru/service/5935949/5900000000161275583')
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
# нажимаем кнопку войти
but = driver.find_element_by_class_name("button-big")
but.click()
time.sleep(4)  # секунды
org = driver.find_element_by_id("org0")
assert org.get_attribute("onclick") == 'orgPage.selectOrg(0);'
org.click()
time.sleep(10)  # секунды
# нажимаем кнопку новый черновик заявления
but = driver.find_element_by_class_name("draft-new-button")
but.click()
time.sleep(20)  # секунды
# Данные документа, подтверждающего факт внесения сведений о юридическом лице в ЕГРЮЛ
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.UL.sved_ul']/div/textarea")
f.send_keys("123")
# должность
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.UL.Panel_Sign.FieldText_ULSign_Post']/div[1]/input")
f.clear()
f.send_keys("123")
# Фамилия
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.UL.Panel_Sign.FieldText_ULSign_LastName']/div[1]/input")
f.send_keys("ыва")
# Фамилия
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.UL.Panel_Sign.FieldText_ULSign_FirstName']/div[1]/input")
f.send_keys("ыва")
# Отчество
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.UL.Panel_Sign.FieldText82']/div[1]/input")
f.send_keys("ыва")
# КПП
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.ob.kod']/div[1]/input")
f.send_keys("111")
# Дата постановки на учет
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.ob.date_nalog']/div[1]/input")
f.send_keys("12.12.2012")
# Реквизиты постановки
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.ob.rekv_nalog']/div[1]/textarea")
f.send_keys("111")
# email
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep1.Panel_ContactUL.email_ul']/div[1]/input")
f.send_keys("ivsemionov@iggn.permkrai.ru")
# next
f = driver.find_element_by_id("__nextStep")
f.click()
time.sleep(10)  # секунды
# этап 2
# Номер квалификационного аттестата
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep2.Panel_Kval.num_kval']/div[1]/input")
f.send_keys("111")
# Серия квалификационного аттестата
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep2.Panel_Kval.ser_kval']/div[1]/input")
f.send_keys("111")
# Дата выдачи
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep2.Panel_Kval.date_kval']/div[1]/input")
f.send_keys("12.12.2012")
# Кем выдан
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep2.Panel_Kval.org_kvalif']/div[1]/textarea")
f.send_keys("111")
# чекбоксы
f = driver.find_element_by_id("Form5935949.FormStep2.Panel_Confirm.FieldCheckbox162")
f.click()
f = driver.find_element_by_id("Form5935949.FormStep2.Panel_Confirm.FieldCheckbox163")
f.click()
f = driver.find_element_by_id("Form5935949.FormStep2.Panel_Confirm.FieldCheckbox164")
f.click()
f = driver.find_element_by_id("Form5935949.FormStep2.Panel_Confirm.FieldCheckbox247")
f.click()
# Реквизиты документа, подтверждающего уплату государственной пошлины
# Номер
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep2.Panel_Duty.duty_number']/div[1]/input")
f.send_keys("111")
# Дата выдачи
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep2.Panel_Duty.duty_date']/div[1]/input")
f.send_keys("12.12.2012")
# next
f = driver.find_element_by_id("__nextStep")
f.click()
time.sleep(10)  # секунды
# этап 3
# Копии учредительных документов
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep3.Panel_Doc.doc1']/div[3]/input")
f.send_keys(os.path.dirname(os.path.realpath(__file__))+"\\1.pdf")
time.sleep(2)  # секунды
# Опись прилагаемых документов
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep3.Panel_Doc.doc2']/div[3]/input")
f.send_keys(os.path.dirname(os.path.realpath(__file__))+"\\1.pdf")
time.sleep(2)  # секунды
# Копия квалификационного аттестата
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep3.Panel_Doc.doc3']/div[3]/input")
f.send_keys(os.path.dirname(os.path.realpath(__file__))+"\\1.pdf")
time.sleep(2)  # секунды
# Копия приказа о назначении должностного лица
f = driver.find_element_by_xpath("//div[@id='Form5935949.FormStep3.Panel_Doc.AppointingOrder']/div[3]/input")
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
