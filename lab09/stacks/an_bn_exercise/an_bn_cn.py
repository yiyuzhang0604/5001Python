# Name: Yiyu Zhang
# Github: https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-YiyuZhang

import sys
sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # nopep8
# from stack_linked_list import Stack  # nopep8


class AnBnCn:
    """Class for evaluating strings of n A's followed by n B's"""
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def accept(self, in_string):
        """Takes a string and returns a boolean
indicating whether the string matches the pattern"""
        # TODO:
        # Return True if in_string's brackets match,
        # False otherwise

        # Solution:
        # Intuition: see an a, push it on the stack,
        # see a b, pop an a off of the stack, expect
        # to wind up with an empty stack.

        # We need to know whether an a is okay to see.
        # We can set a boolean to represent whether
        # we expect an a. We'll expect a until we see
        # the first b, after which we won't expect
        # any more a's.
        expect_a = True
        expect_b = True
        for ch in in_string.lower():
            # If we see an expected a, put it in the stack.
            if ch == "a":
                if expect_a:
                    self.stack1.push(ch)
                else:
                    # unexpected a -> fail
                    return False
            elif ch == "b":
                # If we see a b, there should be a's in
                # the stack to match.
                if self.stack1.is_empty():
                    return False
                else:
                    # If we see b when we're expecting a,
                    # we should no longer expect any a's.
                    # Also, pop one a from the stack.
                    if expect_a:
                        expect_a = False
                        self.stack1.pop()
                    else:
                        # See a b when we're expecting a b,
                        # we just need to pop an a from the stack.
                        self.stack1.pop()
                
                if expect_b:
                    self.stack2.push(ch)
                else:
                    return False
            elif ch == "c":
                if self.stack2.is_empty():
                    return False
                else:
                    if expect_b:
                        expect_b = False
                        self.stack2.pop()
                    else:
                        self.stack2.pop()
        # At the end of the sequence, the stack must be empty,
        # otherwise we had more a's than b's.
        if self.stack1.is_empty() and self.stack2.is_empty():
            return True
        return False

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack1 = Stack()
        self.stack2 = Stack()
