from src.functions.greetings import say_hello
import logging
import time



if __name__ == "__main__":
    
    # Configure logging
    logging.basicConfig(
    filename='runtime.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s')


    # Measure execution time
    start = time.time()
    user_name = input("Enter your name: ")
    greeting = say_hello(user_name)
    end = time.time()

    # Print and log
    print(greeting)
    logging.info(f"Greeted user '{user_name or 'there'}' in {end - start:.4f} seconds")
    