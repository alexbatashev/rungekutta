import random
import sys

from PyQt5.QtWidgets import QSizePolicy

import mainwindow
from PyQt5 import QtWidgets
import solver
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.ode = None
        self.data = None
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self._dynamic_ax = fig.subplots()
        self._timer = self.new_timer(
            100, [(self._update_canvas, (), {})])
        self._timer.start()

    def setResult(self, data, ode):
        self.ode = ode
        self.data = data

    def _update_canvas(self):
        # data = [random.random() for i in range(25)]
        if self.ode is not None:
            self._dynamic_ax.plot(self.data[0], self.data[1])
            self._dynamic_ax.set_title(self.ode)
        # ax.plot(data, 'r-')
        # ax.set_title('PyQt Matplotlib Example')
        self.draw()


class ExampleApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.plot = PlotCanvas(self, width=5, height=4)
        self.plot.move(80, 50)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        ode = str(self.ode.toPlainText())
        x0 = float(self.x0.toPlainText())
        y0 = float(self.y0.toPlainText())
        xn = float(self.xn.toPlainText())
        xk = float(self.xk.toPlainText())

        res = solver.rungekutta(ode, x0, y0, xn, xk)

        data = [[], []]

        for d in res:
            data[0].append(float(d['x']))
            data[1].append(float(d['y']))
        self.plot.setResult(data, ode)
        self.plot.repaint()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
