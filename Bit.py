"""
Rylan Mnier
AI: Bit
Started on: Janurary 22nd, 2020
"""

#Imports
import time

#Command List
def main():
    command = input("Enter your command here: ")
    if command == 'How was your day?' or command == 'how was your day':
        import random
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
    print("Sorry, I didn't understand. Can you repeat that?")
    main()
#Introduction
print("Hello! My name is Bit, your virtual friend and companion.")
name = input("It doesnt seem like we have met before. What is your name?: ")
print("Nice to meet you " + name + ".")
rules = input("Would you like to learn how to use Bit?:")
if rules == 'yes' or rules == 'Yes':
    print("Alright! Bit is a tool to assist you in multiple ways. From solving simple math questions to giving you company when you need it the most.")
    joke = input('Try and ask for a joke using the command, "Tell me a joke":')
    print("What do you call a cow with no legs?")
    time.sleep(3);
    print("Ground beef! *instert laughing sounds*")
    time.sleep(3);
    print("Now that you know how to use Bit, you can use it whenever you like. Whenever you need something, just type in your command.")
if rules == 'No' or rules == 'no':
    print("Got it. Whenever you need something, just type in your command.")
main()

