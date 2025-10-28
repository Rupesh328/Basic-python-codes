command = ""
while command.lower() != "quit":
    command = input(">")
    if command == "start":
        print("Car start")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
              start - to start the car
              stop - to stop the car
              quit - to quit""")
    elif command =="quit":
        break
else:
    print("sorry , don't understand that!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    