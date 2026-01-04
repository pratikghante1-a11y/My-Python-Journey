import random 

target_number = random.randint(1,10)
attempts= 0

print("---Number guessing game me apka swagat hai---")
print("Maine 1 se 10 ke beech ek number socha hia. kya aap usse guess kar sakte hai?")

while True:  
    user_guess = int(input("Apna guess enter karen: "))
    attempts += 1
    
    if user_guess < target_number:
        print("Bahut chhota! hai thoda bada number daalo")
    elif user_guess > target_number:
        print("Bahut bada! hai thoda chhota number daalo")
    else:
        print(f"badhai hoh! apne {attempts} attempts me sahi number guess kiya!")
        break
