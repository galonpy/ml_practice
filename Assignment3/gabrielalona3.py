"""
CS3C, Assignment #3, Linked Lists and Stacks
Gabriel Alon
Driver Code
Use a Stack/Linked List to process a string left to right and check if all valid characters are paired correctly
"""

from Assignment3.gabrielalonstack import Stack
from Assignment3.gabrielalonnode import Node

ok = Stack()
ok.push(5)
ok.push(4)
ok.delete_stack()
#ok.pop()


def matches(top, symbol):
    if top == '(' and symbol == ')' or (top == '[' and symbol == ']') or (top == '{' and symbol == '}'):
        return True
    else:
        return False


def ll_algorithm(my_stack, user_input):
    balanced = True
    # validate symbol matching
    index = 0
    while index < len(user_input) and balanced:
        symbol = user_input[index]
        if balanced:
            if symbol in '([{}])':
                if symbol in '([{':
                    my_stack.push(symbol)
                else:
                    if my_stack.is_empty() and symbol in ')]}':  # redundant for clarity
                        print("error closing symbol but empty stack")  # ?validate this
                        balanced = False
                    else:
                        top = my_stack.pop()
                        if not matches(top, symbol):
                            print("opening symbol does not match closing symbol")  # ? validate this
                            balanced = False
                index = index + 1
            else:
                index = index + 1
    if balanced and my_stack.is_empty():
        return True
    else:
        return False


finished = None
while finished != 0:
    user_input = input("Input:")
    my_stack = Stack()
    print(ll_algorithm(my_stack, user_input))
    test_stack = Stack()
    assert (ll_algorithm(test_stack, '([|)]))') == False)
    assert (ll_algorithm(test_stack, '() (() [()])') == False)
    assert (ll_algorithm(test_stack, '{{([][])}()}') == False)

"""
The space complexity here is O(N) because that is the worse case going through the length of the string
The time complexity is O(N) because in some cases we iterate over N elements and that is the worst case.

Examples
1) correctly ignores non symbol character '|'
#Input: ([|)] 
false 

2)
#Input: () (() [()]) 
#true

3)
#Input: {{([][])}()} 
true
        
4) detects attempting to pop from an empty stack 
#Input:) 
error closing symbol but empty stack 
False 

5)detects an incorrect pairing symbol popped from the stack

#Input:(] 
#opening symbol does not match closing symbol 
#False
"""

"""
Input:([|)]
opening symbol does not match closing symbol
False
Input:() (() [()])
True
Input:{{([][])}()}
True
Input:)
error closing symbol but empty stack
False
Input:(]
opening symbol does not match closing symbol
False
"""
