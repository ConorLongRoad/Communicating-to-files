with open("/myfile.txt", mode="r", encoding="utf-8") as my_file:
    count = 1
    for line in my_file:
        print("{0}. {1}".format(count,line))
        count = count + 1
