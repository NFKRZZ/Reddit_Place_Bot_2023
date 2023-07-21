import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def reddit_login(username, password):

    driver = webdriver.Chrome(executable_path='./chromedriver')

    login_url = 'https://www.reddit.com/login'
    driver.get(login_url)

    # Find the username and password input fields and fill them with the provided credentials
    username_field = driver.find_element_by_name('username')
    password_field = driver.find_element_by_name('password')

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for a short period to allow the page to load
    time.sleep(5)

    
    driver.get('https://reddit.com/r/place/?screenmode=fullscreen')
    print("HELLO\n")
    time.sleep(10)
    print("MO\n")
    try:
        #extras = driver.find_element_by_class_name('icon icon-close')
        extras = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div/div[2]/button")
        extras.click()    
    except:
        print("Element with class name 'icon icon-close' not found.")


    time.sleep(5)

    print("OK CLICK BUTTON NOW")

    driver.get('https://reddit.com/r/place/?screenmode=fullscreen&cx=-317&cy=-148&px=38')
    time.sleep(10)
    try:
        #but = driver.find_element_by_xpath("/html/body/garlic-bread-app/faceplate-alert-reporter/garlic-bread-embed//div/garlic-bread-share-container/div[4]/garlic-bread-status-pill//button")
        #but = driver.find_elements_by_css_selector("div.bottom-controls button")

        #iframe_element = driver.find_element(By.CLASS_NAME,'_3Sf9ucwF90vy8KQgnmYHkY')
        #driver.switch_to.frame(iframe_element)
        but = driver.find_elements(By.CLASS_NAME,"bottom-controls")
        print("OOGA")
        element = driver.find_element(By.TAG_NAME, 'garlic-bread-status-pill')

       # but = driver.find_element(By.CLASS_NAME,'_3Sf9ucwF90vy8KQgnmYHkY')
        print("Found it 1\n")
        element = driver.find_element(By.XPATH, '//garlic-bread-status-pill')

       # but = driver.find_elements(By.CLASS_NAME,'theme-beta theme-light')
        print("Found it 2\n")
       # but = driver.find_elements(By.CLASS_NAME,'bottom-controls')

        
        print("FOUND PILL\n")
        #but.click()
    except:
        print("Couldnt find big red button")
    
    time.sleep(10)
    
    

    

def main():
    # Replace 'YOUR_REDDIT_USERNAME' and 'YOUR_REDDIT_PASSWORD' with your login credentials
    username = ''
    password = ''

    session = reddit_login(username, password)
    print(session)
  

if __name__ == "__main__":
    main()
