def eval_mode(op,si,ss,p):
    '''op = opcode \n si = list of integers \n ss = list of string \n p  = pointer position'''
    c  = ss[p][-3:-2] # mode of 1st parameter
    b  = ss[p][-4:-3] # mode of 2nd parameter
    a  = ss[p][-5:-4] # mode of 3rd parameter // always zero
    if op == 4:
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
    return [c,b,a,p1,p2,p3]
    
def part1(input_instruction):
    with open('inputs/day5.txt') as f:
        seq = f.read()
        seqS = seq.split(',')
        seq = list(map(int,seqS))
        # initialization
        cont = 0
        opcode = seqS[cont][-2:]
        while opcode != '99':
            opint = int(opcode)                               
            if opint == 1:
                # addition
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                seq[p3]  = p1 + p2
                seqS[p3] = str(p1 + p2)
                cont += 4
            elif opint == 2:
                # multiplication
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                seq[p3]  = p1 * p2
                seqS[p3] = str(p1 * p2)
                cont += 4
            elif opint == 3:
                # takes parameter as input
                seq[seq[cont+1]]  = input_instruction
                seqS[seq[cont+1]] = str(input_instruction)
                cont += 2
            elif opint == 4:
                # output parameter value
                print(seq[seq[cont+1]])
                cont += 2
            # getting next opcode
            opcode = seqS[cont][-2:]

def part2(input_instruction):
    with open('inputs/day5.txt') as f:
        seq = f.read()
        seqS = seq.split(',')
        seq = list(map(int,seqS))
        # initialization
        cont = 0
        opcode = seqS[cont][-2:]
        while opcode != '99':
            opint = int(opcode)                               
            if opint == 1:
                # addition
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                seq[p3]  = p1 + p2
                seqS[p3] = str(p1 + p2)
                cont += 4
            elif opint == 2:
                # multiplication
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                seq[p3]  = p1 * p2
                seqS[p3] = str(p1 * p2)
                cont += 4
            elif opint == 3:
                # takes parameter as input
                seq[seq[cont+1]]  = input_instruction
                seqS[seq[cont+1]] = str(input_instruction)
                cont += 2
            elif opint == 4:
                # output parameter value
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                print(p1)
                cont += 2
            elif opint == 5:
                # jump-if-true
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                cont = p2 if p1 != 0 else cont+3
            elif opint == 6:
                # jump-if-false
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                cont = p2 if p1 == 0 else cont+3
            elif opint == 7:
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                seq[p3] = 1 if p1<p2 else 0
                seqS[p3] = str(seq[p3])
                cont += 4
            elif opint == 8:
                c, b, a, p1, p2, p3 = eval_mode(opint,seq,seqS,cont)
                seq[p3] = 1 if p1==p2 else 0
                seqS[p3] = str(seq[p3])
                cont += 4
            # getting next opcode
            opcode = seqS[cont][-2:]

part1(1)
part2(5)