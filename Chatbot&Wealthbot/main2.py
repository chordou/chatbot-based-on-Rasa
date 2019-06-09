import requests
import numpy as np
from bs4 import BeautifulSoup

'''
问题的选项
annual_income：

'$0-$50,000'
 '$50,001-$75,000'
 '$75,001-$100,000'
 '$100,001-$150,000'
'$150,001-$250,000'
'$250,001 +'


income_tax：0-100

 '$0-$25,000'
 '$25,001-$50,000'
 '$50,001-$100,000'
 '$100,001-$200,000'
 '$200,001-$350,000'
 '$350,001-$700,000'
 '$700,001-$1,000,000'
 '$1,000,000 +'

Employment Status：

'Employed'
'Self-Employed'
'Retired'
'Unemployed'


Choose the statement that best reflects your thoughts about reaching your financial goal:
30 interested in steady returns if i accept lowewr returns
31 interestesd in maximizing long term gains, even if i experience short term losses
（30，31是需要传给wealthbot的答案，后面是他们对应的选项，下面的27，28，29也一样）
Which set of hypothetical portfolio returns in a year is most acceptable to you?
27 +-15
28 +-10
29 +-5
The global stock market is often volatile. If your entire investment portfolio lost 10% of its value in a month during a market decline, what would you do?
23 sell all of your investments
24 sell some
25 keep all 
26 buy more
Will you need up to ¼ of your portfolio within the next 10 years for a large expense (house, college, etc.)?
32 yes 
33 no

'''
def main(annual_income, income_tax, liquid_net_worth, employment_type,
         financial_goal, expected_returns,would, need,#这行是step2的四个问题，答案是数字，选项和答案对应看上面
         acount_money='1,111,111.00'):
    ###################register####################
    """
    namelist = []
    namelist = np.load('namelist.npy')
    name = namelist[0]
    print(name)
    namelist = np.delete(namelist, [0])
    # print(namelist)
    np.save('namelist', namelist)
    """

    em=str(str(np.random.rand())+'@sina.com')

    response = requests.request("get", url="http://127.0.0.1:8000/client/registration/5")
    #print (response.text)
    cookie = response.cookies
    url = "http://127.0.0.1:8000/client/registration/5"
    data = {
        'csrfmiddlewaretoken': cookie['csrftoken'],
        'first_name': 'Xiaofeng',
        'last_name': 'Kang',
        # name
        'email': em,
        'password1': '12q12q12q',
        'password2': '12q12q12q',
        'is_accepted': '1',
        'submit': 'Register'
    }
    headers = {
        'Cookie': response.headers['Set-Cookie']
    }
    response = requests.request("post", url, data=data, headers=headers)
    #print (response.text)
    cookies=response.cookies

    ############step1######
    url = "http://127.0.0.1:8000/client/profile/step-one"
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cache-Control': "max-age=0",
        'Connection': "keep-alive",
        # 'Content-Length': "529",
        'Content-Type': "application/x-www-form-urlencoded",
        ##cookies 从login里的cookies获取
        # 'Cookie': 'csrftoken=6blNbvZ8DKZgfoC3tX1vdwq7ZxVIATW9UtCEjKrXLuE0ovpXYGa0ls7Oa7yyE24u; sessionid=rlev9oe4j8kcrli5l7bqlyz4ib6bjelc',
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-one',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data = {
        ##cookies 从login里的cookies获取
        'csrfmiddlewaretoken': cookies['csrftoken'],
        'client-first_name': 'Xiaofeng',
        'client-last_name': 'Kang',
        'client-birth_date': '03-02-2019',
        'client-marital_status': 'Single',
        'spouse-first_name': 'll',
        'spouse-last_name': 'll',
        'spouse-birth_date': 'll',
        'client-street': 'll',
        'client-city': '1111111111111', 
        'client-mailing_street': 'll',
        'client-mailing_city': 'll',
        'client-phone_number': '(111) 111 - 1111',
        'client-annual_income': annual_income,
        'client-estimated_income_tax': income_tax,
        'client-liquid_net_worth': liquid_net_worth,
        'client-employment_type': employment_type,
        'Continue': 'Continue'
    }
    response = requests.request("post", url, data=data, cookies=cookies)
    #print (response.text)
    cookies=response.cookies

    #############step2##############
    url = 'http://127.0.0.1:8000/client/profile/step-two'
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
    data = {
        'csrfmiddlewaretoken': cookies['csrftoken'],
        'answer_11': financial_goal,
        'answer_10': expected_returns,
        'answer_9': would,
        'answer_12': need,
        'Continue': 'Continue',
    }
    response = requests.request("post", url, data=data, cookies=cookies)
    #print (response.text)
    cookies=response.cookies

    ###########step3######################
    url = 'http://127.0.0.1:8000/client/profile/step-three'
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cache-Control': "max-age=0",
        'Connection': "keep-alive",
        # 'Content-Length': "529",
        'Content-Type': "application/x-www-form-urlencoded",
        ##cookies 从login里的cookies获取
        'Cookie': 'csrftoken=SIWszHfob6Ca337Nk1APMvHPWXOK442NQnwj2dGnAlaXOMm3YhgDKiabtKDOhhgP; sessionid=06wsmrjym7nk6fa1ibiqnhcncbqd45ci',
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-one',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    data = {
        'csrfmiddlewaretoken': cookies['csrftoken'],
        'client_account_types-groups': 'deposit_money'
    }
    response = requests.request("post", url, data=data, cookies=cookies)
    #print (response.text)
    cookies=response.cookies

    ##########step3_1################
    url = 'http://127.0.0.1:8000/client/profile/show-deposit-account-form'
    headers = {
        'Cookie': 'csrftoken=' + cookies['csrftoken'] + '; ' + 'sessionid=' + cookies['sessionid'],
        'Host': '127.0.0.1:8000',
        'Origin': 'http://127.0.0.1:8000',
        'Referer': 'http://127.0.0.1:8000/client/profile/step-two',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'csrfmiddlewaretoken': cookies['csrftoken'],
        'client_account_types-group_type': 'Personal Account',
        'client_account_types-groups': 'deposit_money'
    }
    response = requests.request("post", url, data=data, cookies=cookies, headers=headers)
    #print ('6:')
    cookies=response.cookies

    ###########step3_2###################
    url = 'http://127.0.0.1:8000/client/profile/update-account-form/deposit_money'
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
        # 'value': '1,111,111.00',
        'contribution_type': 'neither'
    }
    response = requests.request("post", url, data=data, headers=headers)
    #print ('7')

    ###############step3_3###############
    url = 'http://127.0.0.1:8000/client/profile/create-account/deposit_money'
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
        'value':acount_money ,
    }
    response = requests.request("post", url, data=data, headers=headers)
    #print ('8:')

    ###########logout###############
    response = requests.request("get", 'http://127.0.0.1:8000/logout', cookies=cookies)
    #print ('9:')
    cookies=response.cookies

    ############login##############
    response = requests.request("get", 'http://127.0.0.1:8000/login')
    #print ('10:')
    cookies = response.cookies
    data = {
        'csrfmiddlewaretoken': cookies['csrftoken'],
        'username': em,
        'password': '12q12q12q',
        '_submit': 'Login'
    }
    response = requests.request('post', url='http://127.0.0.1:8000/login', data=data, cookies=cookies)
    #print ('11:')
    cookies=response.cookies

    ########portfolio###########
    url = 'http://127.0.0.1:8000/client/portfolio'
    response = requests.request("get", 'http://127.0.0.1:8000/client/portfolio', cookies=cookies)
    #print ('12:')
    soup = BeautifulSoup(response.text, 'html.parser')
    # print (soup.prettify())
    return response.text
    # print(response.text)

