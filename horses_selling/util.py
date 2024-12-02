# All the helping functions
from config import HORSE_INFO



def print_horse_info():
    horse = HORSE_INFO(NAME = "Juan")    
    print(horse.NAME)

if __name__ == "__main__":
    print_horse_info()