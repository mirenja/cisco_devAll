file = open("devices2.txt", "a")
while True:
    newItem = input("ENter device name : ")
    if newItem == "exit":
        print("all done!")
        break
    else:
        file.write(newItem + "\n")
file.close()