def say_hello(user_name):
    if user_name.strip() == "":
        user_name = "there"
    greeting = "Hello: " + user_name + "!"
    return greeting