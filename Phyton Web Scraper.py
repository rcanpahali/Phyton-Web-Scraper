import requests
from bs4 import BeautifulSoup

#print(token)
#print(headers)
##r = requests.post(url = url, params = PARAMS)

proxies = { 
  "http"  : "http://10.10.1.10:3128", 
  "https" : "https://10.10.1.11:1080", 
  "ftp"   : "ftp://10.10.1.10:3128"
}

loginUrl = 'https://mt2classic.com/login' 
marketUrl = 'https://mt2classic.com/shop/browse'
voteUrl = 'https://mt2classic.com/shop/vote/0'
voteSubmitUrl = 'https://www.metin2pserver.info/vote-Mt2Class.htm'
redeemUrl = 'https://mt2classic.com/shop/vote/redeem/0'

with requests.Session() as session:
    
    #session.proxies.update(proxies)
        
    r = session.get(loginUrl)
    loginPage = BeautifulSoup(r.content, 'html5lib')
    
    tokenInput = loginPage.find('input', attrs = {'name':'_token'})
    
    loginCredentials = {
    "_token": tokenInput['value'],
    "login": "*",
    "password": "*"
    }

    loginHeader = {
        "Cache-Control":"max-age=0",
        "Origin":"https://mt2classic.com",
        "Referer": "https://mt2classic.com/shop/browse",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-User":"?1",
        "Sec-Fetch-Dest":"document",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"tr-TR,tr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"
    } 
    
    ##Login Page
    loginRequest = session.post(loginUrl, headers=loginHeader, data=loginCredentials)
    
    ##Vote Page   
    r = session.get(voteUrl)
    votePage = BeautifulSoup(r.content, 'html5lib')
    
    formData_s = votePage.find('input', attrs = {'name':'s'})
    formData_id = votePage.find('input', attrs = {'name':'id'})
    formData_param_user = votePage.find('input', attrs = {'name':'param_user'})
    
    voteFormData = {
        "s": formData_s['value'],
        "id": formData_id['value'],
        "param_user": formData_param_user['value']
    }
    
    voteHeader = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"          
        }        

    #CAPTCHA Page
    voteRequest = session.post(voteSubmitUrl, headers=voteHeader, data=voteFormData)
    
  
    #Collect Points Page    
    redeemHeader = {
        "Origin":"https://mt2classic.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
  }
        
    r = session.get(redeemUrl, headers = redeemHeader)
    redeemPage = BeautifulSoup(r.content, 'html5lib')  
    
    redeemPageResult = redeemPage.find('div', attrs = {'class':'p-2 mt-4 bg-fog-gradient rounded-lg max-w-sm mx-auto'})
    print(redeemPageResult.prettify())

