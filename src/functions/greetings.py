import logging
import time

logging.basicConfig(
    filename='runtime.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def say_hello(name):
    if name == " ":
        name = "there"
        greeting = "Hello " + name + "!"
        return greeting
    elif name == "":
        name = "there"
        greeting = "Hello " + name + "!"
        return greeting
    else:
        greeting = "Hello " + name + "!"
        return greeting

logging.info(f"Greeted user '{name or 'there'}' in {end - start:.4f} seconds")
