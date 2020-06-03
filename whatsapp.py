# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:59:23 2020

@author: Madhur
"""

from twilio.rest import Client 
 
account_sid = 'AC318f55065b5e56a6df72e0b06caa20d4' 
auth_token = 'c6230fa9b4690c08e54201f9b530c122' 
client = Client(account_sid, auth_token) 
def send_love():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello ,How are you?',      
                              to='whatsapp:+919955746995' 
                          ) 
 
    print(message.sid)