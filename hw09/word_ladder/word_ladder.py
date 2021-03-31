from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, word_with_same_length):
        self.w1 = w1
        self.w2 = w2
        self.wordSet = word_with_same_length
        # a set of words with the same length
        self.queue = Queue()
        self.seen_set = set()
        # a set of words that've seen

    def initialize(self):
        """ initialize a queue containing a single stack, which contains the
            first word(w1)"""
        stack = Stack()
        stack.push(self.w1)
        self.queue.enqueue(stack)

    def make_ladder(self):
        self.initialize()
        letters = 'abcdefghigklmnopqrstuvwxyz'

        if self.w1 == self.w2:
            return None
        if (len(self.w1) != len(self.w2)):
            return None

        if self.w1 not in self.wordSet or self.w2 not in self.wordSet:
            return None

        self.seen_set.add(self.w1)

        while self.queue.isEmpty() is not True:
            # for each element in the queue
            stack = self.queue.dequeue()
            word = stack.peek()
            for i in range(len(word)):
                # for each character in the word
                for letter in letters:
                    # for each character in the alpha
                    new_word = word[:i]
                    new_word += letter
                    rest = word[i+1:]
                    new_word += rest
                    new_stack = self.add_word(new_word, stack)
                    if new_stack is not None:
                        return new_stack

    def add_word(self, new_word, stack):
        """ function to check if the new word is already seen, if not add it"""
        if new_word not in self.seen_set:
            self.seen_set.add(new_word)
            if new_word in self.wordSet:
                new_stack = stack.copy()
                new_stack.push(new_word)
                if new_word == self.w2:
                    return new_stack
                else:
                    self.queue.enqueue(new_stack)
                    return None
