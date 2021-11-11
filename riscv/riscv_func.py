import riscv.riscv_cte as rc

def instruction_type(opcode):
    if ((opcode == 0x37)
     or (opcode == 0x17)
     or (opcode == 0x6F)):
        inst_type = 'U'
    elif opcode == 0x63:
        inst_type = 'B'
    elif opcode == 0x33:
        inst_type = 'R'
    elif opcode == 0x23:
        inst_type = 'S'
    elif opcode == 0x13:
        inst_type = 'I'
    else:
        raise Exception('Unknown type with opcode = '+str(hex(opcode)))
    return inst_type


def u_decoding(inst):
    imm    = (inst & rc.U_IMM_MASK) >> 12
    rd     = (inst & rc.RD_MASK)    >> 7
    opcode = inst & rc.OPCODE_MASK
    return imm, rd, opcode


def i_decoding(inst):
    imm    = (inst & rc.I_IMM_MASK)  >> 20
    rs1    = (inst & rc.RS1_MASK)    >> 15
    funct3 = (inst & rc.FUNCT3_MASK) >> 12
    rd     = (inst & rc.RD_MASK)     >> 7
    opcode = inst & rc.OPCODE_MASK
    return imm, rs1, funct3, rd, opcode


def r_decoding(inst):
    funct7 = (inst & rc.FUNCT7_MASK) >> 25
    rs2    = (inst & rc.RS2_MASK)    >> 20
    rs1    = (inst & rc.RS1_MASK)    >> 15
    funct3 = (inst & rc.FUNCT3_MASK) >> 12
    rd     = (inst & rc.RD_MASK)     >> 7
    opcode = inst & rc.OPCODE_MASK
    return funct7, rs2, rs1, funct3, rd, opcode


def s_decoding(inst):
    imm11  = (inst & rc.S_IMM115_MASK) >> 25
    rs2    = (inst & rc.RS2_MASK)      >> 20
    rs1    = (inst & rc.RS1_MASK)      >> 15
    funct3 = (inst & rc.FUNCT3_MASK)   >> 12
    imm40  = (inst & rc.S_IMM40_MASK)  >> 7
    opcode = inst & rc.OPCODE_MASK
    return imm11, rs2, rs1, funct3, imm40, opcode


def instruction_parsing(inst_type,tested_instruction):
    print("Instruction: " + str(hex(tested_instruction)))
    print("Type: " + inst_type)
    if inst_type == 'U':
        [imm, rd, opcode] = u_decoding(tested_instruction)
        print('[imm, rd, opcode]')
        print('[{}]'.format(', '.join(hex(x) for x in [imm, rd, opcode])))
    elif inst_type == 'I':
        [imm, rs1, funct3, rd, opcode] = i_decoding(tested_instruction)
        print('[imm, rs1, funct3, rd, opcode]')
        print('[{}]'.format(', '.join(hex(x) for x in [imm, rs1, funct3, rd, opcode])))
    elif inst_type == 'R':
        [funct7, rs2, rs1, funct3, rd, opcode] = r_decoding(tested_instruction)
        print('[funct7, rs2, rs1, funct3, rd, opcode]')
        print('[{}]'.format(', '.join(hex(x) for x in [funct7, rs2, rs1, funct3, rd, opcode])))
    elif inst_type == 'S':
        [imm11, rs2, rs1, funct3, imm40, opcode] = s_decoding(tested_instruction)
        print('[imm11, rs2, rs1, funct3, imm40, opcode]')
        print('[{}]'.format(', '.join(hex(x) for x in [imm11, rs2, rs1, funct3, imm40, opcode])))
    else:
        raise Exception("Not decoded yet")