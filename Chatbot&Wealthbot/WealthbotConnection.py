import requests
import numpy as np

def login(email, password):
    response = requests.request("get", url="http://127.0.0.1:8000/login")
    cookies = response.cookies
    #print(cookies)
    url = "http://127.0.0.1:8000/login"
    headers = {
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'Accept-Encoding': "gzip, deflate, br",
            'Accept-Language': "zh-CN,zh;q=0.9",
            'Cache-Control': "max-age=0",
            'Connection': "keep-alive",
            # 'Content-Length': "145",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': 'csrftoken=r6k0UuCG6gv1rAfWWnxBrZgovkokl7dyHnTVNRnEgvRsV9c8nWPou3tQVbpNz6bo',
            'Host': '127.0.0.1:8000',
            'Origin': 'http://127.0.0.1:8000',
            'Referer': 'http://127.0.0.1:8000/login',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            }
    data = {
            'csrfmiddlewaretoken': cookies['csrftoken'],
            'username': email,
            'password': password,
            '_submit': 'Login'
            }
    response = requests.request('post', url='http://127.0.0.1:8000/login', data=data, cookies=cookies)
    return response

def register(name):
    namelist = []
    namelist = np.load('namelist.npy')
    e_name = namelist[0]
    namelist = np.delete(namelist, [0])
    np.save('namelist', namelist)
    ##############
    response = requests.request("get", url="http://127.0.0.1:8000/client/registration/5")
    #print(response.headers)
    cookie = response.cookies
    url = "http://127.0.0.1:8000/client/registration/5"
    data = {
            'csrfmiddlewaretoken':cookie['csrftoken'],
            'first_name': name,
            'last_name': 'Kang',
            'email': e_name,
            'password1': '12q12q12q',
            'password2': '12q12q12q',
            'is_accepted': '1',
            'submit':'Register'
            }
    headers = {'Cookie':response.headers['Set-Cookie']}
    
    response = requests.request("post", url, data=data,headers=headers)
    return response.cookies

def step1(cookies, name):
    #parameter:
    #first_name, last_name, birth_date, marital_status, annual_income, income_tax, liquid_net_worth, employment_type, spouse_first_name = None,
    #spouse_last_name = None, spouse_birth_date = None, street = 1, city = 1, phone = 1
    url = "http://127.0.0.1:8000/client/profile/step-one"
    # cookies = register.register()
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cache-Control': "max-age=0",
        'Connection': "keep-alive",
        #'Content-Length': "529",
        'Content-Type': "application/x-www-form-urlencoded",
        ##cookies 从login里的cookies获取
        #'Cookie': 'csrftoken=6blNbvZ8DKZgfoC3tX1vdwq7ZxVIATW9UtCEjKrXLuE0ovpXYGa0ls7Oa7yyE24u; sessionid=rlev9oe4j8kcrli5l7bqlyz4ib6bjelc',
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-one',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data={
        ##cookies 从login里的cookies获取
        'csrfmiddlewaretoken': cookies['csrftoken'],
        'client-first_name': name,
        'client-last_name': 'Kang',
        'client-birth_date': '09-09-1999',
        'client-marital_status': 'Single',
        'spouse-first_name':'ll',
        'spouse-last_name':'ll',
        'spouse-birth_date':'ll',
        'client-street': 'll',
        'client-city': '1111111111111',
        'client-mailing_street':'ll',
        'client-mailing_city':'ll',
        'client-phone_number': '(111) 111 - 1111',
        'client-annual_income': '$0-$50,000',
        'client-estimated_income_tax': '0.2',
        'client-liquid_net_worth': '$0-$25,000',
        'client-employment_type': 'Employed',
        'Continue': 'Continue'
    }
    #print(cookies['csrftoken'])
    response = requests.request("post", url, data=data, cookies=cookies)

    return response.cookies

def step2(cookies):
    url='http://127.0.0.1:8000/client/profile/step-two'
    # cookies=step1.step1()
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cache-Control': "max-age=0",
        'Connection': "keep-alive",
        'Content-Length': "153",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cookie': 'csrftoken=hQHQvKvELKsxU9blhIvJJiRsJu0RgJE7loiJsvtt1XtKfwkLxWCDkyefx0UNgxw5; sessionid=rlev9oe4j8kcrli5l7bqlyz4ib6bjelc',
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-two',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data={
        'csrfmiddlewaretoken':cookies['csrftoken'],
            'answer_11': '30',
    'answer_10': '27',
    'answer_9': '23',
    'answer_12': '32',
    'Continue': 'Continue',
    }
    response = requests.request("post", url, data=data,cookies=cookies)
    #print(response.text)
    #print(response.cookies)
    return response.cookies

def step3(cookies):
    url='http://127.0.0.1:8000/client/profile/step-three'
    cookies=step2.step2()
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cache-Control': "max-age=0",
        'Connection': "keep-alive",
        #'Content-Length': "529",
        'Content-Type': "application/x-www-form-urlencoded",
        ##cookies 从login里的cookies获取
        'Cookie': 'csrftoken=SIWszHfob6Ca337Nk1APMvHPWXOK442NQnwj2dGnAlaXOMm3YhgDKiabtKDOhhgP; sessionid=06wsmrjym7nk6fa1ibiqnhcncbqd45ci',
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-one',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data={
        'csrfmiddlewaretoken':cookies['csrftoken'],
        'client_account_types-groups': 'deposit_money'
    }
    response = requests.request("post", url, data=data,cookies=cookies)
    #print(response.text)
    #print(response.cookies)
    return response.cookies
#step3()

def step3_1(cookies):
    url='http://127.0.0.1:8000/client/profile/show-deposit-account-form'
    cookies = step3()
    headers={
        'Cookie': 'csrftoken='+cookies['csrftoken']+'; '+'sessionid='+cookies['sessionid'],
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-two',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data={
        'csrfmiddlewaretoken':cookies['csrftoken'],
        'client_account_types-group_type': 'Personal Account',
            'client_account_types-groups': 'deposit_money'
    }
    response = requests.request("post", url, data=data, cookies=cookies,headers=headers)
    #print(response.text)
    #print(response.cookies)
    return response.cookies
#step3_1()

def step3_2(cookies):
    url='http://127.0.0.1:8000/client/profile/update-account-form/deposit_money'
    cookies=step3_1()
    headers={
        'Cookie': 'csrftoken='+cookies['csrftoken']+'; '+'sessionid='+cookies['sessionid'],
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-three',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data={
        'csrfmiddlewaretoken': cookies['csrftoken'],
        #'value': '1,111,111.00',
        'contribution_type': 'neither'
    }
    response = requests.request("post", url, data=data, headers=headers)
    #print(response.text)
    #print(response.cookies)
    return cookies
#step3_2()

def step3_3(cookies):
    url = 'http://127.0.0.1:8000/client/profile/create-account/deposit_money'
    cookies = step3_2()
    headers = {
        'Cookie': 'csrftoken=' + cookies['csrftoken'] + '; ' + 'sessionid=' + cookies['sessionid'],
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-three',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'csrfmiddlewaretoken': cookies['csrftoken'],
        'value': '1,111,111.00',
    }
    response = requests.request("post", url, data=data, headers=headers)
    #print(response.text)
    #print(response.cookies)
    return cookies


