import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
# Optional argument, if not specified will search path.
#driver = webdriver.Chrome()
firstname = "john joe"
lastname = "john"
birthday = "02022000\t"
driver.get('file://C:/work/getting-setup/file2.html')
enter_firstname = driver.find_element_by_id("firstname")
enter_firstname.send_keys(firstname)
enter_lastname = driver.find_element_by_id("lastname")
enter_lastname.send_keys(lastname)

expected_value = firstname.title()
actual_value = enter_firstname.get_attribute('value')

print(expected_value)
print(actual_value)

print("Test 1 = Verify that if an expression is entered into first-name and last-name, the first letter of each word capitalized")
assert(expected_value == actual_value)


print("Test 2 - Verify that when the form is loaded the age label is empty")
assert( driver.find_element_by_id("age").text == '')

enter_dob = driver.find_element_by_id("birthday")
enter_dob.send_keys(birthday)
print("Test 3 - Verify that if a date is applied to the date picker, the age label shows the correct age")
assert(driver.find_element_by_id("age").text == '21')

driver.find_element_by_id("bbc").click()
print("Test 4 - Verify you have moved away and are at the BBC News site")
assert(driver.title == 'Home - BBC News')


driver.get('file://C:/work/getting-setup/file2.html')
driver.find_element_by_id("qa").click()

print("Test 5 -Verify you have moved away and are at the QA site")
assert(driver.title == 'QA – the UK’s leading tech skills organisation | Tech training | Apprenticeships')




driver.quit()