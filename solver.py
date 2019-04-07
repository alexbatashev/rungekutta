import re
import math
# from decimal import Decimal
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy.printing.theanocode import theano_function
from sympy.abc import x
from sympy.abc import y
# import sympy.abc
from sympy import *
import theano

ops = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b),
    "^": (lambda a, b: a ** b)
}


def formula_buitifier(formula):
    res = formula.replace('*', '')
    res = res.replace('log', '\\log')
    res = res.replace('sin', '\\sin')
    res = res.replace('cos', '\\cos')
    res = res.replace('[', '{')
    res = res.replace(']', '}')
    return res


def toRpn(infixStr):
    # divide string into tokens, and reverse so I can get them in order with pop()
    tokens = re.split(r' *([+\-*^/]) *', infixStr)
    tokens = [t for t in reversed(tokens) if t != '']
    precs = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}

    # convert infix expression tokens to RPN, processing only
    # operators above a given precedence
    def toRpn2(tokens, minprec):
        rpn = tokens.pop()
        while len(tokens) > 0:
            prec = precs[tokens[-1]]
            if prec < minprec:
                break
            op = tokens.pop()

            # get the argument on the operator's right
            # this will go to the end, or stop at an operator
            # with precedence <= prec
            arg2 = toRpn2(tokens, prec + 1)
            rpn += " " + arg2 + " " + op
        return rpn

    return toRpn2(tokens, 0)


def expand_arg(arg):
    if "log" in str(arg):
        pure = arg.replace("log[", "")
        pure = pure.replace("]", "")
        return np.log(np.float64(pure))
    elif "sin" in str(arg):
        pure = arg.replace("sin[", "")
        pure = pure.replace("]", "")
        return np.sin(np.float64(pure))
    elif "cos" in str(arg):
        pure = arg.replace("cos[", "")
        pure = pure.replace("]", "")
        return np.sin(np.float64(pure))
    else:
        return arg


def eval_rpn(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = expand_arg(stack.pop())
            arg1 = expand_arg(stack.pop())
            result = ops[token](np.float64(arg1), np.float64(arg2))
            stack.append(str(result))
        else:
            stack.append(str(token))

    return float(expand_arg(stack.pop()))


def rungekutta(raw_expr, x0, y0, xn, xk):
    raw_expr = raw_expr.replace('^', "**")
    if "x" not in raw_expr:
        raw_expr += "+ 0*x"
    if "y" not in raw_expr:
        raw_expr += "+ 0*y"
    ev_expr = parse_expr(raw_expr, evaluate=0)
    print(ev_expr)
    f = theano_function([x, y], [ev_expr])
    print(f)

    # rpnexpr = toRpn(expr)
    h = abs(xk - xn) / 500
    k = abs(xk - x0) / h
    n = abs(xn - x0) / h

    res = [{'x': x0, 'y': y0}]
    res_neg = [{'x': x0, 'y': y0}]

    for i in range(1, math.ceil(k)):
        fv = h * f(res[i - 1]['x'], res[i - 1]['y'])
        ty = res[i - 1]['y'] + fv
        tx = h + res[i - 1]['x']
        yn1 = res[i - 1]['y'] + h * (fv + f(tx, ty)) / 2
        res.append({'x': tx, 'y': yn1})

    h = -h

    for i in range(1, math.ceil(n)):
        fv = h * f(res_neg[i - 1]['x'], res_neg[i - 1]['y'])
        ty = res_neg[i - 1]['y'] + fv
        tx = h + res_neg[i - 1]['x']
        yn1 = res_neg[i - 1]['y'] + h * (fv + f(tx, ty)) / 2
        res_neg.append({'x': tx, 'y': yn1})

    res_neg = res_neg[1:]
    res_neg = res_neg[::-1]
    res_neg.extend(res)

    return res_neg
