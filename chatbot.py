# --- Define your functions below! ---
def hi():
    print("hey")

def hello(answer):
    if("there" in answer):
        print("hello")
    else:
        print("hi")

def intro():
    print("Hi, I am Chatbot")


def process_input(answer):
    if(answer == "Hello" or answer == "hi"):
        hey()
    elif("bye" in answer):
        bye()
    elif(answer == "hey"):
        ("hey" in answer)
    else:
        print("That's Cool")




# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?)")
        process_input(answer)




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
