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