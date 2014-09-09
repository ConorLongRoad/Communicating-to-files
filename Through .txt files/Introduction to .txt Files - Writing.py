count = 1

def append():
    with open("/myfile.txt", mode="w",encoding="utf-8") as my_file:
        inputName = my_file.write("John")
return inputName

def write():
    with open("/myfile.txt", mode="w",encoding="utf-8") as my_file:
        inputName = my_file.write(inputName)
return inputName

def read():
    with open("/myfile.txt", mode="r",encoding="utf-8") as my_file:
        for line in my_file:
            print("{0}. {1}".format(count,line))
            count = count + 1

def main():
    inputName = append()
    inputName = write()
    
