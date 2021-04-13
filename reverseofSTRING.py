# reverse of string using stack
from stack import Stack
def reverse(str):
    stack= Stack()
    rev=''
    a=''
    for i in range (len(str)):

        stack.push(str[i])
    while not stack.isempty():
        a=stack.pop()
        rev= rev+a  
    print(rev)

if __name__=="__main__":
    reverse('darshika')
