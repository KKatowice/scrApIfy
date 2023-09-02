from selenium import webdriver
import time
import imaplib
import config
import email
from selenium.webdriver.common.by import By
import time as t
import re
import glob
from TheScrapeGenerator import ScriptGenerator
import asyncio
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
from dotenv import load_dotenv
from tiktok_uploader.upload import upload_video
from youtube_upload.client import YoutubeUploader
# Load environment variables from the .env file
load_dotenv()
# Access the environment variables
MAIL = os.getenv("EMAIL")
PSWD = os.getenv("PSW")
FREE = True
patzDriver = "/usr/bin/chromium-browser"
pathzDownl = "/home/katowice/Downloads/testVideos"

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

def upVid_tktk(path,title):
    upload_video(path, title, headless=True, username='pastpeek',password='Ertracer1!', cookies=os.getcwd()+"/cookies.txt")

def upVid_X():
#nop..selenium..MESA MANCO.......DIOCANE
    return

def upoVid_yt(path,title):
    uploader = YoutubeUploader()
    uploader.authenticate()

    # Video options
    options = {
        "title" : title, # The video title
        "description" : "Test description", # The video description da vede
        "tags" : [""],
        "categoryId" : "42",
        "privacyStatus" : "private", # Video privacy. Can either be "public", "private", or "unlisted"
        "kids" : False, # Specifies if the Video if for kids or not. Defaults to False.
        "thumbnailLink" : "" # Optional. Specifies video thumbnail.
    }

    # upload video
    uploader.upload(path, options) 

def getLastVid():
    files = glob.glob(os.path.join(pathzDownl, '*'))
    newest_file = max(files, key=os.path.getctime, default=None)
    if newest_file is not None:
        fName = os.path.basename(newest_file)
        print(f"The newest file in the folder is: {fName}")
        print(f"path : {pathzDownl}/{fName}")
        return f"{pathzDownl}/{fName}"
    else:
        print("The folder is empty or contains only subdirectories.")
        return None

async def doShit():
    try:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : pathzDownl}
        chrome_options.add_experimental_option("prefs",prefs)
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
        time.sleep(10)
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
        time.sleep(30)
        try:
            cont_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(cont_button)
            hover.perform()
            cont_button.click()
        except Exception as e:
            print("Error: ", e)
        
        try:
            exp_button = WebDriverWait(browser, 600).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn c-gFGbEn-idBRsyU-css']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(exp_button)
            hover.perform()
            exp_button.click()
            #c-eUfrSE c-eUfrSE-ibydIAZ-css
            exp_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='c-eUfrSE c-eUfrSE-ibydIAZ-css']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(exp_button)
            hover.perform()
            exp_button.click()
        except Exception as e:
            print("Error: ", e)
        time.sleep(1)
        try:
            if(FREE):
                wtMarks_buttonTest = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Stock watermarks')]")))
                hover = ActionChains(browser).move_to_element(wtMarks_buttonTest)
                hover.perform()
                wtMarks_buttonTest.click()
                print(wtMarks_buttonTest)
                time.sleep(0.5)
                wtMarks_buttonTest = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Normal')]")))
                hover = ActionChains(browser).move_to_element(wtMarks_buttonTest)
                hover.perform()
                wtMarks_buttonTest.click()
            #c-gFGbEn c-gFGbEn-igHSfTu-css
            contin_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn c-gFGbEn-igHSfTu-css']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(contin_button)
            hover.perform()
            contin_button.click()

        except Exception as e:
            print("Error: ", e)
        
        time.sleep(300)
        lstVid = getLastVid()
        print("lstVid ",lstVid)
        if(lstVid is not None):
            upVid_tktk(lstVid,"Test upload 2")
            upoVid_yt(lstVid,"Test upload 2")
        time.sleep(900)
    except Exception as e:
        print("Error: ", e)

asyncio.run(doShit())
#getLastVid()

