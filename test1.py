import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

def setup():
    global driver

    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')
    # Optional argument, if not specified will search path.
    #driver = webdriver.Chrome()

def teardown():
    driver.close()
    driver.quit()

def test_1():
    print("Test 1 = Verify that if an expression is entered into first-name and last-name, the first letter of each word capitalized")

    firstname = "john joe"
    lastname = "john"

    driver.get('file://C:/work/getting-setup/file2.html')
    enter_firstname = driver.find_element_by_id("firstname")
    enter_firstname.send_keys(firstname)
    enter_lastname = driver.find_element_by_id("lastname")
    enter_lastname.send_keys(lastname)

    expected_value = firstname.title()
    actual_value = enter_firstname.get_attribute('value')

    print(expected_value)
    print(actual_value)

    assert(expected_value == actual_value)


def test_2():
    print("Test 2 - Verify that when the form is loaded the age label is empty")
    driver.get('file://C:/work/getting-setup/file2.html')
    assert(driver.find_element_by_id("age").text == '')

def test_3():
    print("Test 3 - Verify that if a date is applied to the date picker, the age label shows the correct age")
    driver.get('file://C:/work/getting-setup/file2.html')
    birthday = "02022000\t"
    enter_dob = driver.find_element_by_id("birthday")
    enter_dob.send_keys(birthday)
    assert(driver.find_element_by_id("age").text == '21')

def test_4():
    print("Test 4 - Verify you have moved away and are at the BBC News site")
    driver.get('file://C:/work/getting-setup/file2.html')
    driver.find_element_by_id("bbc").click()
    assert(driver.title == 'Home - BBC News')

def test_5():
    print("Test 5 -Verify you have moved away and are at the QA site")
    driver.get('file://C:/work/getting-setup/file2.html')
    driver.find_element_by_id("bbc").click()
    #assert(driver.title == 'Home - BBC News')
    driver.get('file://C:/work/getting-setup/file2.html')
    driver.find_element_by_id("qa").click()
    #print(driver.title)
    assert(driver.title == 'QA – the UK’s leading tech skills organisation | Tech training online | Apprenticeships')

