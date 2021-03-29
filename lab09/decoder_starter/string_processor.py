from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        self.name = ''

    def process_string(self, input):
        """reading from left to right,
            *: pop the stack and append it to the solution string
            ^: 2 characters are popped from the stack and append it"""
        st = Stack()
        input_message = str(input)
        output_string = ''
        for c in input_message:
            if(c == '*'):
                pop = st.pop()
                if(pop is not None):
                    output_string += pop
            elif(c == '^'):
                pop = st.pop()
                pop2 = st.pop()
                if(pop is not None):
                    output_string += pop
                    output_string += pop2
            else:
                st.push(c)
        return output_string
