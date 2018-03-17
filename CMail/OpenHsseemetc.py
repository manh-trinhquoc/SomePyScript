'''
Created on Dec 1, 2017
CMail.py - Automatic open e-mail. Check folder for new email and follow link
@author: manh.trinhquoc
'''
import re  # search for class pattern
import time  # sleep
import logging  # logging error
import sys  # quit program when error
from selenium import webdriver  # open Chrome
from selenium.webdriver.common.keys import Keys  # Keyboard


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of code')
error_code = None;
state_machine = 0
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://gmail.com')

def input_text (css_selector='', str_keys='', webdriver_controller=None):
    eles = webdriver_controller.find_elements_by_css_selector(css_selector)
    if len(eles) == 0:
        logging.error('webdriver cannot find element <{}>'.format(css_selector))
        return 1
    if len(eles) != 1:
        logging.warning('webdriver find more than 1 element <{}>'.format(css_selector))
        input('Warning 1: There are changes in website structure. Press any key to continue')
    for each in eles:
        try:
            each.send_keys(str_keys)
        except:
            pass
def button_click(css_selector='', webdriver_controller=None):
    eles = driver.find_elements_by_css_selector(css_selector)
    if len(eles) == 0:
        logging.error('webdriver cannot find element <{}>'.format(css_selector))
        return 1
    if len(eles) != 1:
        logging.warning('webdriver find more than 1 element <{}>'.format(css_selector))
        print('Warning 1: There are changes in website structure. Press any key to continue')
    for each in eles:
        try:
            each.click()
        except:
            pass
def is_right_label(target_label = '', current_url = ''):
    # when signed-in successfully, check if we in the right label
    split_url = current_url.split('/')
    current_label =''
    for i in range(len(split_url)):
        if re.search('#',split_url[i]):
            current_label = '/'.join(split_url[i:])
            break
    if target_label == current_label:
        return True
    else:
        return False

state_machine = 1  # signing-in state
while True:
    if state_machine != 1:
        break
    logging.info('state_machine = 1: signing-in state')
    error_code = input_text('input[id="identifierId"]', 'hsseemetc', driver)  # email input box
    time.sleep(1)
    error_code = button_click('div[id="identifierNext"][role="button"]', driver)  # Next button
    time.sleep(5)
    error_code = input_text('input[name="password"]','', driver)  # password input text box
    time.sleep(1)
    error_code = button_click('div[id="passwordNext"][role="button"]', driver)  # Next button
    time.sleep(20)
    while True:  # manually sign-in
        current_url = driver.current_url
        result = is_right_label('#inbox',current_url)
        if result:
            state_machine = 2
            logging.info('go to state_machine = 2')
            break
        else:
            logging.error('Error 2: Sign-in fail due to unknown error')
            input('Error 2: Sign-in fail due to unknown error. Please sing-in to #inbox manually then press any key to continue')

while True:
    '''state_machine == 2: sign-in successfully, false label
    get target label in the database
    if there is no more label quit
    go to label
    go to state 3: right label
    '''
    if state_machine != 2:
        break
    logging.info('state_machine = 2: sign-in success.inbox or wrong label')
    '''target_label = 'C27'
    #  css_path = 'div[class="aim"] a[title="{}"]'.format(target_label)  # tag C27 #obsolet method '''
    target_label = '#label/C27'
    css_path = 'a[href="https://mail.google.com/mail/u/0/{}"]'.format(target_label)
    button_click(css_path,driver)
    time.sleep(10)
    while True:  # manually go to label
        current_url = driver.current_url
        result = is_right_label(target_label,current_url)
        if result:
            state_machine = 3
            logging.info('go to state_machine = 3')
            break
        else:
            logging.error('Error 3: Get to label fail due to unknown error')
            input('Error 3: Get to label fail due to unknown error. Please get to label {} manually then press any key to continue'.format(target_label))

while True:  # state_machine == 3: right label
    if state_machine != 3:
        break
    logging.info('state_machine =3: get in right label')
    '''mail in inbox table[id=":2d"]>tbody>tr
    read email: tr[class="zA yO"]
    un-read email: tr[class="zA zE"]
    un-read mouse hovering email: tr[class="zA zE aqw"]
    '''
    '''label contain un-read mail: 
    find tag: a[href="..."]. 
    tag.title contain (1) or (2) for 1 or 2 un-read mail
    get in mail[0] un-read
    '''
    # check label if there are un-read emails
    target_label = '#label/C27'
    css_path = 'a[href="https://mail.google.com/mail/u/0/{}"]'.format(target_label)
    ele = driver.find_element_by_css_selector(css_path)
    title = ele.get_attribute('title')
    if re.search('\([1-9]+\)',title):
        # if there is. Go to state 4: inside first mail content
        css_path='div[role="main"] table[class="F cf zt"] tbody tr'
        button_click(css_path, driver)
        time.sleep(10)
        state_machine = 4
        logging.info('go to state machine = 4')
    else:
        # if there is not. Exit()
        logging.info('exit at state_machine = 3, check there is no new email in label')
        driver.quit()
        sys.exit()

while True:
    ''' state 4: inside email:
    go to link in email content
    when come back from link. check if there are un-read emails.
    if there is not. go to state 2: wrong label
    if there is. click button older mail'''
    if state_machine != 4:
        break
    logging.info('state_machine =4: get in mail content')
    # TODO: goto link
    # check if there is another un-read mails
    # TODO: refactor check un-read mails
    target_label = '#label/C27'
    css_path = 'a[href="https://mail.google.com/mail/u/0/{}"]'.format(target_label)
    ele = driver.find_element_by_css_selector(css_path)
    title = ele.get_attribute('title')
    if re.search('\([1-9]+\)',title):
        # if there is. go to next mail
        css_path='div[class="iG J-J5-Ji"] div[role="button"][aria-label="Older"]'
        button_click(css_path, driver)
        time.sleep(10)
    else:
        # if there is not. Exit()
        logging.info('exit at state machine = 4. There is no more un-read email')
        driver.quit()
        sys.exit()
# TODO: Create a list of label and walk through all
