from collections import defaultdict

def dec_hello(func):
    def wrapper(check):
        print(f"check {check}")
        func(check)
    return  wrapper

@dec_hello
def hello(checknum):
    print(f"checknum : {checknum}")


if __name__=="__main__":
    print("Hello World!!")
    hello("name") 
