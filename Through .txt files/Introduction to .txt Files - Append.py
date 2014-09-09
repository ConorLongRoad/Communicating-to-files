end = False
with open("/myfile.txt", mode="a",encoding="utf-8") as my_file:
    while end == False:
        nameToAppend = input("What name would you like to enter? ")
        if nameToAppend == "-1":
            end = True
        my_file.write(nameToAppend)
        
my_file.close()
