#!/usr/bin/env python3
import riscv.riscv_cte as rc
import riscv.riscv_func as rf

if __name__ == "__main__":
    # lui x2, 0xc0000000
    print("-----")
    print("lui x2, 0xc0000000")
    tested_instruction = 0xc0000137
    inst_type = rf.instruction_type(tested_instruction & rc.OPCODE_MASK)
    rf.instruction_parsing(inst_type,
                           tested_instruction)
    # sb x3, 0(x2)
    print("-----")
    print("sb x3, 0(x2)")
    tested_instruction = 0x00310023
    inst_type = rf.instruction_type(tested_instruction & rc.OPCODE_MASK)
    rf.instruction_parsing(inst_type,
                           tested_instruction)

    # addi x1, x0, 32 - Type KO
    print("-----")
    print("addi x1, x0, 32")
    tested_instruction = 0x02000093
    inst_type = rf.instruction_type(tested_instruction & rc.OPCODE_MASK)
    rf.instruction_parsing(inst_type,
                           tested_instruction)

    # beq x3, x0, +16 - Type OK / decoding KO
    print("-----")
    print("beq x3, x0, +16")
    tested_instruction = 0x00018863
    inst_type = rf.instruction_type(tested_instruction & rc.OPCODE_MASK)
    rf.instruction_parsing(inst_type,
                           tested_instruction)