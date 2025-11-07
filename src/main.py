from src.functions.greetings import say_hello
import logging
import time

# Configure logging
logging.basicConfig(
    filename='runtime.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

if __name__ == "__main__":
    
    # Measure execution time
    start = time.time()
    say_hello("Jermaine")
    end = time.time()
    