def anounce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@anounce
def hello():
    print("hello")

hello()
