import pickle

class stats():
    def __init__(self):
        self.level = 0
        self.HP = 100
        self.ammo = 100
        self.location = "Berlin"
        self.zombies = 50

def get_file_name():
    try:
        file = input("Please enter the file you wish to load: ")
    except No such file or directory:
        print("Please enter a vaild save name.")
    return file

def renewing_stats(file):
    with open(file ,mode="rb") as my_file:
        new_data = pickle.load(my_file)
        print(new_data.level, new_data.HP, new_data.ammo, new_data.location, new_data.zombies)
    
def main():
    file = get_file_name()
    renewing_stats(file)
main()
