import riscv.riscv_cte as rc


def instruction_type(opcode):
    if ((opcode == 0x37)
     or (opcode == 0x17)
     or (opcode == 0x6F)):
        inst_type = 'U'
    elif (opcode == 0x63):
        inst_type = 'B'
    elif (opcode == 0x33):
        inst_type = 'R'
    else:
        inst_type=''
    return inst_type


def u_decoding(inst):
    imm    = inst & rc.U_IMM_MASK
    rd     = inst & rc.RD_MASK
    opcode = inst & rc.OPCODE_MASK
    return imm, rd, opcode


def i_decoding(inst):
    imm    = inst & rc.I_IMM_MASK
    rs1    = inst & rc.RS1_MASK
    funct3 = inst & rc.FUNCT3_MASK
    rd     = inst & rc.RD_MASK
    opcode = inst & rc.OPCODE_MASK
    return imm, rs1, funct3, rd, opcode


def r_decoding(inst):
    funct7 = inst & rc.FUNCT7_MASK
    rs2    = inst & rc.RS2_MASK
    rs1    = inst & rc.RS1_MASK
    funct3 = inst & rc.FUNCT3_MASK
    rd     = inst & rc.RD_MASK
    opcode = inst & rc.OPCODE_MASK
    return funct7, rs2, rs1, funct3, rd, opcode


def s_decoding(inst):
    imm11  = inst & rc.S_IMM115_MASK
    rs2    = inst & rc.RS2_MASK
    rs1    = inst & rc.RS1_MASK
    funct3 = inst & rc.FUNCT3_MASK
    imm40  = inst & rc.S_IMM40_MASK
    opcode = inst & rc.OPCODE_MASK
    return imm11, rs2, rs1, funct3, imm40, opcode