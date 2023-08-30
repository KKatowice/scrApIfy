from selenium import webdriver
import time
import imaplib
import config
import email
from selenium.webdriver.common.by import By
import time as t
import re
from TheScrapeGenerator import ScriptGenerator
import asyncio
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()
# Access the environment variables
MAIL = os.getenv("EMAIL")
PSWD = os.getenv("PSW")

patzDriver = "/usr/bin/chromium-browser"

def getCode():
    sessionz = imaplib.IMAP4_SSL(config.imap_server,config.imap_port)
    
    sessionz.login(MAIL,PSWD)
    time.sleep(1)
    sessionz.select("Inbox")
    (result, blocks) = sessionz.search(None, 'UNSEEN')
    lastMsg = None
    try:
        for messages in blocks:
            msgList = messages.split()
            lastMsg = msgList[0]
            break
    except Exception as e:
        print("No new emails", e)
        return None
    porcodio = lastMsg.decode()
    niente, ids = sessionz.fetch(str(porcodio) , "(RFC822)")
    raw = email.message_from_bytes(ids[0][1])
    finalCode = None
    for part in raw.walk():
        
        if('text/plain' in part.get_content_type()):
            code = part.get_payload()
            match = re.search(r'\b\d{6}\b', str(code))
            if match:
                finalCode = match.group()
                print("Found number")
            else:
                print("No number found in the string.")
            break
    return finalCode

    
async def doShit():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = patzDriver
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(config.LOGINURL)
        email_input = browser.find_element(By.NAME, "email")
        email_input.send_keys(MAIL)
        time.sleep(2)
        submit_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Continue with email')]")
        submit_button.click()
        time.sleep(2)
        isPorcodioError = False
        while(isPorcodioError == False):
            try:
                submit_buttonTest = browser.find_element(By.XPATH, "//button[contains(text(), 'Continue with email')]")
                if(submit_buttonTest):
                    submit_buttonTest.click()
            except:
                isPorcodioError = True
                break
            time.sleep(1.5)
        time.sleep(7)
        code = getCode()
        print("code",code)
        code_input = browser.find_element(By.NAME, "code")
        code_input.send_keys(code)
        time.sleep(1)
        submit_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        submit_button.click()
        time.sleep(3)
        isPorcodioError = False
        while(isPorcodioError == False):
            try:
                submit_buttonTest = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
                if(submit_buttonTest):
                    submit_buttonTest.click()
            except:
                isPorcodioError = True
                break
            time.sleep(1.5)
       
        time.sleep(5)
        #brief
        textInp = browser.find_element(By.NAME, "brief")
        testo = await ScriptGenerator(config.SITOSCRAPE).scrape_data()
        textInp.send_keys(testo)
        time.sleep(2)
        try:
            gen_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(gen_button)
            hover.perform()
            gen_button.click()
        except Exception as e:
            print("Error: ", e)
            #c-gFGbEn
        time.sleep(60)
        try:
            gen_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(gen_button)
            hover.perform()
            gen_button.click()
        except Exception as e:
            print("Error: ", e)


        
        time.sleep(900)
    except Exception as e:
        print("Error: ", e)

asyncio.run(doShit())


