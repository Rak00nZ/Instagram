from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from selenium.common.exceptions import NoSuchElementException
import pickle



def clear():                
    os.system("cls")
    return  # Creates a clear function for ease of use
def login():
    browser.get("https://www.instagram.com/accounts/login")
    clear()
    inputs =  browser.find_elements_by_xpath('//input[@class="_2hvTZ pexuQ zyHYP"]')
    ActionChains(browser)\
     .move_to_element(inputs[0]).click()\
     .send_keys(str(username))\
     .move_to_element(inputs[1]).click()\
     .send_keys(str(password))\
     .send_keys(Keys.TAB*2)\
     .send_keys(Keys.ENTER)\
     .perform()
   # try:
    sleep(1)
    browser.get('https://www.instagram.com/')

    try:
        sendCodeElem = browser.find_element_by_xpath('(//button)[2]') #send code button
        ActionChains(browser)\
            .move_to_element(sendCodeElem).click()\
            .perform()
        code = input('Type in 2 factor authentication code or send n if no code is required     ')
        if  len(code) == 6:
            factorElem = browser.find_element_by_xpath('//input[@class="_281Ls zyHYP"]')
            ActionChains(browser)\
                .move_to_element(factorElem).click()\
                .send_keys(str(code)+Keys.TAB+Keys.ENTER)\
                .perform()
    except:
        pass
    sleep(1)  #logs into instagram //////////// working, buggy
def myFollowers():
    FollowerList = []   
    browser.get('https://www.instagram.com/'+ (username))
    myFollowerElem = browser.find_element_by_xpath('(//li/a/span)[1]')  #the button on your page that says your follower count
    followerCount = myFollowerElem.text #reads your follower count
    followerCount = (int(followerCount.replace(',','')) -1)
    myFollowerElem.click() #navigates to your followers list
    sleep(1)
    followerPanel = browser.find_element_by_xpath('// div[@class="j6cq2"]') # follower panel for scroll
    x = 1
    test = 0
    while (x < followerCount):
        try:
            myFollowersUsernameElem = browser.find_element_by_xpath('(// a[@class="FPmhX notranslate _0imsa "])['+str(x)+']')
            FollowerList.append(myFollowersUsernameElem.text)    #reads follower's username and adds to list
            x = x + 1
        except(NoSuchElementException):
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",followerPanel) #scrolls
            sleep(1)
    print(FollowerList)
    return(FollowerList)   #makes a list of your follower's usernames //////////////////WORKING


def follow(person): # function that follows a single user
    try:
        browser.get('https://www.instagram.com/'+str(person))
        sleep(1)    
    
        followButton = browser.find_element_by_xpath('//button[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]') #clicks the follow button 
        followButton.click()
    except:
        pass
    return  # function that follows a single user  \\\\\\\\\\\\\\ NOT FULLY TESTED


def followers(user):
    try:
        theirFollowerList = []   
        browser.get('https://www.instagram.com/'+ (user))
        theirFollowerElem = browser.find_element_by_xpath('(//li/a/span)[1]')  #the button on their page that says their follower count
        theirFollowerCount = theirFollowerElem.text #reads their follower count
        theirFollowerCount = (int(theirFollowerCount.replace(',','')) -1)
        theirFollowerElem.click() #navigates to your followers list
        sleep(1)
        theirFollowerPanel = browser.find_element_by_xpath('// div[@class="j6cq2"]') # follower panel for scroll
        x = 1
        while (x < theirFollowerCount):
            try:
                theirFollowersUsernameElem = browser.find_element_by_xpath('(// a[@class="FPmhX notranslate _0imsa "])['+str(x)+']')
                theirFollowerList.append(theirFollowersUsernameElem.text)    #reads follower's username and adds to list
                clear()
                print(x)
                x = x + 1
            except(NoSuchElementException):
                browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",theirFollowerPanel) #scrolls
                sleep(2)
        return(theirFollowerList)   #makes a list of your follower's usernames ////////////////// incomplete delay needs to be added
    except:
        return
fullFollower = []   # full list of all of my follower's followers (with duplicates)
noDuplicate = []    # full list of all the people that are followed by more than one of my followers
myFollowerList = []
username = str(input("Input Instagram username     "))         #Instagram Username
password = str(input("Input Instagram password     "))         #instagram password
chromeDriver = './chromedriver'
browser = webdriver.Chrome(chromeDriver)
clear()
login()
myFollowerList = []
myFollowerList = list(myFollowers())
x = ''
for x in myFollowerList:
    fullFollower.append(followers(x))
browser.quit()
clear()
FFlength = len(fullFollower)

print(FFlength)

l = [1,2,3,4]
with open("list.txt", "wb") as fp:   #Pickling
  pickle.dump(fullFollower, fp)
