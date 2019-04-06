import unittest
import solver


class TestSolver(unittest.TestCase):

    def test_eval_simple(self):
        rpn = solver.toRpn("5*x+y")
        rpn = rpn.replace('x', '2')
        rpn = rpn.replace('y', '4')
        res = solver.eval(rpn)
        assert abs(res - 14) < 0.001

    def test_eval_square(self):
        rpn = solver.toRpn("x^2")
        rpn = rpn.replace('x', '2')
        res = solver.eval(rpn)
        assert abs(res - 4) < 0.001

    def test_eval_div(self):
        rpn = solver.toRpn("x/2")
        rpn = rpn.replace('x', '8')
        res = solver.eval(rpn)
        assert abs(res - 4) < 0.001

    def test_eval_complex(self):
        rpn = solver.toRpn("x*y + x / 2")
        rpn = rpn.replace('x', '2')
        rpn = rpn.replace('y', '5')
        res = solver.eval(rpn)
        assert abs(res - 11) < 0.001


if __name__ == '__main__':
    unittest.main()
