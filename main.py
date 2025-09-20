print('Welcome, traveler! I help wanderers find their way. ' \
'My name is Ross Croad.')

name = input('May I have the honor of knowing who I am speaking to? ')
age = input('How old are you, if you do not mind me asking? ')

def myAge()
    if age < 12:
        print("My goodness, aren't you a little too young to travel on your own?")
    elif age>= 12 && age=<30:
        print("Ah, I assume you are headed to the factory to work?")
    elif age> 20 && age=<60:
        print("Ah, I remember when I was your age. So full of life, and now I am old!")
    elif age>60 && age<100:
        print("My, my! Many would not have lived up to your age in this day.")
    elif age>100:
        print("Oh ho! Not many men are wise enough to live as long as you have.")
    elif age<1:
        print("Sorry? I don't think that's true.")
        myAge();
        
dir = input("How can I help you today? ")
print("1. Lost ")
print("2. Hungry ")
print("3. Sleepy")

