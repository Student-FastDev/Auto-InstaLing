# Import necessary libraries
from prettytable import PrettyTable
from genericpath import isfile
from clear_screen import clear
import json
import time
from selenium import webdriver
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import datetime

# Define settings
DEFAULT_SETTINGS = {
    "entries": 3,
    "headless": False,
    "login": "",
    "password": ""
}

# Function to load settings from a JSON file
def load_settings():
    # Check if settings file exists
    if not isfile('settings.json'):
        # If not, create one with default settings
        with open('settings.json', 'w') as settings_file:
            json.dump(DEFAULT_SETTINGS, settings_file, indent=4)
    # Open the settings file and load the settings
    with open('settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
    # Return the settings
    return settings

# Function to initialize the driver
def initialize_driver(headless):
    # Setup ChromeDriverManager
    chrome_manager = ChromeDriverManager()
    # Setup ChromeOptions
    options = webdriver.ChromeOptions()
    # If headless mode is enabled, add the corresponding argument
    if headless:
        options.add_argument("--headless")
    # Add other necessary arguments
    options.add_argument("--mute-audio")
    options.add_argument("--no-sandbox")
    
    # Install the chromedriver and get its path
    chrome_driver_path = chrome_manager.install()
    # Get the main version of the browser
    version_main = int(chrome_manager.driver.get_browser_version_from_os().split('.')[0])
    driver = uc.Chrome(driver_executable_path=chrome_driver_path, version_main=version_main, options=options)
    return driver

# Function to load data from a JSON file
def load_data():
    # Check if data file exists
    if not isfile('data.json'):
        # If not, create an empty data dictionary and write it to a new file
        data = {}
        with open("data.json", "w") as outfile:
            json.dump(data, outfile)
    else:
        # If file exists, open it and load the data
        with open('data.json', encoding='utf-8') as f:
            data = json.load(f)
    # Return the loaded data
    return data

# Function to login to the website
def login(driver, LOGIN, PASSWORD):
    # Navigate to the login page
    driver.get("https://instaling.pl/teacher.php?page=login")
    # Wait for elements to load
    driver.implicitly_wait(0.5)
    # Find the login and password input boxes
    login_box = driver.find_element(by=By.NAME, value="log_email")
    password_box = driver.find_element(by=By.NAME, value="log_password")
    # Find the login button
    s = driver.find_elements(By.TAG_NAME, "button")
    # Enter the login and password
    login_box.send_keys(LOGIN)
    password_box.send_keys(PASSWORD)
    # Click the login button
    s[1].click()

# Function to process a session
def process_session(driver, data, x):
    # Find the continue session button if it's displayed, otherwise find the start session button
    s2 = driver.find_element(By.XPATH, "//*[@id=\"continue_session_button\"]/h4") if driver.find_element(By.XPATH, "//*[@id=\"continue_session_page\"]/div[1]").is_displayed() else driver.find_element(By.XPATH, "//*[@id=\"start_session_button\"]/h4")
    # Click the found button
    s2.click()
    # Enter a loop to process the session
    while True:
        try:
            # Wait for elements to load
            time.sleep(2)
            # Find the question text
            t = driver.find_element(By.XPATH, "//*[@id=\"question\"]/div[2]/div[2]").text
            # Find the answer input box
            answer = driver.find_element(by=By.XPATH, value="//*[@id=\"answer\"]")
            # Get the answer from the data dictionary
            a = data.get(t, "0")
            # If the answer is not in the data dictionary
            if a == "0":
                # Wait for elements to load
                time.sleep(1)
                # If the "Don't Know New" button is displayed
                if driver.find_element(By.XPATH, "//*[@id=\"dont_know_new\"]").is_displayed():
                    # Wait for elements to load
                    time.sleep(1)
                    # Find the "Don't Know New" button
                    case3 = driver.find_element(by=By.XPATH, value="//*[@id=\"dont_know_new\"]")
                    # Click the "Don't Know New" button
                    case3.click()
                    # Wait for elements to load
                    time.sleep(1)
                    # Find the "Skip" button
                    case4 = driver.find_element(by=By.XPATH, value="//*[@id=\"skip\"]")
                    # Click the "Skip" button
                    case4.click()
                else:
                    # Find the "Check" button
                    case = driver.find_element(by=By.XPATH, value="//*[@id=\"check\"]")
                    # Wait for elements to load
                    time.sleep(1)
                    # Click the "Check" button
                    case.click()
                    # Wait for elements to load
                    time.sleep(1)
                    # Find the word text
                    word = driver.find_element(by=By.XPATH, value="//*[@id=\"word\"]").text
                    # Add the word to the data dictionary
                    data[t] = word
                    # Convert the data dictionary to a JSON string
                    json_object = json.dumps(data, indent=4, ensure_ascii=False)
                    # Write the JSON string to the data file
                    with open("data.json", "w", encoding='utf-8') as outfile:
                        outfile.write(json_object)
                    # Wait for elements to load
                    time.sleep(1)
                    # Find the "Next word" button
                    case3 = driver.find_element(by=By.XPATH, value="//*[@id=\"nextword\"]")
                    # Click the "Next word" button
                    case3.click()
            else:
                # Wait for elements to load
                time.sleep(1)
                # Enter the answer in the answer input box
                answer.send_keys(a)
                # Find the "Check" button
                case = driver.find_element(by=By.XPATH, value="//*[@id=\"check\"]")
                # Wait for elements to load
                time.sleep(1)
                # Click the "Check" button
                case.click()
                # Wait for elements to load
                time.sleep(1)
                # Find the word text
                word = driver.find_element(by=By.XPATH, value="//*[@id=\"word\"]").text
                # If the word is not the same as the answer
                if word != a:
                    # Open the data file and load the data
                    filepath = 'data.json'
                    with open(filepath, 'r') as fp:
                        data = json.load(fp)
                    # Remove the question from the data dictionary
                    del data[t]
                    # Write the updated data dictionary to the data file
                    with open(filepath, "w") as outfile:
                        json.dump(data, outfile)
                # Find the "Next word" button
                case2 = driver.find_element(by=By.XPATH, value="//*[@id=\"nextword\"]")
                # Wait for elements to load
                time.sleep(1)
                # Click the "Next word" button
                case2.click()
        # If an ElementNotInteractableException is raised
        except ElementNotInteractableException:
            # Close the driver
            driver.close()
            # Break the loop
            break
        # If a NoSuchElementException is raised
        except NoSuchElementException:
            # Close the driver
            driver.close()
            # Break the loop
            break
        

# Function to check if login credentials are present
def checkLogin():
    # Load settings from a file or other source
    settings = load_settings()
    # Check if the login or password fields are empty
    if (settings["login"] == "" or settings["password"] == ""):
        # Clear the console
        clear()
        # Print an error message
        print("Error! No password or username.")
        # Return False indicating that the login check failed
        return False
    # If the login and password fields are not empty, return True indicating that the login check passed
    return True

# Function to check if the number of entries is valid
def checkEntries():
    # Load settings from a file or other source
    settings = load_settings()
    # Check if the number of entries is less than or equal to 0
    if (settings["entries"] <= 0):
        # Clear the console
        clear()
        # Print an error message
        print("Error! Entries cannot be lower than 1.")
        # Return False indicating that the entries check failed
        return False
    # If the number of entries is greater than 0, return True indicating that the entries check passed
    return True

if __name__ == "__main__":
    try:
        # Load settings from a file
        settings = load_settings()
        # Initialize a flag to indicate whether the program is done
        programDone = False

        # Create a table with the field names "Date", "Session", and "Resolving Time"
        table = PrettyTable()
        table.field_names = ["Date", "Session", "Resolving Time"]

        # Get the number of entries from the settings
        entries = settings["entries"]

        # If the login credentials and number of entries are valid
        if (checkLogin() and checkEntries()):
            # For each entry
            for x in range(1, entries + 1):
                # Get the current date and time
                y = datetime.datetime.now()
                start_time = y

                # Add a row to the table with the current date and time, the session number, and "N/A" for the resolving time
                table.add_row([y, str(x) + " / Doing", "N/A"])
                # Clear the console
                clear()
                # Print the table
                print(table)

                # Initialize the driver
                driver = initialize_driver(settings["headless"])
                # Load the data
                data = load_data()
                # Log in
                login(driver, settings["login"], settings["password"])
                
                # Wait for elements to load
                time.sleep(3)
                # If the current URL indicates that the login failed
                if(driver.current_url == "https://instaling.pl/teacher.php?page=login"):
                    # Clear the console
                    clear()
                    # Print an error message
                    print("Error! Invalid login or password.")
                    # Quit the driver
                    driver.quit()
                    # Break the loop
                    break
                    

                # Find all elements with the tag name "a"
                a = driver.find_elements(By.TAG_NAME, "a")
                # Click the third element in the list
                a[2].click()

                # Wait for elements to load
                time.sleep(2)
                # Process the session
                process_session(driver, data, x)

                # Get the current date and time
                end_time = datetime.datetime.now()
                # Calculate the resolving time
                resolving_time = end_time - start_time

                # Delete the last row in the table
                table.del_row(-1)
                # Add a row to the table with the current date and time, the session number, and the resolving time
                table.add_row([y, str(x) + " / Done", resolving_time])

                # Clear the console
                clear()
                # Print the table
                print(table)
                # Set the programDone flag to True
                programDone = True
                if (programDone):
                    # Print a message indicating that the program is finished
                    print ("Finished!")
    # If an exception is raised
    except:
        # Clear the console
        clear()
        # Print an error message
        print("Error or program closed before finish!")
input("Press enter to exit.")
