import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-t', "--time",default = 5)    

args = parser.parse_args()
timet =int(args.time)
print(timet)

time.sleep(timet)

user_input = input("Press Enter to continue... ")

time.sleep(timet)

print("You entered:", user_input)

print("Bye")
