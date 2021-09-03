from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from threading import Thread
import time
import random
import gener_info
import uuid

class Generation_Bot(object):
    def __init__(self):
        str1 = str(uuid.uuid4())#'123456789'
        str2 = str(uuid.uuid4())#'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str1 + str2 + str3
        ls = list(str4)
        random.shuffle(ls)
        psw = ''.join([random.choice(ls) for x in range(12)])
        self.name = "User_" + psw
        self.password = self.name




def connect_function(bot_number):
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "90.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    time.sleep(1)
    #path = "C:/Users/zhora/PycharmProjects/geckodriver.exe"
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )
    time.sleep(2)
    #browser = webdriver.Firefox(executable_path=r'C:/Users/zhora/PycharmProjects/pythonProject1/geckodriver.exe')
    #f = open("C:/Users/zhora/PycharmProjects/pythonProject1/geckodriver.exe", 'r')
    #browser.get('http://seleniumhq.org/')

    print(bot_number)
    browser.get('http://192.168.43.8:3000/')
    time.sleep(1)
    print('OK')
    search_form = browser.find_element_by_id('root').find_elements_by_tag_name('div')
    sf0 = browser.find_element_by_xpath("/html/body/div/div/div/nav/div/nav").click()
    time.sleep(1)
    sf1 = browser.find_element_by_xpath("/html/body/div/div/div/div/a").click()
    time.sleep(1)
    Bot  = Generation_Bot()
    print(Bot.name, Bot.password)
    sf2 = browser.find_element_by_xpath("/html/body/div/div/div").find_elements_by_tag_name('input')
    time.sleep(1)
    sf2[0].send_keys(Bot.name)
    time.sleep(1)
    sf2[1].send_keys(Bot.password)
    time.sleep(1)
    sf2[2].send_keys(Bot.password)
    time.sleep(2)
    sf2[3].click()
    print('OK')
    time.sleep(5)
    browser.get('http://192.168.43.8:3000/')
    time.sleep(1)

    browser.find_element_by_xpath("/html/body/div/div/div/nav/div/nav").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div/div/div/div[2]/input[1]").send_keys(Bot.name)
    time.sleep(2)
    print('OK')
    browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div/input").send_keys(Bot.password)
    time.sleep(3)
    print('OK')
    browser.find_element_by_xpath("/html/body/div/div/div/div[2]/input[2]").click()
    time.sleep(2)

    # print('OK')
    # browser.find_element_by_xpath("/html/body/div/div/div/nav/div/nav/div/div[2]/div/div[1]").click()
    # time.sleep(3)
    # print('OK')
    # browser.find_element_by_xpath("/html/body/div/div/div/nav/div/nav/div/div[2]/div/div[4]").click()
    # time.sleep(2)
    # print('OK')
    # browser.find_element_by_xpath("/html/body/div/div/div/nav/div/nav").click()
    # time.sleep(2)
    # print('OK')
    # browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/input").send_keys(Bot.name)
    # time.sleep(2)
    # print('OK')
    # browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div/input").send_keys(Bot.password)
    # time.sleep(2)
    # print('OK')
    # browser.find_element_by_xpath("/html/body/div/div/div/div[2]/input[2]").click()
    time.sleep(2)
    print('OK')
    browser.find_element_by_xpath("/html/body/div/div/div/nav/div/nav/div/div[2]/div/div[1]").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div/div/div/nav/div/nav/div/div[2]/div/div[2]").click()
    time.sleep(2)
    for i in range(5):
        browser.find_element_by_xpath("/html/body/div/div/div/div[4]/div[1]/div[1]/div/div/input").send_keys(Bot.name + str(i))
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div/div/div/div[4]/div[1]/div[1]/div/div/div").click()
        time.sleep(2)
    browser.get('http://192.168.43.8:3000/')
    #http://192.168.43.8:3000/
    #http://192.168.65.2:3000/
    time.sleep(1)
    sf1 = browser.find_element_by_xpath("/html/body/div/div/div/nav/div/ul").find_elements_by_tag_name('li')
    sf1[2].click()
    sf2 = browser.find_element_by_xpath("/html/body/div/div/div").find_elements_by_tag_name('div')
    print(bot_number)
    sf3 = sf2[1].find_element_by_xpath("//form").find_elements_by_tag_name('input')
    print(bot_number)
    time.sleep(1)
    for i in range(6):
        print("begin "+str(i))
        sf3[1].clear()
        time.sleep(2)
        sf3[1].send_keys(gener_info.rand_title())
        time.sleep(2)
        sf3[0].click()
        time.sleep(4)
        # print(bot_number)

        print("mid " + str(i))
        try:
            sf2 = browser.find_element_by_xpath(
            "/html/body/div/div/div/div[4]/div[1]")
            print("0try " + str(i))
            time.sleep(2)
            sf2.click()
            time.sleep(2)
            print("1try " + str(i))
            browser.find_element_by_xpath("/html/body/div/div/div/div[5]/div[2]/div[1]/div[1]").click()
            time.sleep(2)
            print("2try " + str(i))
            browser.find_element_by_xpath("/html/body/div/div/div/div[5]/div[2]/div[1]/div[2]/div[1]").click()
            time.sleep(2)
            browser.find_element_by_xpath("/html/body/div/div/div/div[5]/div[2]/div[1]/div[1]").click()
            time.sleep(2)
            print("3try " + str(i))
            browser.find_element_by_xpath("/html/body/div/div/div/div[5]/div[1]").click()
            time.sleep(2)
            print("4try " + str(i))
        except:
            print("exc " + str(i))
            time.sleep(2)
            continue



    assert "No results found." not in browser.page_source
