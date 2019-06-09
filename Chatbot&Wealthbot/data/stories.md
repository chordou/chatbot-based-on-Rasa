## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_greet <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' -->  
 
## story_goodbye
* goodbye
  - utter_goodbye
  
## stroy_thanks
* thanks
 - utter_thanks
  
## story_wealthbot_consulting01
* greet
 - utter_greet
* wealthbot_consulting
 - utter_client
* affirm
 - utter_ask_email
* wealthbot_consulting{"email":"lizelee@126.com"}
 - slot{"email":"lizelee@126.com"}
 - utter_ask_password
* wealthbot_consulting{"password":"lz123456"}
 - slot{"password":"lz123456"}
 - action_wealthbot1
 
   
## story_wealthbot_consulting02
* greet
 - utter_greet
* wealthbot_consulting
 - utter_client
* deny
 - utter_ask_name
* wealthbot_consulting{"name":"Lucy"}
 - slot{"name":"Lucy"}
 - utter_ask_address
* wealthbot_consulting{"address":"taposai"}
 - slot{"address":"taposai"}
 - utter_ask_income
* wealthbot_consulting{"income":"$150,001-$250,000"}
 - slot{"income":"$150,001-$250,000"}
 - utter_ask_tax
* wealthbot_consulting{"tax":"10"}
 - slot{"tax":"10"}
 - utter_ask_networth
* wealthbot_consulting{"networth":"$0-$25,000"}
 - slot{"networth":"$0-$25,000"}
 - utter_ask_employ
 * wealthbot_consulting{"employ":"Employed"}
 - slot{"employ":"Employed"}
 - utter_ask_financial_goal
 * wealthbot_consulting{"financial_goal":"lowewr returns"}
 - slot{"financial_goal":"lowewr returns"}
 - utter_ask_returns
 * wealthbot_consulting{"returns":"+-15"}
 - slot{"returns":"15"}
 - utter_ask_would
 * wealthbot_consulting{"would":"sell all"}
 - slot{"would":"sell all"}
 - utter_ask_need
 * wealthbot_consulting{"need":"1"}
 - slot{"need":"1"}
 - action_wealthbot2
 
## story_stock_info_consulting
* greet
 - utter_greet
* stock_consulting
 - action_stockinfo

 
 
 
 


