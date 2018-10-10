print("""room w 2 doors
        choose one of dem""")
door = input(">")
door = int(door)

if door == 1:
    print("therez a bear. 1 to take her cake 2. to scream at her")
    bear = int(input(">"))
    if bear == 1:
        print("u ded")
    elif bear == 2:
        print("u ded 2")
    else:
        print(f"{bear} is a win, u won")
elif door == 2:
    print("therez chthulhu, choose 1 2 or 3")
    inp = int(input(">"))
    if inp == 1:
        print("u won")
    elif inp == 2:
        print("u ded")
    else:
        print("u ded")

print("its over")
    
