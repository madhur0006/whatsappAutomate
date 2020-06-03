# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:08:54 2020

@author: Madhur
"""

#from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from whatsapp import send_love
#def job_function():
   # print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_love, 'interval', seconds=10)

sched.start()