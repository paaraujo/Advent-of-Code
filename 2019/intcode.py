class Intcode():
    """Intcode class with TEST method which includes some performance validations and
    CALCULATE which executes the complete intcode algorithm    

    Initialized with a list of computer instructions (seq)    
    """
    def test(self,seqS,input_instruction):
        """Intcode Test Version
        
        Parameters
        ----------
        seqS : list[str]
            A list of strings containing the computer instructions
        input_intruction : list[int]
            A list of integers containing all user input instructions
        
        Returns
        -------
        Nothing
        """
        # initialization
        seqI = list(map(int,seqS))
        pointer = 0
        opcode = seqS[pointer][-2:]
        while opcode != '99':
            opint = int(opcode)                               
            if opint == 1:
                # addition
                p1, p2, p3 = self._eval_mode(opint,seqI,seqS,pointer)
                seqI[p3]  = p1 + p2
                seqS[p3] = str(p1 + p2)
                pointer += 4
            elif opint == 2:
                # multiplication
                p1, p2, p3 = self._eval_mode(opint,seqI,seqS,pointer)
                seqI[p3]  = p1 * p2
                seqS[p3] = str(p1 * p2)
                pointer += 4
            elif opint == 3:
                # takes parameter as input
                p1,_,_ = self._eval_mode(opint,seqI,seqS,pointer)
                try:
                    seqI[p1] = input_instruction.pop(0)
                    seqS[p1] = str(seqI[p1])
                    pointer += 2
                except AttributeError:
                    print("[ERROR] Check if the input_instruction is a list of integers.")
                    break
                except IndexError:
                    print("[ERROR] Check if the size of the input_instruction is higher than one.")
                    break
            elif opint == 4:
                # output parameter value
                p1,_,_ = self._eval_mode(opint,seqI,seqS,pointer)
                print(p1)
                pointer += 2
            # getting next opcode
            opcode = seqS[pointer][-2:]
           
    def calculate(self,seqS,input_instruction,p):
        """Intcode Full Version
        
        Parameters
        ----------
        seqS : list[str]
            A list of strings containing the computer instructions
        input_intruction : list[int]
            A list of integers containing all user input instructions
        
        Returns
        -------
        seqS : list[str]
            Input list of strings modified
        p : integer
            Pointer position
        output : int
            The final result of the calculations
        """
        # initialization
        seqI = list(map(int,seqS))
        pointer = p
        output = -1
        opcode = seqS[pointer][-2:]
        while opcode != '99':
            opint = int(opcode)                               
            if opint == 1:
                # addition
                p1, p2, p3 = self._eval_mode(opint,seqI,seqS,pointer)
                seqI[p3] = p1 + p2
                seqS[p3] = str(p1 + p2)
                pointer += 4
            elif opint == 2:
                # multiplication
                p1, p2, p3 = self._eval_mode(opint,seqI,seqS,pointer)
                seqI[p3] = p1 * p2
                seqS[p3] = str(p1 * p2)
                pointer += 4
            elif opint == 3:
                # takes parameter as input
                p1,_,_ = self._eval_mode(opint,seqI,seqS,pointer)
                 # if statement to manage waiting cases
                if len(input_instruction):
                    seqI[p1] = input_instruction.pop(0)
                    seqS[p1] = str(seqI[p1])
                    pointer += 2
                else:
                    break
            elif opint == 4:
                # output parameter value
                p1,_,_ = self._eval_mode(opint,seqI,seqS,pointer)
                output = p1
                pointer += 2
            elif opint == 5:
                # jump-if-true
                p1, p2, p3 = self._eval_mode(opint,seqI,seqS,pointer)
                pointer = p2 if p1 != 0 else pointer+3
            elif opint == 6:
                # jump-if-false
                p1, p2, p3 = self._eval_mode(opint,seqI,seqS,pointer)
                pointer = p2 if p1 == 0 else pointer+3
            elif opint == 7:
                p1, p2, p3 = self._eval_mode(opint,seqI,seqS,pointer)
                seqI[p3] = 1 if p1<p2 else 0
                seqS[p3] = str(seqI[p3])
                pointer += 4
            elif opint == 8:
                p1, p2, p3 = self._eval_mode(opint,seqI,seqS,pointer)
                seqI[p3] = 1 if p1==p2 else 0
                seqS[p3] = str(seqI[p3])
                pointer += 4
            # getting next opcode
            opcode = seqS[pointer][-2:]
        # cycle is done, set -1 as out trigger
        if opcode == '99':
            pointer = -1
        return seqS,pointer,output
    
    def _eval_mode(self,op,si,ss,p):
        """Evaluate Instruction Modes
        
        Parameters
        ----------
        op : int
            Opcode
        si : list[int]
            A list of integers containing the computer instructions
        ss : list[str]
            A list of strings containing the computer instructions
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
        c  = ss[p][-3:-2] # mode of 1st parameter
        b  = ss[p][-4:-3] # mode of 2nd parameter
        a  = ss[p][-5:-4] # mode of 3rd parameter // always zero
        if op == 3:
            p1 = p+1 if c == '1' else si[p+1]
            p2 = None
            p3 = None
        elif op == 4:
            p1 = si[p+1] if c == '1' else si[si[p+1]]
            p2 = None
            p3 = None
        elif op == 5 or op == 6:
            p1 = si[p+1] if c == '1' else si[si[p+1]]
            p2 = si[p+2] if b == '1' else si[si[p+2]]
            p3 = None
        else:   
            p1 = si[p+1] if c == '1' else si[si[p+1]]
            p2 = si[p+2] if b == '1' else si[si[p+2]] 
            p3 = si[si[p+3]] if a == '1' else si[p+3]
        return [p1,p2,p3]

class Amplifier():
    """Encapsulate some methods to simulate an amplifier of a instance of the Intcode class    

    Initialized with a list of computer instructions (seq)    
    """
    def __init__(self,seq):
        """ Initialization of class
        Parameters
        ----------
        seq : list[str]
            A list of strings containing the computer instructions
        
        Returns
        -------
        None
        """
        # position where the intcode should start reading values of the working_list
        self.pointer = 0 
        # backup of the initialization list
        self.original_seq = seq
        # runtime list of computer instructions
        self.working_seq  = list(seq)
    def reset(self):
        """ Reset of both pointer and list of computer instructions
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.pointer = 0
        self.working_seq = list(self.original_seq)
    def run(self, input_instruction):
        """ Reset of both pointer and list of computer instructions
        Parameters
        ----------
        None
        
        Returns
        -------
        Result of the calculations
        """
        computer = Intcode()
        self.working_seq,self.pointer,output = computer.calculate(self.working_seq,input_instruction,self.pointer)
        return output