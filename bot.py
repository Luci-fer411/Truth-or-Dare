import telebot

import random
import pandas as pd


API_KEY = '5307902104:AAGYlBsyBBOGw4y2oTJ9VjuBRrKkoL6jGxU'
bot = telebot.TeleBot(API_KEY)

us = bot.get_me()

@bot.message_handler(commands=['hi'])
def hi(message):
     bot.send_message(message.chat.id , 'hello!')
     
 
     
file = pd.read_csv('truth.csv')
k = file.iloc[:,-1]

file1 = pd.read_csv('dare.csv')
t = file1.iloc[:,-1]

def pt(message):
   while(True):
     l = random.choice(k)
  
     bot.reply_to(message , l)
     break
def pk(message):
     while(True):
          y = random.choice(t)
          bot.reply_to(message,y)
          break

names = ['R@j', 'Angel','Dr@shti', 'Honey']      
@bot.message_handler(commands=['truth'])
def prsg(message):
    bot.reply_to(message,'Processing...')
    
    
    while(True):
         k = random.choice(names)
         bot.reply_to(message,k)
         pt(message)
         break
    
@bot.message_handler(commands=['dare'])
def rsg(message):
    bot.reply_to(message,'Processing...')
    
    
    while(True):
         k = random.choice(names)
         bot.reply_to(message,k)
         pk(message)
         break
        
  

         
bot.polling()
