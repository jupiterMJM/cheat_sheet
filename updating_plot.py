import pyqtgraph as pg
# if you want to see full examples of pyqgraph module: enter "python -m pyqtgraph.examples" in your cmd
import random as rd
from pyqtgraph.Qt import QtCore


win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

# then we create the random data
datas = [rd.randint(1, 100) for i in range(100)]

# and we add a plotItem to the window
p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen="red")  # color the plot (the background is automatically black

indic = 10
def repet():
    """
    the function that "actualise" the data you see on the screen
    """
    global curve, indic, p6, datas
    curve.setData(datas[:indic % 100])
    indic += 1

# the final part: the timer: every time your "timer" clicks, it launches your function repet()
timer = QtCore.QTimer()
timer.timeout.connect(repet)
timer.start(1000)  # in ms

if __name__ == '__main__':
    pg.exec()
