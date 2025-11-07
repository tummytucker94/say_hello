import logging
import time
from functions.greetings import say_hello

logging.basicConfig(
    filename='runtime.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

if __name__ == "__main__":
    start = time.time()
    user_name = input("Enter your name: ")
    greeting = say_hello(user_name)
    print(greeting)
    end = time.time()
    logging.info(f"Greeted user '{user_name or 'there'}' in {end - start:.4f} seconds")
