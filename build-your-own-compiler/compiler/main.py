import json
import operator


def skip_space(expression: str, index: int):
    while index < len(expression) and expression[index].isspace():
        index += 1

    return index


def parse_atom(expression: str):
    try:
        return ['val', json.loads(expression)]
    except json.JSONDecodeError:
        return expression


def parse_expression(expression: str, index: int):
    index = skip_space(expression, index)

    if expression[index] == '(':
        # a list
        index += 1

        left = []

        while True:
            index = skip_space(expression, index)

            if index >= len(expression):
                raise Exception('unbalanced parenthesis')

            if expression[index] == ')':
                index += 1
                break

            index, value = parse_expression(expression, index)
            left.append(value)

        return index, left

    elif expression[index] == ')':
        raise Exception('bad parenthesis')

    else:
        # an atom
        start = index

        while index < len(expression) and (not expression[index].isspace()) and expression[index] not in '()':
            index += 1

        if start == index:
            raise Exception('empty program')

        return index, parse_atom(expression[start:index])


def pl_parse(expression: str):
    index, node = parse_expression(expression, 0)
    index = skip_space(expression, index)

    if index < len(expression):
        raise ValueError('trailing garbage')

    return node


def pl_eval(node):
    if len(node) == 0:
        raise ValueError('empty list')

    if len(node) == 2 and node[0] == 'val':
        return node[1]

    # binary operators
    binops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        'eq': operator.eq,
        'ne': operator.ne,
        'gt': operator.gt,
        'lt': operator.lt,
        'ge': operator.ge,
        'le': operator.le,
        'and': operator.and_,
        'or': operator.or_,
    }

    if len(node) == 3 and node[0] in binops:
        op = binops[node[0]]
        return op(pl_eval(node[1]), pl_eval(node[2]))

    # unary operations
    unops = {
        '-': operator.neg,
        'not': operator.not_,
    }

    if len(node) == 2 and node[0] in unops:
        op = unops[node[0]]
        return op(pl_eval(node[1]))

    # conditionals
    if len(node) == 4 and node[0] == '?':
        _, condition, yes, no = node
        if pl_eval(condition):
            return pl_eval(yes)
        else:
            return pl_eval(no)

    if node[0] == 'print':
        return print(*(pl_eval(value) for value in node[1:]))

    raise Exception('unexpected expression')
