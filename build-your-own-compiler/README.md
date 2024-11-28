# Compilers

- source: some text files written in a programming language
- parser: first, the text is split into a stream of tokens,
  then the parser assembles the tokens into structures (grammar)
  - tokenizer, scanner
  - syntax tree
- interpreter: simulate the program from the syntax tree
- bytecodes: syntax tree converted into a list of instructions
  - the execution of a program works on the bytecode
- IR: intermediate representations