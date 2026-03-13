### I think these two methods(actually same method) can only worked when there is no more '[' after the first ']'
def decode_string(string):
    num_stack, str_stack = Stack(), Stack()
    current_string, num_string = '', ''
    for char in string:
        if char.isdigit():
            num_string += char
        elif char.isalpha():
            current_string += char
        elif char == '[': #'[' is a sign that the strings should be refreshed
            str_stack.push(current_string)
            num_stack.push(int(num_string))
            current_string, num_string = '', ''
        else: # here, else is just "]", this is a sign that the string can be updated
            current_string = str_stack.pop() + current_string * num_stack.pop()
            #here, I firstly worried about: what if the str_stack or the num_stack is empty?
            # but the thing is, str_stack won't be empty untill every step has been done
            # what about num_stack? also won't be empty as well, however, in some cases, the bottom element in num_stack may be an empt string, hence, using repeat = repeat * 10 + int(char) is much safer
    return current_string


def decode_string(string):
    num_stack, str_stack = Stack(), Stack()
    curr, repeat = '', 0
    for char in string:
        if char.isdigit():
            repeat = 10 * repeat + int(char) # this is a magical method to store the repeat number,  replacing my anothr answer's 'num_string', and this is more obvious. This is the only differencebetween the two methods
        elif char.isalpha():
            curr += char
        elif char == '[':
            str_stack.push(curr)
            num_stack.push(repeat)
            curr, repeat = '', 0
        else:
            curr = str_stack.pop() + curr * num_stack.pop()
    return curr


# the following method comes from Leon, he uses only one stack to solve this problem
def decode_string(string):
    a_stack = Stack()
    w, num = '', ''
    for char in string:
        if char.isalpha() or char.isdigit() or char == '[':
            a_stack.push(char)
        else:# the emphasis is when char == ']'
            w = ''
            while not a_stack.is_empty() and not a_stack.peek() == '[':
                w = a_stack.pop() + w
            a_stack.pop() # remove the top '['
            num = ''
            while not a_stack.is_empty() and a_stack.peek().isdigit():
                num = a_stack.pop() + num
            w = w * int(num)
            a_stack.push(w)
    w = ''
    while not a_stack.is_empty():
        w = a_stack.pop() + w
    return w
            

#接下来是一个I don't understand my logic right now不知道自己that time在叽里呱啦写啥
def decode_string(string): #instant = instant + str_stack.pop()
    str_stack, num_stack = Stack(), Stack()
    for char in string:
        if char.isdigit():
            num_stack.push(char)
        elif char == '[':
            str_stack.push(char)
            num_stack.push(char)
        elif char.isalpha():
            str_stack.push(char)
        else:
            instant = ''
            while (not str_stack.is_empty()) and str_stack.peek() != '[':
                instant = str_stack.pop() + instant
            if not str_stack.is_empty() and str_stack.peek() == '[':
                str_stack.pop() #add instant string in stack
 
            num = ''
            if not num_stack.is_empty() and num_stack.peek() == '[':
                num_stack.pop()
            while not num_stack.is_empty() and num_stack.peek().isdigit():
                num = num_stack.pop() + num
            num = 1 if num == '' else int(num)
            str_stack.push(instant * int(num))
            
    ans = ''
    while not str_stack.is_empty():
        ans = str_stack.pop() + ans
    return ans
        