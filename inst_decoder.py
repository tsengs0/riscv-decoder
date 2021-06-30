#!/usr/bin/env python3
# Instructions with opcodes
INSTR={"lui"   : {"opcode" : 0b0110111, "type" : "U", "funct3" : 0xF},
       "auipc" : {"opcode" : 0b0010111, "type" : "U", "funct3" : 0xF},
       "jal"   : {"opcode" : 0b1101111, "type" : "U", "funct3" : 0xF},

       "jalr"  : {"opcode" : 0b1100111, "type" : "I", "funct3" : 0x0},

       "beq"   : {"opcode" : 0b1100011, "type" : "B", "funct3" : 0x0},
       "bne"   : {"opcode" : 0b1100011, "type" : "B", "funct3" : 0x1}, 
       "blt"   : {"opcode" : 0b1100011, "type" : "B", "funct3" : 0x4}, 
       "bge"   : {"opcode" : 0b1100011, "type" : "B", "funct3" : 0x5}, 
       "bltu"  : {"opcode" : 0b1100011, "type" : "B", "funct3" : 0x6}, 
       "bgeu"  : {"opcode" : 0b1100011, "type" : "B", "funct3" : 0x7}, 

       "lb"    : {"opcode" : 0b0000011, "type" : "I", "funct3" : 0x0}, 
       "lh"    : {"opcode" : 0b0000011, "type" : "I", "funct3" : 0x1}, 
       "lw"    : {"opcode" : 0b0000011, "type" : "I", "funct3" : 0x2}, 
       "lbu"   : {"opcode" : 0b0000011, "type" : "I", "funct3" : 0x4}, 

       "lhu"   : {"opcode" : 0b0100011, "type" : "I", "funct3" : 0x5}, 
       "sb"    : {"opcode" : 0b0100011, "type" : "S", "funct3" : 0x0}, 
       "sh"    : {"opcode" : 0b0100011, "type" : "S", "funct3" : 0x1}, 

       "sw"    : {"opcode" : 0b0010011, "type" : "S", "funct3" : 0x2}, 
       "addi"  : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x0}, 
       "slti"  : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x2}, 
       "sltiu" : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x3}, 
       "xori"  : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x4}, 
       "ori"   : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x6}, 
       "andi"  : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x7}, 
       "slli"  : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x1}, 
       "srli"  : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x5}, 
       "srai"  : {"opcode" : 0b0010011, "type" : "I", "funct3" : 0x5}, 

       "add"   : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x0}, 
       "sub"   : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x0}, 
       "sll"   : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x1}, 
       "slt"   : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x2}, 
       "sltu"  : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x3}, 
       "xor"   : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x4}, 
       "srl"   : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x5}, 
       "sra"   : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x5}, 
       "or"    : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x6}, 
       "and"   : {"opcode" : 0b0110011, "type" : "R", "funct3" : 0x7}} 
# Masks
OPCODE_MASK   = 0x7F
U_IMM_MASK    = 0xFFFFF000
I_IMM_MASK    = 0xFFF00000
RS2_MASK      = 0x1F00000
RS1_MASK      = 0xF8000
FUNCT3_MASK   = 0x7000
FUNCT7_MASK   = 0xFE000000
RD_MASK       = 0xF80
S_IMM115_MASK = 0xFE000000
S_IMM40_MASK  = 0xF80

def instruction_type(opcode):
    if ((opcode == 0x37)
     or (opcode == 0x17)
     or (opcode == 0x6F)):
        inst_type='U'
    elif (opcode == 0x63):
        inst_type='B'
    elif (opcode == 0x33):
        inst_type='R'
    else:
        inst_type=''
    return inst_type
def u_decoding(inst):
    imm        = inst & U_IMM_MASK
    rd         = inst & RD_MASK
    opcode     = inst & OPCODE_MASK
    return imm, rd, opcode
def i_decoding(inst):
    imm    = inst & I_IMM_MASK
    rs1    = inst & RS1_MASK
    funct3 = inst & FUNCT3_MASK
    rd     = inst & RD_MASK 
    opcode = inst & OPCODE_MASK
    return imm, rs1, funct3, rd, opcode
def r_decoding(inst):
    funct7 = inst & FUNCT7_MASK
    rs2    = inst & RS2_MASK
    rs1    = inst & RS1_MASK
    funct3 = inst & FUNCT3_MASK
    rd     = inst & RD_MASK 
    opcode = inst & OPCODE_MASK
    return funct7, rs2, rs1, funct3, rd, opcode
def s_decoding(inst):
    imm11  = inst & S_IMM115_MASK
    rs2    = inst & RS2_MASK
    rs1    = inst & RS1_MASK
    funct3 = inst & FUNCT3_MASK
    imm40  = inst & S_IMM40_MASK
    opcode = inst & OPCODE_MASK
    return imm11, rs2, rs1, funct3, imm40, opcode
if __name__ == "__main__":
    # Instruction to be tested
    tested_instruction=0xc0000137
    print("Instruction: " + str(hex(tested_instruction)))
    type=instruction_type(tested_instruction & OPCODE_MASK)
    print("Type: " + type)
    if type == 'U':
        [imm,rd,opcode]=u_decoding(tested_instruction)
        print("Imm: " + str(hex(imm)))
        print("Rd: " + str(hex(rd)))
        print("Opcode: " + str(hex(opcode)))
    else:
        print("Not verified yet")