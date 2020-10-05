from collections import defaultdict

class Intcode():
    """Intcode class with TEST method which includes some performance validations and
    CALCULATE which executes the complete intcode algorithm    

    Initialized with a list of computer instructions (seq)    
    """
    def __init__(self):
        self.relative_base = 0
        self.result = []
        
    def initialize_memory(self,seq):
        self.seq = seq
        self.int_dict = defaultdict(int)
        for i,v in enumerate(self.seq):
            self.int_dict[i] = int(v)
            
    def reset_memory(self):
        self.int_dict.clear()
        self.initialize_memory(self.seq)
             
    def set_pointer(self,p):
        self.pointer = p
    
    def test(self,input_instruction):
        """Intcode Test Version
        
        Parameters
        ----------
        input_intruction : list[int]
            A list of integers containing all user input instructions
        
        Returns
        -------
        None
        """
        if type(input_instruction) is not list:
            input_instruction = [input_instruction]
            
        opcode = self.int_dict[self.pointer] % 100
        while opcode != 99:
            p1, p2, p3 = self._eval_mode(opcode,self.int_dict,self.pointer)                          
            if opcode == 1:
                # addition
                self.int_dict[p3] = p1 + p2
                self.pointer += 4
            elif opcode == 2:
                # multiplication
                self.int_dict[p3] = p1 * p2
                self.pointer += 4
            elif opcode == 3:
                # takes parameter as input, if statement to manage waiting cases
                if len(input_instruction):
                    self.int_dict[p1] = input_instruction.pop(0)
                    self.pointer += 2
                else:
                    break
            elif opcode == 4:
                # output parameter value
                print(p1)
                self.pointer += 2
            elif opcode == 5:
                # jump-if-true
                self.pointer = p2 if p1 != 0 else self.pointer+3
            elif opcode == 6:
                # jump-if-false
                self.pointer = p2 if p1 == 0 else self.pointer+3
            elif opcode == 7:
                self.int_dict[p3] = 1 if p1<p2 else 0
                self.pointer += 4
            elif opcode == 8:
                self.int_dict[p3] = 1 if p1==p2 else 0
                self.pointer += 4
            elif opcode == 9:
                self.relative_base += p1
                self.pointer += 2
            # getting next opcode
            opcode = self.int_dict[self.pointer] % 100
           
    def calculate(self,input_instruction):
        """Intcode Full Version
        
        Parameters
        ----------
        input_intruction : list[int]
            A list of integers containing all user input instructions
        
        Returns
        -------
        result : int
            The final result of the calculations
        """
        if type(input_instruction) is not list:
            input_instruction = [input_instruction]
            
        self.result.clear()
        
        opcode = self.int_dict[self.pointer] % 100
        while opcode != 99:
            p1, p2, p3 = self._eval_mode(opcode,self.int_dict,self.pointer)                            
            if opcode == 1:
                # addition
                self.int_dict[p3] = p1 + p2
                self.pointer += 4
            elif opcode == 2:
                # multiplication
                self.int_dict[p3] = p1 * p2
                self.pointer += 4
            elif opcode == 3:
                # takes parameter as input, if statement to manage waiting cases
                if len(input_instruction):
                    self.int_dict[p1] = input_instruction.pop(0)
                    self.pointer += 2
                else:
                    break
            elif opcode == 4:
                # output parameter value
                self.result.append(p1)
                self.pointer += 2
            elif opcode == 5:
                # jump-if-true
                self.pointer = p2 if p1 != 0 else self.pointer+3
            elif opcode == 6:
                # jump-if-false
                self.pointer = p2 if p1 == 0 else self.pointer+3
            elif opcode == 7:
                self.int_dict[p3] = 1 if p1<p2 else 0
                self.pointer += 4
            elif opcode == 8:
                self.int_dict[p3] = 1 if p1==p2 else 0
                self.pointer += 4
            elif opcode == 9:
                self.relative_base += p1
                self.pointer += 2
            # getting next opcode
            opcode = self.int_dict[self.pointer] % 100
        # cycle is done, set -1 as out trigger
        if opcode == 99:
            self.pointer = -1
        return self.result
    
    def _eval_mode(self,op,si,p):
        """Evaluate Instruction Modes
        
        Parameters
        ----------
        op : int
            Opcode
        si : list[int]
            A list of integers containing the computer instructions
        p : int
            Current position of the pointer
        
        Returns
        -------
        p1 : int
            The value of the position or the value stored in the position indicated by the first parameter
        p2 : int
            The value of the position or the value stored in the position indicated by the second parameter 
        p3 : int
            The value of the position or the value stored in the position indicated by the third parameter 
        """
        c  = (si[p] % 1000) // 100
        b  = (si[p] % 10000) // 1000
        a  = (si[p] % 100000) // 10000 # always zero
        if op == 3:
            if c == 0:
                p1 = si[p+1]
            elif c == 1:
                p1 = p+1
            elif c == 2:
                p1 = self.relative_base + si[p+1]
            p2 = None
            p3 = None
        elif op == 4:
            if c == 0:
                p1 = si[si[p+1]]
            elif c == 1:
                p1 = si[p+1]
            elif c == 2:
                p1 = si[self.relative_base + si[p+1]]
            p2 = None
            p3 = None
        elif op == 5 or op == 6:
            if c == 0:
                p1 = si[si[p+1]]
            elif c == 1:
                p1 = si[p+1]
            elif c == 2:
                p1 = si[self.relative_base + si[p+1]]
                
            if b == 0:
                p2 = si[si[p+2]]
            elif b == 1:
                p2 = si[p+2]
            elif b == 2:
                p2 = si[self.relative_base + si[p+2]]
            p3 = None
        elif op == 9:
            if c == 0:
                p1 = si[si[p+1]]
            elif c == 1:
                p1 = si[p+1]
            elif c == 2:
                p1 = si[self.relative_base + si[p+1]]
            p2 = None
            p3 = None
        else:
            if c == 0:
                p1 = si[si[p+1]]
            elif c == 1:
                p1 = si[p+1]
            elif c == 2:
                p1 = si[self.relative_base + si[p+1]]
                
            if b == 0:
                p2 = si[si[p+2]]
            elif b == 1:
                p2 = si[p+2]
            elif b == 2:
                p2 = si[self.relative_base + si[p+2]]
                
            if a == 0:
                p3 = si[p+3]
            elif a == 1:
                p3 = si[si[p+3]]
            elif a == 2:
                p3 = self.relative_base + si[p+3]

        return [p1,p2,p3]

class Amplifier():
    """Encapsulate some methods to simulate an amplifier of a instance of the Intcode class    

    Initialized with a list of computer instructions (seq)    
    """
    def __init__(self,seq):
        self.computer = Intcode()
        self.computer.initialize_memory(seq)
        self.computer.set_pointer(0)
        
    def reset(self):
        self.computer.set_pointer(0)
        self.computer.reset_memory()
        
    def run(self, input_instruction):
        output = self.computer.calculate(input_instruction)
        return output[-1]