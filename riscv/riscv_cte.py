# Instructions with opcodes
INSTR = {"lui":  {"opcode": 0b0110111, "type": "U", "funct3": 0xF},
        "auipc": {"opcode": 0b0010111, "type": "U", "funct3": 0xF},
        "jal":   {"opcode": 0b1101111, "type": "U", "funct3": 0xF},

        "jalr":  {"opcode": 0b1100111, "type": "I", "funct3": 0x0},

        "beq":   {"opcode": 0b1100011, "type": "B", "funct3": 0x0},
        "bne":   {"opcode": 0b1100011, "type": "B", "funct3": 0x1},
        "blt":   {"opcode": 0b1100011, "type": "B", "funct3": 0x4},
        "bge":   {"opcode": 0b1100011, "type": "B", "funct3": 0x5},
        "bltu":  {"opcode": 0b1100011, "type": "B", "funct3": 0x6},
        "bgeu":  {"opcode": 0b1100011, "type": "B", "funct3": 0x7},

        "lb":    {"opcode": 0b0000011, "type": "I", "funct3": 0x0},
        "lh":    {"opcode": 0b0000011, "type": "I", "funct3": 0x1},
        "lw":    {"opcode": 0b0000011, "type": "I", "funct3": 0x2},
        "lbu":   {"opcode": 0b0000011, "type": "I", "funct3": 0x4},

        "lhu":   {"opcode": 0b0000011, "type": "I", "funct3": 0x5},
        "sb":    {"opcode": 0b0100011, "type": "S", "funct3": 0x0},
        "sh":    {"opcode": 0b0100011, "type": "S", "funct3": 0x1},

        "sw":    {"opcode": 0b0100011, "type": "S", "funct3": 0x2},
        "addi":  {"opcode": 0b0010011, "type": "I", "funct3": 0x0},
        "slti":  {"opcode": 0b0010011, "type": "I", "funct3": 0x2},
        "sltiu": {"opcode": 0b0010011, "type": "I", "funct3": 0x3},
        "xori":  {"opcode": 0b0010011, "type": "I", "funct3": 0x4},
        "ori":   {"opcode": 0b0010011, "type": "I", "funct3": 0x6},
        "andi":  {"opcode": 0b0010011, "type": "I", "funct3": 0x7},
        "slli":  {"opcode": 0b0010011, "type": "I", "funct3": 0x1},
        "srli":  {"opcode": 0b0010011, "type": "I", "funct3": 0x5},
        "srai":  {"opcode": 0b0010011, "type": "I", "funct3": 0x5},

        "add":   {"opcode": 0b0110011, "type": "R", "funct3": 0x0},
        "sub":   {"opcode": 0b0110011, "type": "R", "funct3": 0x0},
        "sll":   {"opcode": 0b0110011, "type": "R", "funct3": 0x1},
        "slt":   {"opcode": 0b0110011, "type": "R", "funct3": 0x2},
        "sltu":  {"opcode": 0b0110011, "type": "R", "funct3": 0x3},
        "xor":   {"opcode": 0b0110011, "type": "R", "funct3": 0x4},
        "srl":   {"opcode": 0b0110011, "type": "R", "funct3": 0x5},
        "sra":   {"opcode": 0b0110011, "type": "R", "funct3": 0x5},
        "or":    {"opcode": 0b0110011, "type": "R", "funct3": 0x6},
        "and":   {"opcode": 0b0110011, "type": "R", "funct3": 0x7}}
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
