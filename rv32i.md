# RV32I instructions

## Format

![format](./doc/format.png)

## Opcodes

| inst[4:2]     | 000      | 001        | 010        | 011        | 100      | 101        | 110              | 111        |
| ------------- | -------- | ---------- | ---------- | ---------- | -------- | ---------- | ---------------- | ---------- |
| **inst[6:5]** |          |            |            |            |          |            |                  | **(>32b)** |
| 00            | `LOAD`   | `LOAD-FP`  | `custom-0` | `MISC-MEM` | `OP-IMM` | `AUIPC`    | `OP-IMM-32`      | **48b**    |
| 01            | `STORE`  | `STORE-FP` | `custom-1` | `AMO`      | `OP`     | `LUI`      | `OP-32`          | **64b**    |
| 10            | `MADD`   | `MSUB`     | `NMSUB`    | `NMADD`    | `OP-FP`  | `reserved` | `custom-2/rv128` | **80b**    |
| 11            | `BRANCH` | `JALR`     | `reserved` | `JAL`      | `SYSTEM` | `reserved` | `custom-3/rv128` | **>=80b**  |



## ISA

![isa](./doc/isa.png)

## isa_reformat

![isa_reformat](./doc/isa_reformat.png)
