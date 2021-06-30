#!/usr/bin/env python3
import riscv.riscv_cte as rc
import riscv.riscv_func as rf

if __name__ == "__main__":
    # Instruction to be tested: lui x2, 0xc0000000
    tested_instruction = 0xc0000137
    inst_type = rf.instruction_type(tested_instruction & rc.OPCODE_MASK)
    rf.instruction_parsing(inst_type,
                           tested_instruction)
    