import requests
import numpy as np
#namelist=[]
#for i in range(1000):
    #namelist.append(str(i)+'@sina.com')
#np.save('namelist',namelist)



def register(name):
    namelist = []
    namelist = np.load('namelist.npy')
    e-name = namelist[0]
    namelist = np.delete(namelist, [0])
    np.save('namelist', namelist)
    ##############
    response = requests.request("get", url="http://127.0.0.1:8000/client/registration/5")
    #print(response.headers)
    cookie=response.cookies
    url = "http://127.0.0.1:8000/client/registration/5"
    data={
        'csrfmiddlewaretoken':cookie['csrftoken'],
        'first_name': name,
        'last_name': 'Kang',
        'email': e-name,
        'password1': '12q12q12q',
        'password2': '12q12q12q',
        'is_accepted': '1',
        'submit':'Register'
    }
    headers={
        'Cookie':response.headers['Set-Cookie']
    }
    #print(headers)
    response = requests.request("post", url, data=data,headers=headers)
    #print(response.text)
    #print(response.cookies)
    return response.cookies
#register()
