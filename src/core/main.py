import logging
import time
from functions.greetings import say_hello

logging.basicConfig(
    filename='runtime.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

if __name__ == "__main__":
    user_name = input("Enter your name: ")

    start = time.perf_counter()   # higher-precision timer
    greeting_msg = say_hello(user_name)
    end = time.perf_counter()

    print(greeting_msg)
    logging.info(f"Greeted user '{user_name or 'there'}' in {end - start:.6f} seconds")
