import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Variable declaration
wait = 5
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
first_name = "Elizabeth"
last_name = "Ezirim"
postal_code = "110241"

#Browser Initialization
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait)

#login details
UserName = driver.find_element(By.ID, "user-name")
UserName.send_keys(first_name)

passWord = driver.find_element(By.ID, "password")
passWord.send_keys(last_name)

loginButton = driver.find_element(By.ID, "login-button")
loginButton.click()
time.sleep(wait)

# Products

#add-to-cart-sauce-labs-backpack  item 1
backPack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack  item 1")
backPack.click()

#item 2  add-to-cart-sauce-labs-bike-light
bikeLight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
bikeLight.click()

#Item3 add-to-cart-sauce-labs-bolt-t-shirt
boltShirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
boltShirt.click()

#Item4 add-to-cart-sauce-labs-fleece-jacket
jacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #Scroll to bottom

#item 5 add-to-cart-sauce-labs-onesie
onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
onesie.click()

#item6 add-to-cart-test.allthethings()-t-shirt-(red)
tShirt = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
tShirt.click()

#cart_icon /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]
cartIcon= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]")
cartIcon.click()

#checkout checkout
checkOut = driver.find_element(By.ID, "checkout")
checkOut.click()

#checkout Information
#firstname first-name
#lastname last-name
#zipcode postal-code

#contnue button  continue

#customer information
firstName = driver.find_element(By.ID, "first-name")
firstName.send_keys(first_name)

lastName = driver.find_element(By.ID, "last-name")
lastName.send_keys(last_name)

postalCode = driver.find_element(By.ID, "postal-code")
postalCode.send_keys(postal_code)

continueButton = driver.find_element(By.ID, "continue")
continueButton.click()

#Checkout Overview finish
finishButton = driver.find_element(By.ID, "finish")
finishButton.click()

#hamburger react-burger-menu-btn
hamburgerIcon = driver.find_element(By.ID, "hamburger react-burger-menu-btn")
hamburgerIcon.click()


#logout logout_sidebar_link
logOut = driver.find_element(By.ID, "logout_sidebar_link")
logOut.click()





