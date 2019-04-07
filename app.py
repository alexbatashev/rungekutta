import sys

from PyQt5.QtWidgets import QSizePolicy


import mainwindow
from PyQt5 import QtWidgets
import solver
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import rc


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.ode = None
        self.data = None
        self.X = None
        self.Y = None
        self.dX = None
        self.dY = None
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.imrk = fig.subplots()
        # self._timer = self.new_timer(
        #     100, [(self._update_canvas, (), {})])
        # self._timer.start()

    def setResult(self, data, ode, X, Y, dX, dY):
        self.ode = ode
        self.data = data
        self.X = X
        self.Y = Y
        self.dX = dX
        self.dY = dY

    def update_canvas(self):
        if self.ode is not None:
            rc('text', usetex=True)
            self.imrk.clear()
            self.imrk.plot(self.data[0], self.data[1], 'r-')
            self.imrk.plot(self.data[2], self.data[3], 'b-')
            self.figure.suptitle("$\\displaystyle y\'=" + solver.formula_buitifier(self.ode) + "$")
            self.imrk.quiver(self.X, self.Y, self.dX, self.dY)
        self.draw()
        self.repaint()


class ExampleApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.plot = PlotCanvas(self, width=6, height=5)
        self.plot.move(90, 50)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        ode = str(self.ode.toPlainText())
        x0 = float(self.x0.toPlainText())
        y0 = float(self.y0.toPlainText())
        xn = float(self.xn.toPlainText())
        xk = float(self.xk.toPlainText())

        res, ymin, ymax = solver.rungekutta(ode, x0, y0, xn, xk)
        res2, ymin2, ymax2 = solver.rk4(ode, x0, y0, xn, xk)

        X, Y, dX, dY = solver.slope_field(ode, xn, xk, min(ymin, ymin2), max(ymax, ymax2))

        data = [[], [], [], []]

        for d in res:
            data[0].append(float(d['x']))
            data[1].append(float(d['y']))
        for d in res2:
            data[2].append(float(d['x']))
            data[3].append(float(d['y']))
        self.plot.setResult(data, ode, X, Y, dX, dY)
        self.plot.update_canvas()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
