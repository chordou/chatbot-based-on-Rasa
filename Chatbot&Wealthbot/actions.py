# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from bs4 import BeautifulSoup
import bs4
from rasa_core_sdk import Action
#import register, step1, step2, step3

import sys
sys.path.append('C:\\Users\kxf\Desktop\Chatbot&Wealthbot')
import WealthbotConnection as wcon
import main2
import numpy as np

logger = logging.getLogger(__name__)

class ActionWealthbot2(Action):
    def name(self):
        return "action_wealthbot2"
    
    def run(self, dispatcher, tracker, domain):  
        annual_income = tracker.get_slot('income')
        income_tax = tracker.get_slot('tax')
        employemt_type = tracker.get_slot('employ')
        liquid_net_worth = tracker.get_slot('networth')
        finanical_goal = tracker.get_slot('goal')
        expected_returns=tracker.get_slot('returns')
        would=tracker.get_slot('would')
        need=tracker.get_slot('need')

        
        text = main2.main(annual_income=annual_income, income_tax=income_tax, liquid_net_worth=liquid_net_worth, employment_type=employemt_type,
                          financial_goal=finanical_goal, expected_returns=expected_returns,would =would, need =need,acount_money='1,111,111.00')
        soup = BeautifulSoup(text, 'html.parser')
        
        portfolio = ['your portfolio:']
        for tbody in soup.find('tbody'):
            if isinstance(tbody, bs4.element.Tag):
                tds = tbody('td')
                portfolio.append([tds[0].string, tds[1].string, tds[2].string])
                #portfolio.append('\n')
        dispatcher.utter_message(str(portfolio))
     

class ActionWealthbot1(Action):
    def name(self):
        return "action_wealthbot1"
    
    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email')
        password = tracker.get_slot('password')
        response = wcon.login(email, password)
        print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        portfolio = ['your portfolio:']
        for tbody in soup.find("tbody"):
            if isinstance(tbody, bs4.element.Tag):
                tds = tbody("td")
                portfolio.append([tds[0].string, tds[1].string, tds[2].string])
                portfolio.append(['\n'])
        dispatcher.utter_message(str(portfolio))
        
class ActionStockinfo(Action):
    def name(self):
        return "action_stockinfo"
    
    def run(self, dispatcher, tracker, domain):
        stock = tracker.get_slot('stock')

        url = 'https://gupiao.baidu.com/stock/'+'sz300370'+'.html'
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.text, "html.parser")
        info = soup.find('div', attrs={'class':'stock-bets'})
        #stock = info.find_all(attrs={'class':'bets-content'})
        key = info.find_all('dt')
        value = info.find_all('dd')
        infoDic = {}
        for i in range(len(key)):
            k = key[i].text
            v = value[i].text
            infoDic[k] = v
            
        dispatcher.utter_message(str(infoDic))
