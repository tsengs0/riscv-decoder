# A simple RISC-V decoder

This idea of this tool is just to decode/parse a given instruction. In others words, given the hexadecimal representation of an instruction, it prints all fields of the instruction.

## Features

- [ ] RV32I support
  - [x] U type
  - [x] R type
  - [x] I type
  - [x] S type
  - [x] B type
  - [x] J type
- [ ] Support of other instruction extensions

## Known issues

Instructions are first parsed to their opcode, which is not the best option:

```python
"lhu": {"opcode": 0b0100011, "type": "I", "funct3": 0x5},
"sb":  {"opcode": 0b0100011, "type": "S", "funct3": 0x0},
"sh":  {"opcode": 0b0100011, "type": "S", "funct3": 0x1},
```

`lhu`, `sb` and `sh` share the same opcode while having two different types: this case isn't processed yet. In other words, the decoder works only when the opcode is specific to a type.

- However comparing both `opcode` and `funct3` should work.
- Ideas in these hardware implementations:
  - https://github.com/BrunoLevy/learn-fpga/blob/master/FemtoRV/RTL/PROCESSOR/femtorv32_electron.v
  - https://github.com/cliffordwolf/picorv32/blob/master/picorv32.v#L644

## Documentation

- Instructions are listed in the official documentation release: https://github.com/riscv/riscv-isa-manual/releases (chapter 23)
- Details for [RV32I](./rv32i.md)
- Do [not look at this decoder before I code mine](https://github.com/jck/riscv)
