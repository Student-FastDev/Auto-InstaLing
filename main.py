from prettytable import PrettyTable
from genericpath import isfile
import json
import time
from selenium import webdriver
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import datetime

DEFAULT_SETTINGS = {
    "entries": 3,
    "headless": False,
    "login": "",
    "password": ""
}

def load_settings():
    if not isfile('settings.json'):
        with open('settings.json', 'w') as settings_file:
            json.dump(DEFAULT_SETTINGS, settings_file, indent=4)
    with open('settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
    return settings

def initialize_driver(headless):
    chrome_manager = ChromeDriverManager()
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--mute-audio")
    options.add_argument("--no-sandbox")
    chrome_driver_path = chrome_manager.install()
    version_main = int(chrome_manager.driver.get_browser_version_from_os().split('.')[0])
    driver = uc.Chrome(driver_executable_path=chrome_driver_path, version_main=version_main, options=options)
    return driver

def load_data():
    if not isfile('data.json'):
        data = {}
        with open("data.json", "w") as outfile:
            json.dump(data, outfile)
    else:
        with open('data.json', encoding='utf-8') as f:
            data = json.load(f)
    return data

def login(driver, LOGIN, PASSWORD):
    driver.get("https://instaling.pl/teacher.php?page=login")
    driver.implicitly_wait(0.5)
    login_box = driver.find_element(by=By.NAME, value="log_email")
    password_box = driver.find_element(by=By.NAME, value="log_password")
    s = driver.find_elements(By.TAG_NAME, "button")
    login_box.send_keys(LOGIN)
    password_box.send_keys(PASSWORD)
    s[1].click()

def process_session(driver, data, x):
    s2 = driver.find_element(By.XPATH, "//*[@id=\"continue_session_button\"]/h4") if driver.find_element(By.XPATH, "//*[@id=\"continue_session_page\"]/div[1]").is_displayed() else driver.find_element(By.XPATH, "//*[@id=\"start_session_button\"]/h4")
    s2.click()
    while True:
        try:
            time.sleep(2)
            t = driver.find_element(By.XPATH, "//*[@id=\"question\"]/div[2]/div[2]").text
            answer = driver.find_element(by=By.XPATH, value="//*[@id=\"answer\"]")
            a = data.get(t, "0")
            if a == "0":
                time.sleep(1)
                if driver.find_element(By.XPATH, "//*[@id=\"dont_know_new\"]").is_displayed():
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
        

def checkLogin():
    settings = load_settings()
    if (settings["login"] == "" or settings["password"] == ""):
        print("\033c")
        print("Error! No password or username.")
        return False
    return True

def checkEntries():
    settings = load_settings()
    if (settings["entries"] <= 0):
        print("\033c")
        print("Error! Entries cannot be lower than 1.")
        return False
    return True


if __name__ == "__main__":
    try:
        settings = load_settings()
        programDone = False

        table = PrettyTable()
        table.field_names = ["Date", "Session", "Resolving Time"]

        entries = settings["entries"]

        if (checkLogin() and checkEntries()):
            for x in range(1, entries + 1):
                y = datetime.datetime.now()
                start_time = y

                table.add_row([y, str(x) + " / Doing", "N/A"])
                print("\033c")
                print(table)

                driver = initialize_driver(settings["headless"])
                data = load_data()
                login(driver, settings["login"], settings["password"])
                
                time.sleep(3)
                if(driver.current_url == "https://instaling.pl/teacher.php?page=login"):
                    print("\033c")
                    print("Error! Invalid login or password.")
                    driver.quit()
                    break
                    

                a = driver.find_elements(By.TAG_NAME, "a")
                a[2].click()

                time.sleep(2)
                process_session(driver, data, x)

                end_time = datetime.datetime.now()
                resolving_time = end_time - start_time

                table.del_row(-1)
                table.add_row([y, str(x) + " / Done", resolving_time])

                print("\033c")
                print(table)
                programDone = True
            if (programDone):
                print ("Finished!")
    except:
        print("\033c")
        print("Error or program closed before finish!")
