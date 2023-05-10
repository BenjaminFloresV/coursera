#!/usr/bin/env python3
import random


def show_message(message):
    print(f"This is our message: {message}")


def set_message():
    value = random.randint(1,11)
    
    message = "Hello, God is life"
    if value % 2 == 0:
        message = "Hello, Satan is life"

    return message


if __name__ == "__main__":
    message = set_message()
    show_message(message)

