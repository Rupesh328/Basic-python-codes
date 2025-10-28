secret = 7
guess_count=0
while guess_count < 3: 
    guess=int(input("guess :"))
    guess_count += 1
    if secret==guess:
        print("you won!!")
        break  
else:
    print("you lost")
    