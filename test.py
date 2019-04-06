import solver
from matplotlib import pyplot
from matplotlib import rc

if __name__ == '__main__':
    # rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    rc('text', usetex=True)

    ode = input("ode ")
    x0 = float(input("x0 "))
    y0 = float(input("y(x0) "))
    xn = float(input("xn "))
    xk = float(input("xk "))
    print(solver.toRpn(ode))
    data = solver.rungekutta(ode, x0, y0, xn, xk)

    print(data)

    x = []
    y = []

    for d in data:
        x.append(float(d['x']))
        y.append(float(d['y']))

    pyplot.title("$\\displaystyle y\'=" + solver.formula_buitifier(ode) + "$ solution", fontsize=16)
    pyplot.plot(x, y)
    pyplot.show()
