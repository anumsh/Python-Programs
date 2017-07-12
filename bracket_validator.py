"""
You're working with an intern that keeps coming to you with JavaScript code that won't run because the braces, brackets, and parentheses are off. To save you both some time, you decide to write a braces/brackets/parentheses validator.
Let's say:

'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False
"""

def is_valid(code):
    openers_to_closers = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    openers = frozenset(openers_to_closers.keys())
    print "the operners are : ",openers
    closers = frozenset(openers_to_closers.values())
    print "the closers are :", closers

    openers_stack = []
    print "opener_new_stack----------",openers_stack

    for char in code:
        if char in openers:
            print "the characters are :",char
            openers_stack.append(char)
        elif char in closers:
            print "char in closers "
            print openers_stack
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()

                # if this closer doesn't correspond to the most recently
                # seen unclosed opener, short-circuit, returning false
                if not openers_to_closers[last_unclosed_opener] == char:
                    return False

    return openers_stack == []
    
print is_valid("hdfhsj([{}])fdffjfghb")
print is_valid("hdfhsj([{]fdffjfghb")
