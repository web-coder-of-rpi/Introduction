print("Hello, I am Chatbot 2.0! 😊")
#get name of user
print("To start, tell me more about yourself.")
full_name = input("What is your full name? ").split()
print(f"Hello {full_name[0]}!")
#get grade of user
grade = int(input(f"What grade are you in {full_name[0]}? "))
#check to see if still in school
if grade > 12:
    print("Wow, you graduated high school!")
else:
    enjoy = input("How are you enjoying school? ")
#check to see how the user is feeling
feel = input("How are you feeling today? ").lower()
if feel == "good":
    print("I'm glad you are having a good day!😊")
elif feel == "bad":
    print("I'm sorry you feel that way")
else:
    print("I understand that sometimes it's hard to put a word to a feeling")

print("Stay tuned, more upgrades coming up👍!")
