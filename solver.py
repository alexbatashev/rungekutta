import re
import math
from decimal import Decimal

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
        return math.log(Decimal(pure))
    elif "sin" in str(arg):
        pure = arg.replace("sin[", "")
        pure = pure.replace("]", "")
        return math.sin(Decimal(pure))
    elif "cos" in str(arg):
        pure = arg.replace("cos[", "")
        pure = pure.replace("]", "")
        return math.sin(Decimal(pure))
    else:
        return arg


def eval(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = expand_arg(stack.pop())
            arg1 = expand_arg(stack.pop())
            result = ops[token](Decimal(arg1), Decimal(arg2))
            stack.append(str(result))
        else:
            stack.append(str(token))

    return float(stack.pop())


def rungekutta(expr, x0, y0, xn, xk):
    rpnexpr = toRpn(expr)
    h = 0.02
    k = abs(xk - x0) / h
    n = abs(xn - x0) / h

    res = [{'x': x0, 'y': y0}]
    res_neg = [{'x': x0, 'y': y0}]

    for i in range(1, math.ceil(k)):
        cexpr = rpnexpr.replace('x', str(res[i-1]['x']))
        cexpr = cexpr.replace('y', str(res[i-1]['y']))
        f = h * eval(cexpr)
        ty = res[i-1]['y'] + f
        x = h + res[i-1]['x']
        cexpr = rpnexpr.replace('x', str(x))
        cexpr = cexpr.replace('y', str(ty))
        y = res[i-1]['y'] + h * (f + eval(cexpr)) / 2
        res.append({'x': x, 'y': y})

    h = -h

    for i in range(1, math.ceil(n)):
        cexpr = rpnexpr.replace('x', str(res_neg[i-1]['x']))
        cexpr = cexpr.replace('y', str(res_neg[i-1]['y']))
        f = h * eval(cexpr)
        ty = res_neg[i-1]['y'] + f
        x = res_neg[i-1]['x'] + h
        cexpr = rpnexpr.replace('x', str(x))
        cexpr = cexpr.replace('y', str(ty))
        y = res_neg[i-1]['y'] + h * (f + eval(cexpr)) / 2
        res_neg.append({'x': x, 'y': y})

    res_neg = res_neg[1:]
    res_neg = res_neg[::-1]
    res_neg.extend(res)

    return res_neg
