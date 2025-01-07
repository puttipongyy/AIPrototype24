import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--bd',
        type=int,
        required=True,
        # default=7,
        help= 'input for birthday of the user format (ddmmyyyy).'     
    )

    parser.add_argument(
        '--name',
        type=str,
        # required=True,
        default='Puttipongyy',
        help= 'input the name of people who are using the app.'     
    )
    
    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello world, {who}!!")

def cal_todayVbd(bd):
    date_format = "%m%d%Y"

    bday = datetime.strptime(bd,date_format)
    # b = datetime.strptime('9/26/2008', date_format)
    # print(delta.days)
    td = datetime.today().strftime(date_format) 
    delta = td - bday  
    return delta

if __name__=="__main__":
    input_v = parse_input()
    print("this is my first .py file.")
    printHello(input_v.name)
    print(f"your birthday is {cal_todayVbd(input_v.bd)} from today")



