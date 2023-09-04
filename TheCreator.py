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
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import os
from dotenv import load_dotenv
from tiktok_uploader.upload import upload_video
from youtube_upload.client import YoutubeUploader
import tweepy
import json
import telegram
import logging

# Load environment variables from the .env file
load_dotenv()
# Access the environment variables
MAIL = os.getenv("EMAIL")
PSWD = os.getenv("PSW")
GML = os.getenv("GMAIL")
GPSWD = os.getenv("GMPSW")
XPSWD = os.getenv("XPSW")
TKTKPSWD = os.getenv("TKTKPSW")
TGTKN = os.getenv("TGTOKEN")
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
    print("entrato upvidtk")
    upload_video(path, title, headless=True, username='pastpeek',password=TKTKPSWD, cookies=os.getcwd()+"/cookies.txt")

async def upVid_X(path,title,desc):
    print("entrato upvidX")
    upUrl = 'https://twitter.com/i/flow/login'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--headless')
    chrome_options.binary_location = patzDriver
    browser = webdriver.Chrome(options=chrome_options)
    print("aperta pag X")
    browser.get(upUrl)
    time.sleep(5)
    
    browser.find_element(By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys(GML)
    time.sleep(2)
    print("metto la mail")
    nxt = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu']")))
    nxt.click()
    #input r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu
    time.sleep(1.5)
    uNameInp = browser.find_element(By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys('past_peek')
    print("metto l username")
    #div css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr
    time.sleep(0.5)
    nxt = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']")))
    nxt.click()
    # input r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu
    time.sleep(1.5)
    pswInp = browser.find_element(By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys(XPSWD)
    # div css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr
    time.sleep(0.5)
    print("metto la pass")
    nxt = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']")))
    nxt.click()
    time.sleep(5)
    upBtn = browser.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-xoduu5 r-xyw6el r-mk0yit r-13qz1uu']")
    upBtn.click()
    time.sleep(1)
    #div css-18t94o4 css-1dbjc4n r-1niwhzg r-42olwf r-sdzlij r-1phboty r-rs99b7 r-5vhgbc r-mvpalk r-htfu76 r-2yi16 r-1qi8awa r-1ny4l3l r-o7ynqc r-6416eg r-lrvibr
    upBtn = browser.find_element(By.XPATH, "//input[@class='r-8akbif r-orgf3d r-1udh08x r-u8s1d r-xjis5s r-1wyyakw']")
    """ hover = ActionChains(browser).move_to_element(upBtn)
    hover.perform()
    upBtn.click() """
    upBtn.send_keys(path)
    print("uppo file")
    time.sleep(1)
    #css-901oao r-1awozwy r-18jsvk2 r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0
    upBtn = browser.find_element(By.XPATH, "//div[@class='css-901oao r-1awozwy r-18jsvk2 r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")
    if upBtn.is_enabled():
        print("Ci sei ????")
        upBtn.click()
    #div css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr
    postBtn = WebDriverWait(browser, 300).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']")))
    postBtn.click()
    print("posto")
    time.sleep(1)
    """     browser.quit()
    time.sleep(1) """
    
    return


def upSnapchat(path,title,desc): #daje da fa 
    return

def upVidYT(path,title,desc):
    """ upUrl = 'https://studio.youtube.com/channel/UCeshQg3ojhYHHvmWvv-WWcQ'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = patzDriver
    browser = webdriver.Chrome(options=chrome_options)

    browser.get(upUrl)
    time.sleep(0.5)
    browser.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf']").send_keys(GML)
    #VfPpkd-vQzf8d
    nxt = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")))
    nxt.click()
    #input whsOnd zHQkBf
    time.sleep(1.5)
    pswInp = browser.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf']")
    pswInp.click()
    pswInp.send_keys('FabioSfabiolinscky')
    time.sleep(0.5)
    nxt = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")))
    nxt.click()
    time.sleep(600) """
    # cianno nculato gg w8ing for auth
    return

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
    print("start doShit")
    try:
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        prefs = {"download.default_directory" : pathzDownl}
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.binary_location = patzDriver
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(config.LOGINURL)
        email_input = browser.find_element(By.NAME, "email")
        email_input.send_keys(MAIL)
        print("ho messo l email")
        time.sleep(2)
        submit_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Continue with email')]")
        submit_button.click()
        time.sleep(2)
        isPorcodioError = False
        while(isPorcodioError == False):
            print("ha sbroccato la mail, riprovo")
            try:
                submit_buttonTest = browser.find_element(By.XPATH, "//button[contains(text(), 'Continue with email')]")
                if(submit_buttonTest):
                    submit_buttonTest.click()
            except:
                isPorcodioError = True
                break
            time.sleep(1.5)
        print("ha fatto la mail")
        time.sleep(10)
        try:
            code = getCode()
        except Exception as e:
            await botTg(None,"Error getting code: ", str(e))
        print("preso code ",code)
        code_input = browser.find_element(By.NAME, "code")
        code_input.send_keys(code)
        time.sleep(1)
        submit_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        submit_button.click()
        time.sleep(3)
        isPorcodioError = False
        tconunt = 0
        while(isPorcodioError == False):
            print("ha sbroccato il code, riprovo",tconunt)
            try:
                if(tconunt == 5):# @todo rifallo bene
                    print("rirpovo a pia rcode")
                    code = getCode()
                    print("new code ",code)
                    code_input = browser.find_element(By.NAME, "code")
                    code_input.clear()
                    code_input.send_keys(code)
                    time.sleep(1)
                submit_buttonTest = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
                if(submit_buttonTest):
                    submit_buttonTest.click()
                    tconunt += 1
                    
            except:
                isPorcodioError = True
                break
            time.sleep(1.5)
        print("ha fatto il code")
        time.sleep(5)
        #brief
        textInp = browser.find_element(By.NAME, "brief")
        testo = await ScriptGenerator(config.SITOSCRAPE).scrape_data()
        textInp.send_keys(testo)
        print('setto testo')
        time.sleep(2)
        try:
            gen_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(gen_button)
            hover.perform()
            gen_button.click()
            print("ho cliccato genera")
        except Exception as e:
            print("Error: ", e)
            await botTg(None,"Error generating video [gen_button]: "+str(e))
            return
        time.sleep(30)
        try:
            cont_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(cont_button)
            hover.perform()
            cont_button.click()
            print("ho cliccato continua")
        except Exception as e:
            print("Error: ", e)
            await botTg(None,"Error generating video [cont_button]: "+str(e))
            return

        try:
            time.sleep(1)
            title = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='c-bBzSYw c-famIYX c-haqLIS']"))) #browser.find_element(By.CLASS_NAME,'c-bBzSYw c-famIYX c-haqLIS').text.strip()
            ttitle = title.text.strip()
            print(ttitle, "titolo")
            with open('todaytitle.json', 'r') as file:
                data = json.load(file)
            data['title'] = ttitle
            with open('todaytitle.json', 'w') as file:
                json.dump(data, file, indent=4)
            exp_button = WebDriverWait(browser, 600).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn c-gFGbEn-idBRsyU-css']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(exp_button)
            hover.perform()
            exp_button.click()
            print("ho cliccato export")
            #c-eUfrSE c-eUfrSE-ibydIAZ-css
            exp_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='c-eUfrSE c-eUfrSE-ibydIAZ-css']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(exp_button)
            hover.perform()
            exp_button.click()
            print("ho ricliccato export")
        except Exception as e:
            print("Error: ", e)
            await botTg(None,"Error generating video [exp_button]: "+str(e))
            return
        time.sleep(1)
        try:
            if(FREE):
                print("metto a robba pe i poveri")
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
            print("Continua [watermark etc section]")
            contin_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-gFGbEn c-gFGbEn-igHSfTu-css']")))#browser.find_element(By.XPATH, "//button[@type='submit']")
            hover = ActionChains(browser).move_to_element(contin_button)
            hover.perform()
            contin_button.click()
            print("aspetto rendering e download")
            time.sleep(10)
        except Exception as e:
            print("Error: ", e)
            await botTg(None,"Error generating video [contin_button]: "+str(e))
            return
        time.sleep(120)
        print("sto pe quitta ciao")
        time.sleep(1)
        lstVid = getLastVid()
        #os.rename(lstVid, title.text.strip())
        #await upVid_X(browser,lstVid,title.text.strip(),"willBeADesc")
    # -------------------------------- TWITTER ---------------------------------
        """upUrl = 'https://twitter.com/i/flow/login'
        
        print("sbrocco no se vede")
        browser.get(upUrl)
        time.sleep(5)
        
        browser.find_element(By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys(GML)
        time.sleep(2)
        nxt = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu']")))
        nxt.click()
        #input r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu
        time.sleep(1.5)
        uNameInp = browser.find_element(By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys('past_peek')
        #div css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr
        time.sleep(0.5)
        nxt = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']")))
        nxt.click()
        # input r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu
        time.sleep(1.5)
        pswInp = browser.find_element(By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys(XPSWD)
        # div css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr
        time.sleep(0.5)
        nxt = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr']")))
        nxt.click()
        time.sleep(5)
        upBtn = browser.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-xoduu5 r-xyw6el r-mk0yit r-13qz1uu']")
        upBtn.click()
        time.sleep(1)
        #div css-18t94o4 css-1dbjc4n r-1niwhzg r-42olwf r-sdzlij r-1phboty r-rs99b7 r-5vhgbc r-mvpalk r-htfu76 r-2yi16 r-1qi8awa r-1ny4l3l r-o7ynqc r-6416eg r-lrvibr
        upBtn = browser.find_element(By.XPATH, "//input[@class='r-8akbif r-orgf3d r-1udh08x r-u8s1d r-xjis5s r-1wyyakw']")


        upBtn.send_keys(lstVid)
        time.sleep(1)
        #css-901oao r-1awozwy r-18jsvk2 r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0
        upBtn = browser.find_element(By.XPATH, "//div[@class='css-901oao r-1awozwy r-18jsvk2 r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")
        upBtn.click()
        #div css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr
        postBtn = WebDriverWait(browser, 300).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']")))
        postBtn.click()
        time.sleep(1)
        browser.quit()
        time.sleep(10) """
    #---------------------------------------------------------------------------
        #upVid_tktk(lstVid,title.text.strip())
        print("porcodio prima di bottg", lstVid)
        #await botTg(lstVid,f"No nevvero, ecco il video di oggi o/ -Title- `{title.text.strip()}` - ") 
        print("porcodio dopo di bottgasdijnoakjsndkjaonsd  RETURN")
        return 
        """ lstVid = getLastVid()
        print("lstVid ",lstVid)
        if(lstVid is not None):
            await upShit(lstVid,title.text.strip())
        time.sleep(900) """
    except Exception as e:
        print("Error: ", e)
        await botTg(None,"Error generating video [main]: "+str(e))
        return


async def botTg(path,msg):
    application = telegram.Bot(TGTKN)
    chat_id = '-973874521'
    if path:
        document = open(path, 'rb')
        async with application:
            await application.send_document(chat_id, document)
    if msg:
        async with application:
            await application.send_message(chat_id=chat_id, text="Bro! there was an error! diohane:\n"+msg)

async def upShit(lstVid,title):

    #await botTg(lstVid,f"No nevvero, ecco il video di oggi o/ - {title} - ") 
    print("uppo su X")
    await upVid_X(lstVid,title,"willBeADesc")
    time.sleep(10)
    print("uppo su TikTOk")
    upVid_tktk(lstVid,title)
""" 
async def mainShit():
    titl = await doShit()
    time.sleep(1)
    if titl:
        lstVid = getLastVid()
        await upShit(lstVid,titl)
    else:
        print("PORCODIO") """
""" def porcodio():
    try:
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        prefs = {"download.default_directory" : pathzDownl}
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.binary_location = patzDriver
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(config.LOGINURL)
        time.sleep(3)
        wait = WebDriverWait(browser, 10)  # Adjust the timeout as needed
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        element.send_keys(Keys.CONTROL + 't')
        upUrl = 'https://twitter.com/i/flow/login'
        print("sbrocco no se vede")
        browser.get(upUrl)
        time.sleep(10)
    except WebDriverException as e:
        print("Error: ", e)
        return 
porcodio()"""

#asyncio.run(doShit())
import sys

# Check if the script has at least one argument
if len(sys.argv) < 2:
    print("Usage: python script.py <argument>")
    sys.exit(1)  # Exit the script with an error code

# Access the first argument (without the script name)
arg1 = sys.argv[1]
if arg1 == "-u" or arg1 == "--upload":
    lstVid = getLastVid()
    """     file_name_without_extension = os.path.splitext(os.path.basename(lstVid))[0]
    print("lstVid title: ",file_name_without_extension)#sistemanome """
    with open('todaytitle.json', 'r') as file:
        data = json.load(file)
    ttl = data['title']
    asyncio.run(upShit(lstVid,ttl))
elif arg1 == "-c" or arg1 == "--create":
    asyncio.run(doShit())
else:
    print(f"Received argument: {arg1}")


