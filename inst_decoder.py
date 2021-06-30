#!/usr/bin/env python3
import riscv.riscv_cte as rc
import riscv.riscv_func as rf

if __name__ == "__main__":
    # Instruction to be tested: lui x2, 0xc0000000
    tested_instruction = 0xc0000137
    print("Instruction: " + str(hex(tested_instruction)))
    type=rf.instruction_type(tested_instruction & rc.OPCODE_MASK)
    print("Type: " + type)
    if type == 'U':
        [imm, rd, opcode] = rf.u_decoding(tested_instruction)
        print("Imm: " + str(hex(imm)))
        print("Rd: " + str(hex(rd)))
        print("Opcode: " + str(hex(opcode)))
    else:
        print("Not verified yet")
