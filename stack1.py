#create a stack example

def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack)

def push(stack, item):
    stack.append(item)
    return stack

def pop(stack):
    
    stack.pop()
    return stack

stack = create_stack()
push(stack,str(1))
push(stack, str(2)) 
pop(stack)

print(stack)

nums = [1,2,4,1,6,3,2]
nums.sort()
