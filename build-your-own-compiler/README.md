# Compilers

- `source`: some text files written in a programming language
- `parser`: first, the text is split into a stream of tokens,
  then the parser assembles the tokens into structures (grammar)
  - `tokenizer`, `scanner`
  - `syntax tree`
- `interpreter`: simulate the program from the syntax tree
- `bytecode`: syntax tree converted into a list of instructions
  - the execution of a program works on the bytecode
- `IR`: intermediate representations

## A Simple Calculator

The first step in building a compiler or interpreter is to parse the
source code into tree structures (most parsing can be done recursively).

- S-expression: `sexpr` (type of grammar used): An `sexpr` is either a nested list in parentheses,
  or an indivisible element called an `atom`.

```
;; atom
a
123
;; list
(a)
(a b c d)
;; nested list
(a ((b) c))
;; prefix operators
(+ 1 (* 2 3))
```

## Setup

```bash
pyenv local 3.12
pip install poetry
poetry shell
```

## Test

```bash
python -m pytest
```
