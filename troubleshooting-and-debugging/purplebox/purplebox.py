#!/usr/bin/env python3
import time
import random
import sys

def generate_random_num(min_value, max_value):
    """This funciton returns random numbers between given range"""
    return random.randint(min_value, max_value)


def main():
    while True:
        num = generate_random_num(1,100)
    
        if num % 2 == 0:
            print("Finally, a pair number!!!")
            sys.exit(0)
            break
        else:
            print("Ooops, ow number!")

        time.sleep(1)

main()
