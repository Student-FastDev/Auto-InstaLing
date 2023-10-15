from genericpath import isfile
import json, time
from selenium import webdriver
import os
import stat
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import datetime
import sys
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager


# SETTINGS
# Entries in a session
entries = 3
# Login to InstaLing
LOGIN = ""
# Password to InstaLing
PASSWORD = ""
# SETTINGS


y = 0
time.sleep(1)
y = datetime.datetime.now()

print("-----")
print("Date: ", y)
print("-----")

for x in range(1, entries+1):
    chrome_manager = ChromeDriverManager()
    options = webdriver.ChromeOptions()
    options.add_argument("--mute-audio")

    # Delete the hashtag if you dont want the window
    #options.add_argument("--headless");

    options.add_argument("--no-sandbox")
    chrome_driver_path = chrome_manager.install()
    version_main = int(chrome_manager.driver.get_browser_version_from_os().split('.')[0])
    driver = uc.Chrome(driver_executable_path=chrome_driver_path, version_main=version_main, options=options)


    if (isfile('data.json') == False):
        data = {}
        with open("data.json", "w") as outfile:
            json.dump(data, outfile)

    else:
        f = open('data.json', encoding='utf-8')
        data = json.load(f)

    driver.get("https://instaling.pl/teacher.php?page=login")
    driver.implicitly_wait(0.5)

    login_box = driver.find_element(by=By.NAME, value="log_email")
    password_box = driver.find_element(by=By.NAME, value="log_password")
    s = driver.find_elements(By.TAG_NAME, "button")

    login_box.send_keys(LOGIN)
    password_box.send_keys(PASSWORD)
    s[1].click()

    a = driver.find_elements(By.TAG_NAME, "a")

    a[2].click()

    if (driver.find_element(By.XPATH, "//*[@id=\"continue_session_page\"]/div[1]").is_displayed()):
        s2 = driver.find_element(By.XPATH, "//*[@id=\"continue_session_button\"]/h4")
    else:
        s2 = driver.find_element(By.XPATH, "//*[@id=\"start_session_button\"]/h4")
    s2.click()

    while 1 == 1:
        try:
            time.sleep(2)

            t = driver.find_element(By.XPATH, "//*[@id=\"question\"]/div[2]/div[2]").text
            answer = driver.find_element(by=By.XPATH, value="//*[@id=\"answer\"]")

            a = data.get(t, "0")

            if (a == "0"):
                time.sleep(1)
                if (driver.find_element(By.XPATH,"//*[@id=\"dont_know_new\"]").is_displayed()):
                    time.sleep(1)
                    case3 = driver.find_element(by=By.XPATH, value="//*[@id=\"dont_know_new\"]")

                    case3.click()

                    time.sleep(1)
                    case4 = driver.find_element(by=By.XPATH, value="//*[@id=\"skip\"]")

                    case4.click()
                else:
                    case = driver.find_element(by=By.XPATH, value="//*[@id=\"check\"]")
                    time.sleep(1)

                    case.click()
                    time.sleep(1)

                    word = driver.find_element(by=By.XPATH, value="//*[@id=\"word\"]").text
                    data[t] = word

                    json_object = json.dumps(data, indent=4, ensure_ascii=False)
                    with open("data.json", "w", encoding='utf-8') as outfile:
                        outfile.write(json_object)
                    time.sleep(1)

                    case3 = driver.find_element(by=By.XPATH, value="//*[@id=\"nextword\"]")
                    case3.click()
            else:
                time.sleep(1)
                answer.send_keys(a)

                case = driver.find_element(by=By.XPATH, value="//*[@id=\"check\"]")
                time.sleep(1)

                case.click()
                time.sleep(1)

                word = driver.find_element(by=By.XPATH, value="//*[@id=\"word\"]").text
                if word != a:
                    print(word)
                    filepath = 'data.json'
                    with open(filepath, 'r') as fp:
                      data = json.load(fp)
                    del data[t]
                    with open(filepath, "w") as outfile:
                      json.dump(data, outfile)

                case2 = driver.find_element(by=By.XPATH, value="//*[@id=\"nextword\"]")
                  
                time.sleep(1)
                case2.click()
                                    
        except ElementNotInteractableException:
            driver.close()
            break
        except NoSuchElementException:
            driver.close()
            break
    print("Completed sessions: ", x)
