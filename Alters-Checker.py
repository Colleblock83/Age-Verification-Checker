print("Welcome to the Age-Verification!")
print("")
print("")
age_input = int(input("How old are you?: "))

if age_input == 1:
    print("Bro you're not even able to use a computer at that age! ")
elif age_input <= 17:
    print("You're a minor, please leave that program immediately ")
elif age_input >= 18 and age_input <= 64:
    print("You're an adult.")
    print("")
    say_hello = str(input("You're allowed to type in the word Hello! "))
    if say_hello == "Hello":
     print("Hello back!")
    else:
     print("Oh, I was not able to understand what you wanted to type!")

elif age_input >= 65 and age_input <= 100:
    print("You are an old man.")
    print("")
    say_hello = str(input("You are still allowed to type in the word Hello! "))
    if say_hello == "Hello":
            print("Hello back old man!")
    else:
            print("Oh, I was not able to understand what you wanted to type! ")
else:
    print("The integer value cannot be over 100")

input("Press any key to close the program... ")







