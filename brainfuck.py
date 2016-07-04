'''

@author: wenhuizone
'''
import os

class Tape(object):  
    def __init__(self):  
        self.thetape = [0]  
        self.position = 0  
    def get(self):  
        return self.thetape[self.position]  
    def set(self, val):  
        self.thetape[self.position] = val  
    def inc(self):  
        self.thetape[self.position] += 1  
    def dec(self):  
        self.thetape[self.position] -= 1  
    def advance(self):  
        self.position += 1  
        if len(self.thetape) <= self.position:  
            self.thetape.append(0)  
    def devance(self):  
        self.position -= 1  

def mainloop(program, bracket_map):  
    pc = 0  
    tape = Tape()  
    while pc < len(program):  
        code = program[pc]  
        if code == ">":  
            tape.advance()  
        elif code == "<":  
            tape.devance()  
        elif code == "+":  
            tape.inc()  
        elif code == "-":  
            tape.dec()  
        elif code == ".":  
                # print  
            os.write(1, chr(tape.get()))  
        elif code == ",":  
                # read from stdin  
            tape.set(ord(os.read(0, 1)[0]))  
        elif code == "[" and tape.get() == 0:  
                # Skip forward to the matching ]  
            pc = bracket_map[pc]  
        elif code == "]" and tape.get() != 0:  
                # Skip back to the matching [  
            pc = bracket_map[pc]  
        pc += 1
    class Tape(object):  
        def __init__(self):  
            self.thetape = [0]  
            self.position = 0  
        def get(self):  
            return self.thetape[self.position]  
        def set(self, val):  
            self.thetape[self.position] = val  
        def inc(self):  
            self.thetape[self.position] += 1  
        def dec(self):  
            self.thetape[self.position] -= 1  
        def advance(self):  
            self.position += 1  
            if len(self.thetape) <= self.position:  
                self.thetape.append(0)  
        def devance(self):  
            self.position -= 1  

 
def parse(program):  
    parsed = []  
    bracket_map = {}  
    leftstack = []  
    pc = 0  
    for char in program:  
        if char in ('[', ']', '<', '>', '+', '-', ',', '.'):  
            parsed.append(char)  
            if char == '[':  
                leftstack.append(pc)  
            elif char == ']':  
                left = leftstack.pop()  
                right = pc  
                bracket_map[left] = right  
                bracket_map[right] = left  
            pc += 1  
          
    return "".join(parsed), bracket_map  
def run(fp):  
    program_contents = ""  
    while True:  
        read = os.read(fp, 4096)  
        if len(read) == 0:  
            break  
        program_contents += read  
    os.close(fp)  
    program, bm = parse(program_contents)  
    mainloop(program, bm)  
          
run(os.open("d:/bf/a.bf", os.O_RDONLY, 0777))    