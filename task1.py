import random
count = 0

#initializing list.
names = ["terry", "john", "scary", "hello", "hide", "version", "kill", "snake", "rat", "pumpkin", "tea", "willing", "orange", 
         "calm", "gorilla", "tea", "lively", "bullet", "impressive","navy"]

print("Password Generator")
print("===================")

try:
    number_of_password = int(input("How many passwords are needed?: "))
    
    if number_of_password <= 0 or number_of_password > 26:
        print("Please enter a value between 1 and 26")
    else:
        for i in range(number_of_password):
            p = random.sample(names, 3) #picks 3 elements from list name.
            print(i + 1 ,"-->", end = " ")
            for password in p:
                print(password, end = "")
                count += 1
                if count == 3: 
                    print() #move to next line after printing 3 elements from names.
                    count = 0
except ValueError:
    print("Please enter a number.")