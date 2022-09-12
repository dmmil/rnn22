from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal
import numpy as np

class GraphScene(QtWidgets.QGraphicsScene):

    signalDrawed = pyqtSignal()

    def __init__(self, Lr_index, L, M, d, q, route):
        super().__init__()

        self.Lr_index = Lr_index
        self.L = L
        self.M = M
        self.d = d
        self.q = q
        self.route = route

        self.matrix = np.zeros((2, L, M, d, q), dtype=np.int8)

        self.brush_lightgray = QtGui.QBrush(QtGui.QColor(0xcf, 0xcf, 0xcf))
        self.brush_gray = QtGui.QBrush(QtGui.QColor(0x71, 0x71, 0x71))
        self.brush_black = QtGui.QBrush(QtGui.QColor(0x00, 0x00, 0x00))
        self.brush_white = QtGui.QBrush(QtGui.QColor(0xff, 0xff, 0xff))

        self.pen_black = QtGui.QPen(QtGui.QColor(0x00, 0x00, 0x00))

        self.pixelSize_wigth = self.M * self.q * 10
        self.pixelSize_height = self.L * self.d * 10
        self.setSceneRect(0, 0, self.pixelSize_wigth, self.pixelSize_height)
        self.setBackgroundBrush(self.brush_lightgray)

        # определяем начальные координаты и размеры рамки исходя из конфигурации сети
        self.x_start = self.pixelSize_wigth*0.05
        self.y_start = self.pixelSize_height*0.05
        self.X_SIZE = self.pixelSize_wigth*0.9
        self.Y_SIZE = self.pixelSize_height*0.9
        self.m_gap = 0.02 * self.X_SIZE / self.M
        self.l_gap = 0.02 * self.Y_SIZE / self.L
        self.m_width = self.X_SIZE / self.M - self.m_gap * 2
        self.l_width = self.Y_SIZE / self.L - self.l_gap * 2
        self.q_gap = 0.1 * self.m_width / self.q
        self.d_gap = 0.1 * self.l_width / self.d
        self.q_width = self.m_width / self.q - self.q_gap * 2
        self.d_width = self.l_width / self.d - self.d_gap * 2

        self.coord_x = 0
        self.coord_y = 0

        self.clearGraphic()

    def clearGraphic(self):

        if self.M*self.L*self.q*self.d == 0:
            print("M_DIM*L_DIM*q_SIZ*d_SIZ == 0")
            return

        self.clear()

        self.setSceneRect(0, 0, self.pixelSize_wigth, self.pixelSize_height)

        # # определяем начальные координаты и размеры рамки исходя из конфигурации сети
        # x_start = self.pixelSize_wigth*0.05
        # y_start = self.pixelSize_height*0.05
        # X_SIZE = self.pixelSize_wigth*0.9
        # Y_SIZE = self.pixelSize_height*0.9

        # добавляем главную рамку
        self.addRect(self.x_start, self.y_start, self.X_SIZE, self.Y_SIZE)

        # цикл по полям РНС
        for il in range(self.L):
            for im in range(self.M):
                # определяем начальные координаты и размеры поля исходя из координат M и L
                # m_gap = 0.02*self.X_SIZE/self.M
                # l_gap = 0.02*self.Y_SIZE/self.L
                # m_width = self.X_SIZE/self.M-m_gap*2
                # l_width = self.Y_SIZE/self.L-l_gap*2
                m_start = self.x_start+im*self.X_SIZE/self.M+self.m_gap
                l_start = self.y_start+il*self.Y_SIZE/self.L+self.l_gap


                # добавляем локальную рамку поля
                self.addRect(self.x_start+im*self.X_SIZE/self.M, self.y_start+il*self.Y_SIZE/self.L,
                             self.X_SIZE/self.M, self.Y_SIZE/self.L, self.pen_black, self.brush_white)

                # цикл по нейронам в поле
                for id in range(self.d):
                    for iq in range(self.q):

                        # определяем начальные координаты и размеры нейрона исходя из координат q и d
                        # q_gap = 0.1*self.m_width/self.q
                        # d_gap = 0.1*self.l_width/self.d
                        # q_width = self.m_width/self.q-q_gap*2
                        # d_width = self.l_width/self.d-d_gap*2
                        q_start = m_start+iq*self.m_width/self.q+self.q_gap
                        d_start = l_start+id*self.l_width/self.d+self.d_gap

                        self.addEllipse(q_start, d_start, self.q_width, self.d_width, self.pen_black, self.brush_white)

    def drawGraphic(self, vals):

        if type(vals) == np.ndarray:
            # значит это не изменение масштаба, а именно новые данные
            for item in self.route:
                self.matrix[item['Lr'], item['L'], item['M'], :, :] = vals[self.route.index(item)]

        if self.M*self.L*self.q*self.d == 0:
            print("M_DIM*L_DIM*q_SIZ*d_SIZ == 0")
            return

        self.clear()

        self.setSceneRect(0, 0, self.pixelSize_wigth, self.pixelSize_height)

        # # определяем начальные координаты и размеры рамки исходя из конфигурации сети
        # x_start = self.pixelSize_wigth*0.05
        # y_start = self.pixelSize_height*0.05
        # X_SIZE = self.pixelSize_wigth*0.9
        # Y_SIZE = self.pixelSize_height*0.9

        # добавляем главную рамку
        self.addRect(self.x_start, self.y_start, self.X_SIZE, self.Y_SIZE)

        # цикл по полям РНС
        for il in range(self.L):
            for im in range(self.M):
                # определяем начальные координаты и размеры поля исходя из координат M и L
                # m_gap = 0.02*self.X_SIZE/self.M
                # l_gap = 0.02*self.Y_SIZE/self.L
                # m_width = self.X_SIZE/self.M-m_gap*2
                # l_width = self.Y_SIZE/self.L-l_gap*2
                m_start = self.x_start+im*self.X_SIZE/self.M+self.m_gap
                l_start = self.y_start+il*self.Y_SIZE/self.L+self.l_gap

                # добавляем локальную рамку поля
                self.addRect(self.x_start+im*self.X_SIZE/self.M, self.y_start+il*self.Y_SIZE/self.L,
                             self.X_SIZE/self.M, self.Y_SIZE/self.L, self.pen_black, self.brush_white)

                # цикл по нейронам в поле
                for id in range(self.d):
                    for iq in range(self.q):

                        # определяем начальные координаты и размеры нейрона исходя из координат q и d
                        # q_gap = 0.1*self.m_width/self.q
                        # d_gap = 0.1*self.l_width/self.d
                        # q_width = self.m_width/self.q-q_gap*2
                        # d_width = self.l_width/self.d-d_gap*2
                        q_start = m_start+iq*self.m_width/self.q+self.q_gap
                        d_start = l_start+id*self.l_width/self.d+self.d_gap

                        if self.matrix[self.Lr_index, il, im, id, iq] == 0:
                            self.addEllipse(q_start, d_start, self.q_width, self.d_width, self.pen_black, self.brush_white)
                        if self.matrix[self.Lr_index, il, im, id, iq] > 0:
                            self.addEllipse(q_start, d_start, self.q_width, self.d_width, self.pen_black, self.brush_gray)
                        if self.matrix[self.Lr_index, il, im, id, iq] == -1:
                            self.addEllipse(q_start, d_start, self.q_width, self.d_width, self.pen_black, self.brush_black)

        self.signalDrawed.emit()

    def wheelEvent(self, event):
        koef = 1.1
        if event.delta() > 0:
            if self.pixelSize_wigth * koef > 100000.0 or self.pixelSize_height * koef > 100000.0:
                return

            self.coord_x = event.scenePos().x() * koef
            self.coord_y = event.scenePos().y() * koef
            self.pixelSize_wigth *= koef
            self.pixelSize_height *= koef

        if event.delta() < 0:
            if self.pixelSize_wigth / koef < 10.0 or self.pixelSize_height / koef < 10.0:
                return
            self.pixelSize_wigth /= koef
            self.pixelSize_height /= koef

        self.x_start = self.pixelSize_wigth*0.05
        self.y_start = self.pixelSize_height*0.05
        self.X_SIZE = self.pixelSize_wigth*0.9
        self.Y_SIZE = self.pixelSize_height*0.9
        self.m_gap = 0.02 * self.X_SIZE / self.M
        self.l_gap = 0.02 * self.Y_SIZE / self.L
        self.m_width = self.X_SIZE / self.M - self.m_gap * 2
        self.l_width = self.Y_SIZE / self.L - self.l_gap * 2
        self.q_gap = 0.1 * self.m_width / self.q
        self.d_gap = 0.1 * self.l_width / self.d
        self.q_width = self.m_width / self.q - self.q_gap * 2
        self.d_width = self.l_width / self.d - self.d_gap * 2

        self.drawGraphic('')

    def getScrollParams(self):
        return [self.pixelSize_height, self.pixelSize_wigth, self.coord_y, self.coord_x]