from config import *

browser = webdriver.Chrome() # Launch browser
browser.implicitly_wait(5) # Standard wait for upload web objects

def login(username, password):
    link='https://www.instagram.com/'
    
    browser.get(link)

    # Here is the authorization and subscription to recommended accounts

    browser.find_element_by_css_selector('[name=username]').send_keys(username)
    browser.find_element_by_css_selector('[name=password]').send_keys(password)
    browser.find_element_by_css_selector('[type=submit]').click()

    browser.find_element_by_css_selector('[class="aOOlW   HoLwm "]').click()
    logging.info(u'Login success')

def follow_recommended(n=15):
    link_suggest='https://www.instagram.com/explore/people/suggested/'
    
    login(Username,Password)

    for i in range(hours):
        logging.info(u'Upload started')
        
        for i in range(n):
            browser.get(link_suggest)
            browser.find_element_by_css_selector('[class="sqdOP  L3NKy   y3zKF     "]').click() # Presses the button
            logging.info(u'Was add person in folowers')
        
        logging.info(u'Upload stopped for a hour')
        time.sleep(3600) # This is to exclude account blocking
    logging.info(u'Upload stopped')    

if __name__=='__main__':
    follow_recommended()