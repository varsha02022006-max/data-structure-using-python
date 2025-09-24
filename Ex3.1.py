max_size=5
stack=[]
top=-1

def push(book_title):
    global top
    if top >= max_size-1:
        print(" stack over flow! cannot push more books.")

    else:
        top +=-1
        stack.append(book_title)
        print(f"book'(book title)' pushed onto the stack.")

def pop():
    global top
    if top==-1:
       print("stack under flow ! cannot pop any book.")

    else:
        removed_book=stack.pop()
        print(f"book'(removed_book)' popped from the stack.")
        top==-1
def peek():
    if top==-1:
        print("stack is empty. no book to peek.")
    else:
        print(f"top book on the stack:'(stack[top])'")


def display():
    if top==-1:
       print("stack is empty.")
    else:
        print("book in stack (top to bottom):")
        for i in range (top,-1,-1):
            print(f"{i+1}.{stack[i]}")
push("The sum also rises")
push("The jungle book")
push("All  around the world in 18 days")
push("Chirst topper")
push("The  name last")
push("The genius wallet")
display()
peek()
pop()
pop()
display()
peek()
    
