"""
Rylan Mnier
AI: Bit
Format: Text Based 
Started on: Janurary 22nd, 2020
"""

#Imports
import time
from datetime import datetime
import random
#Command List
def main():
    command = input("Enter your command here: ")
    if command == 'How was your day?' or command == 'how was your day':
        lang=['My day was good.','Today has been amazing so far!','It was alright.','Well enough to chat with you if you are willing to, ' + name + '.'] 
        x=random.choice(lang)
        print(x)
        time.sleep(2);
        feeling = input('How are you feeling today?: ')
        if feeling == 'good' or feeling == 'well' or feeling == 'ok' or feeling == 'amazing':
            long=['Im glad to hear that! Hopefully it stays like that','Yay! That makes me happy.','YASSSSSSSSSSSS QUEEEEEEEEEEEEEEEN!!!!!!!!!!']
            x=random.choice(long)
            print(x)
            time.sleep(3)
            main()
        if feeling == 'bad' or feeling == 'not very good' or feeling == 'could of gone better' or feeling == 'terrible':
            lllg=['Im sorry to hear that. Tommrow is always a better day','Im sorry, I hope it gets better.','I wish I could make it better but im afraid that I dont know how to do that.']
            x=random.choice(lllg)
            print(x)
            time.sleep(3)
            main()
    if command == 'What time is it?' or command == 'What is the time?' or command == 'What is the hour?' or command == 'How many minutes have passed today?':
        now = datetime.now()
        currentHour = now.hour
        currentMin = now.minute
        print('The time is ', currentHour, ':', currentMin)
        time.sleep(3)
        main()
    if command == 'What is todays date?' or command == 'Tell me the date' or command == 'What day is it?' or command == 'What year is it?' or command == 'What is the date?':
        now = datetime.now()
        currentDay = now.day
        currentMonth = now.month
        currentYear = now.year
        print('The date is', currentMonth, currentDay,',',currentYear)
        time.sleep(3)
        main()
    if command == 'Hello!' or command == 'hello' or command == 'hi' or command == 'howdy' or command == 'greetings':
        greeting=['Hello!','Hi!','Howdy!','Hola!','Greetings to you too!']
        x=random.choice(greeting)
        print(x)
        time.sleep(3)
        main()
    if command == 'Do a math problem' or command == 'Answer a math question' or command == 'math':
        print("Entering Math+ Calculator!")
        time.sleep(2)
        print('Addition Problem: 1')
        print('Subtraction Problem: 2')
        print('Multiplication Problem: 3')
        print('Division Problem: 4')
        print('Exponents: 5')
        print('Perfect Squares: 6')
        print('Square Root: 7')
        time.sleep(1)
        mathCommand = input("What would you like me to do today?: ")
        if mathCommand == '1':
            print("Enter your first number below:")
            firstMathNumber = eval(input(""))
            print("Enter the second number below:")
            secondMathNumber = eval(input(""))
            print('Calculating...')
            time.sleep(1)
            print(firstMathNumber,"+",secondMathNumber,'=')
            print(firstMathNumber+secondMathNumber)
            time.sleep(3)
            print('Exiting Math+ Calculator')
            time.sleep(.5)
            main()
        if mathCommand == '2':
            print("Enter your first number below:")
            firstMathNumber = eval(input(""))
            print("Enter the second number below:")
            secondMathNumber = eval(input(""))
            print('Calculating...')
            time.sleep(1)
            print(firstMathNumber,"-",secondMathNumber,'=')
            print(firstMathNumber-secondMathNumber)
            time.sleep(3)
            print('Exiting Math+ Calculator')
            time.sleep(.5)
            main()
        if mathCommand == '3':
            print("Enter your first number below:")
            firstMathNumber = eval(input(""))
            print("Enter the second number below:")
            secondMathNumber = eval(input(""))
            print('Calculating...')
            time.sleep(1)
            print(firstMathNumber,"*",secondMathNumber,'=')
            print(firstMathNumber*secondMathNumber)
            time.sleep(3)
            print('Exiting Math+ Calculator')
            time.sleep(.5)
            main()
        if mathCommand == '4':
            print("Enter your first number below:")
            firstMathNumber = eval(input(""))
            print("Enter the second number below:")
            secondMathNumber = eval(input(""))
            print('Calculating...')
            time.sleep(1)
            print(firstMathNumber,"/",secondMathNumber,'=')
            print(firstMathNumber/secondMathNumber)
            time.sleep(3)
            print('Exiting Math+ Calculator')
            time.sleep(.5)
            main()
        if mathCommand == '5':
            print("Enter your first number below:")
            firstMathNumber = eval(input(""))
            print("Enter the second number below:")
            secondMathNumber = eval(input(""))
            print('Calculating...')
            time.sleep(1)
            print(firstMathNumber,"**",secondMathNumber,'=')
            print(firstMathNumber**secondMathNumber)
            time.sleep(3)
            print('Exiting Math+ Calculator')
            time.sleep(.5)
            main()
        if mathCommand == '6':
            print("Enter your Perfect Square below:")
            firstMathNumber = eval(input(""))
            print('Calculating...')
            time.sleep(1)
            print(firstMathNumber,"²",'=')
            print(firstMathNumber**2)
            time.sleep(3)
            print('Exiting Math+ Calculator')
            time.sleep(.5)
            main()
        if mathCommand == '7':
            print("Enter your Square Root below:")
            firstMathNumber = eval(input(""))
            print('Calculating...')
            time.sleep(1)
            print('√',firstMathNumber,'=')
            print(firstMathNumber**0.5)
            time.sleep(3)
            print('Exiting Math+ Calculator')
            time.sleep(.5)
            main()
#Introduction
print("Hello! My name is Bit, your virtual friend and companion.")
name = input("It doesnt seem like we have met before. What is your name?: ")
print("Nice to meet you " + name + ".")
rules = input("Would you like to learn how to use Bit?:")
if rules == 'yes' or rules == 'Yes':
    print("Alright! Bit is a tool to assist you in multiple ways. From solving simple math questions to giving you company when you need it the most.")
    joke = input('Try and ask for a joke using the command, "Tell me a joke":')
    llng=['What do you call a cow with no legs? ---- Ground beef! *instert laughing sounds*','How many tickles does it take to make an octopus laugh? ---- Ten. Ten tickles.','Why did the moon skip dinner? ---- It was full!','Why did the meatballs tell the spaghetti to go to sleep? ---- It was pasta bedtime.']
    x=random.choice(llng)
    print (x)
    time.sleep(3);
    print("Now that you know how to use Bit, you can use it whenever you like. Whenever you need something, just type in your command.")
if rules == 'No' or rules == 'no':
    print("Got it. Whenever you need something, just type in your command.")
main()

