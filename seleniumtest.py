from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#closes the pop-up
def click_decline_all(driver):
    try:
        decline_button = driver.find_element(By.ID, "W0wltc")
        decline_button.click()
    except NoSuchElementException:
        print("Didn't find the button")
        pass

#Input the word 'dog'
def search(search_box):
    driver.implicitly_wait(2)
    search_box.send_keys("dog")
    print("wrote")

#submits the word
def enter(search_box):
    search_box.send_keys(Keys.RETURN)
    print("tried to enter")

#checks if the word is in the results
def check_word_in_results(driver, word):
    try:
        result = driver.find_element(By.XPATH, f"//*[contains(text(), '{word}')]")
        return True
    except NoSuchElementException:
        return False

driver = webdriver.Firefox()
driver.get('https://www.google.com')
click_decline_all(driver)
search_box = driver.find_element(By.ID, "APjFqb")
search(search_box)
driver.implicitly_wait(5)
enter(search_box)
driver.implicitly_wait(5)

if check_word_in_results(driver, "dog"):
    print("The word 'dog' is found in the search results.")
else:
    print("The word 'dog' is NOT found in the search results.")

driver.implicitly_wait(5)

driver.quit()
