# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/kraftway/Desktop/PyRNN_App_2022_05_01/GUI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.comboBox_ProcessingType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ProcessingType.setEnabled(False)
        self.comboBox_ProcessingType.setObjectName("comboBox_ProcessingType")
        self.comboBox_ProcessingType.addItem("")
        self.comboBox_ProcessingType.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_ProcessingType)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.label_18)
        self.novFiltWeightsGain = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.novFiltWeightsGain.setEnabled(True)
        self.novFiltWeightsGain.setMaximum(9999.99)
        self.novFiltWeightsGain.setObjectName("novFiltWeightsGain")
        self.horizontalLayout_5.addWidget(self.novFiltWeightsGain)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.novFiltDetectBorder = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.novFiltDetectBorder.setEnabled(True)
        self.novFiltDetectBorder.setObjectName("novFiltDetectBorder")
        self.horizontalLayout_5.addWidget(self.novFiltDetectBorder)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_5.addWidget(self.label_24)
        self.novFiltStepsNum = QtWidgets.QSpinBox(self.centralwidget)
        self.novFiltStepsNum.setEnabled(True)
        self.novFiltStepsNum.setObjectName("novFiltStepsNum")
        self.horizontalLayout_5.addWidget(self.novFiltStepsNum)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.predictStepsNum = QtWidgets.QSpinBox(self.centralwidget)
        self.predictStepsNum.setEnabled(True)
        self.predictStepsNum.setObjectName("predictStepsNum")
        self.horizontalLayout_4.addWidget(self.predictStepsNum)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.pushButton_CopyModel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CopyModel.setEnabled(False)
        self.pushButton_CopyModel.setObjectName("pushButton_CopyModel")
        self.horizontalLayout_13.addWidget(self.pushButton_CopyModel)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_rnn1 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_rnn1.sizePolicy().hasHeightForWidth())
        self.dockWidget_rnn1.setSizePolicy(sizePolicy)
        self.dockWidget_rnn1.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_rnn1.setObjectName("dockWidget_rnn1")
        self.dockWidgetContents_rnn1 = QtWidgets.QWidget()
        self.dockWidgetContents_rnn1.setObjectName("dockWidgetContents_rnn1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents_rnn1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_rnn1_begin = QtWidgets.QPushButton(self.dockWidgetContents_rnn1)
        self.pushButton_rnn1_begin.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rnn1_begin.sizePolicy().hasHeightForWidth())
        self.pushButton_rnn1_begin.setSizePolicy(sizePolicy)
        self.pushButton_rnn1_begin.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn1_begin.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn1_begin.setObjectName("pushButton_rnn1_begin")
        self.horizontalLayout.addWidget(self.pushButton_rnn1_begin)
        self.pushButton_rnn1_next = QtWidgets.QPushButton(self.dockWidgetContents_rnn1)
        self.pushButton_rnn1_next.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rnn1_next.sizePolicy().hasHeightForWidth())
        self.pushButton_rnn1_next.setSizePolicy(sizePolicy)
        self.pushButton_rnn1_next.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn1_next.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn1_next.setObjectName("pushButton_rnn1_next")
        self.horizontalLayout.addWidget(self.pushButton_rnn1_next)
        self.pushButton_rnn1_end = QtWidgets.QPushButton(self.dockWidgetContents_rnn1)
        self.pushButton_rnn1_end.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rnn1_end.sizePolicy().hasHeightForWidth())
        self.pushButton_rnn1_end.setSizePolicy(sizePolicy)
        self.pushButton_rnn1_end.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn1_end.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn1_end.setObjectName("pushButton_rnn1_end")
        self.horizontalLayout.addWidget(self.pushButton_rnn1_end)
        self.pushButton_rnn1_clear = QtWidgets.QPushButton(self.dockWidgetContents_rnn1)
        self.pushButton_rnn1_clear.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rnn1_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_rnn1_clear.setSizePolicy(sizePolicy)
        self.pushButton_rnn1_clear.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn1_clear.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn1_clear.setObjectName("pushButton_rnn1_clear")
        self.horizontalLayout.addWidget(self.pushButton_rnn1_clear)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.tabWidget_rnn1 = QtWidgets.QTabWidget(self.dockWidgetContents_rnn1)
        self.tabWidget_rnn1.setObjectName("tabWidget_rnn1")
        self.tab_rnn1_params = QtWidgets.QWidget()
        self.tab_rnn1_params.setObjectName("tab_rnn1_params")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_rnn1_params)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rnn1_flag_learn = QtWidgets.QCheckBox(self.tab_rnn1_params)
        self.rnn1_flag_learn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rnn1_flag_learn.sizePolicy().hasHeightForWidth())
        self.rnn1_flag_learn.setSizePolicy(sizePolicy)
        self.rnn1_flag_learn.setObjectName("rnn1_flag_learn")
        self.horizontalLayout_7.addWidget(self.rnn1_flag_learn)
        self.rnn1_flag_clear_learning = QtWidgets.QCheckBox(self.tab_rnn1_params)
        self.rnn1_flag_clear_learning.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rnn1_flag_clear_learning.sizePolicy().hasHeightForWidth())
        self.rnn1_flag_clear_learning.setSizePolicy(sizePolicy)
        self.rnn1_flag_clear_learning.setObjectName("rnn1_flag_clear_learning")
        self.horizontalLayout_7.addWidget(self.rnn1_flag_clear_learning)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.rnn1_alpha = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_alpha.setProperty("value", 20.0)
        self.rnn1_alpha.setObjectName("rnn1_alpha")
        self.horizontalLayout_6.addWidget(self.rnn1_alpha)
        self.label_6 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.rnn1_h = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_h.setProperty("value", 2.0)
        self.rnn1_h.setObjectName("rnn1_h")
        self.horizontalLayout_6.addWidget(self.rnn1_h)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        self.rnn1_gInc = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_gInc.setSingleStep(0.1)
        self.rnn1_gInc.setProperty("value", 0.5)
        self.rnn1_gInc.setObjectName("rnn1_gInc")
        self.horizontalLayout_11.addWidget(self.rnn1_gInc)
        self.label_21 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_11.addWidget(self.label_21)
        self.rnn1_gDec = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_gDec.setDecimals(4)
        self.rnn1_gDec.setSingleStep(0.1)
        self.rnn1_gDec.setProperty("value", 0.5)
        self.rnn1_gDec.setObjectName("rnn1_gDec")
        self.horizontalLayout_11.addWidget(self.rnn1_gDec)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.rnn1_borderType = QtWidgets.QComboBox(self.tab_rnn1_params)
        self.rnn1_borderType.setObjectName("rnn1_borderType")
        self.rnn1_borderType.addItem("")
        self.rnn1_borderType.addItem("")
        self.gridLayout.addWidget(self.rnn1_borderType, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)
        self.rnn1_borderConstValue = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_borderConstValue.setSingleStep(0.1)
        self.rnn1_borderConstValue.setProperty("value", 1.0)
        self.rnn1_borderConstValue.setObjectName("rnn1_borderConstValue")
        self.gridLayout.addWidget(self.rnn1_borderConstValue, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 2, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 2, 1, 1)
        self.rnn1_borderConcurrentWinners = QtWidgets.QSpinBox(self.tab_rnn1_params)
        self.rnn1_borderConcurrentWinners.setMaximum(999)
        self.rnn1_borderConcurrentWinners.setObjectName("rnn1_borderConcurrentWinners")
        self.gridLayout.addWidget(self.rnn1_borderConcurrentWinners, 3, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab_rnn1_params)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.rnn1_input_data_file_path = QtWidgets.QLineEdit(self.tab_rnn1_params)
        self.rnn1_input_data_file_path.setEnabled(True)
        self.rnn1_input_data_file_path.setObjectName("rnn1_input_data_file_path")
        self.horizontalLayout_2.addWidget(self.rnn1_input_data_file_path)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton_rnn1_refreshParams = QtWidgets.QPushButton(self.tab_rnn1_params)
        self.pushButton_rnn1_refreshParams.setObjectName("pushButton_rnn1_refreshParams")
        self.verticalLayout_2.addWidget(self.pushButton_rnn1_refreshParams)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.tabWidget_rnn1.addTab(self.tab_rnn1_params, "")
        self.tab_rnn1_lr1 = QtWidgets.QWidget()
        self.tab_rnn1_lr1.setObjectName("tab_rnn1_lr1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_rnn1_lr1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView_rnn1_lr1 = QtWidgets.QGraphicsView(self.tab_rnn1_lr1)
        self.graphicsView_rnn1_lr1.setObjectName("graphicsView_rnn1_lr1")
        self.verticalLayout_3.addWidget(self.graphicsView_rnn1_lr1)
        self.tabWidget_rnn1.addTab(self.tab_rnn1_lr1, "")
        self.tab_rnn1_lr2 = QtWidgets.QWidget()
        self.tab_rnn1_lr2.setObjectName("tab_rnn1_lr2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_rnn1_lr2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView_rnn1_lr2 = QtWidgets.QGraphicsView(self.tab_rnn1_lr2)
        self.graphicsView_rnn1_lr2.setObjectName("graphicsView_rnn1_lr2")
        self.verticalLayout_4.addWidget(self.graphicsView_rnn1_lr2)
        self.tabWidget_rnn1.addTab(self.tab_rnn1_lr2, "")
        self.verticalLayout_5.addWidget(self.tabWidget_rnn1)
        self.dockWidget_rnn1.setWidget(self.dockWidgetContents_rnn1)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_rnn1)
        self.dockWidget_rnn2 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_rnn2.sizePolicy().hasHeightForWidth())
        self.dockWidget_rnn2.setSizePolicy(sizePolicy)
        self.dockWidget_rnn2.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_rnn2.setObjectName("dockWidget_rnn2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.pushButton_rnn2_next = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.pushButton_rnn2_next.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rnn2_next.sizePolicy().hasHeightForWidth())
        self.pushButton_rnn2_next.setSizePolicy(sizePolicy)
        self.pushButton_rnn2_next.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn2_next.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn2_next.setObjectName("pushButton_rnn2_next")
        self.horizontalLayout_3.addWidget(self.pushButton_rnn2_next)
        self.pushButton_rnn2_end = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.pushButton_rnn2_end.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rnn2_end.sizePolicy().hasHeightForWidth())
        self.pushButton_rnn2_end.setSizePolicy(sizePolicy)
        self.pushButton_rnn2_end.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn2_end.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn2_end.setObjectName("pushButton_rnn2_end")
        self.horizontalLayout_3.addWidget(self.pushButton_rnn2_end)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.tabWidget_rnn2 = QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget_rnn2.setObjectName("tabWidget_rnn2")
        self.tab_rnn2_params = QtWidgets.QWidget()
        self.tab_rnn2_params.setObjectName("tab_rnn2_params")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_rnn2_params)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.rnn2_alpha = QtWidgets.QDoubleSpinBox(self.tab_rnn2_params)
        self.rnn2_alpha.setEnabled(True)
        self.rnn2_alpha.setProperty("value", 20.0)
        self.rnn2_alpha.setObjectName("rnn2_alpha")
        self.horizontalLayout_9.addWidget(self.rnn2_alpha)
        self.label_7 = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.rnn2_h = QtWidgets.QDoubleSpinBox(self.tab_rnn2_params)
        self.rnn2_h.setEnabled(True)
        self.rnn2_h.setProperty("value", 2.0)
        self.rnn2_h.setObjectName("rnn2_h")
        self.horizontalLayout_9.addWidget(self.rnn2_h)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)
        self.rnn2_borderType = QtWidgets.QComboBox(self.tab_rnn2_params)
        self.rnn2_borderType.setObjectName("rnn2_borderType")
        self.rnn2_borderType.addItem("")
        self.rnn2_borderType.addItem("")
        self.gridLayout_3.addWidget(self.rnn2_borderType, 1, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem18, 2, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 2, 1, 1)
        self.rnn2_borderConstValue = QtWidgets.QDoubleSpinBox(self.tab_rnn2_params)
        self.rnn2_borderConstValue.setSingleStep(0.1)
        self.rnn2_borderConstValue.setProperty("value", 0.5)
        self.rnn2_borderConstValue.setObjectName("rnn2_borderConstValue")
        self.gridLayout_3.addWidget(self.rnn2_borderConstValue, 2, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 3, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 2, 1, 1)
        self.rnn2_borderConcurrentWinners = QtWidgets.QSpinBox(self.tab_rnn2_params)
        self.rnn2_borderConcurrentWinners.setMaximum(999)
        self.rnn2_borderConcurrentWinners.setObjectName("rnn2_borderConcurrentWinners")
        self.gridLayout_3.addWidget(self.rnn2_borderConcurrentWinners, 3, 3, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_3)
        self.pushButton_rnn2_refreshParams = QtWidgets.QPushButton(self.tab_rnn2_params)
        self.pushButton_rnn2_refreshParams.setObjectName("pushButton_rnn2_refreshParams")
        self.verticalLayout_9.addWidget(self.pushButton_rnn2_refreshParams)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem19)
        self.tabWidget_rnn2.addTab(self.tab_rnn2_params, "")
        self.tab_rnn2_lr1 = QtWidgets.QWidget()
        self.tab_rnn2_lr1.setObjectName("tab_rnn2_lr1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_rnn2_lr1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView_rnn2_lr1 = QtWidgets.QGraphicsView(self.tab_rnn2_lr1)
        self.graphicsView_rnn2_lr1.setObjectName("graphicsView_rnn2_lr1")
        self.verticalLayout_6.addWidget(self.graphicsView_rnn2_lr1)
        self.tabWidget_rnn2.addTab(self.tab_rnn2_lr1, "")
        self.tab_rnn2_lr2 = QtWidgets.QWidget()
        self.tab_rnn2_lr2.setObjectName("tab_rnn2_lr2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_rnn2_lr2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graphicsView_rnn2_lr2 = QtWidgets.QGraphicsView(self.tab_rnn2_lr2)
        self.graphicsView_rnn2_lr2.setObjectName("graphicsView_rnn2_lr2")
        self.verticalLayout_7.addWidget(self.graphicsView_rnn2_lr2)
        self.tabWidget_rnn2.addTab(self.tab_rnn2_lr2, "")
        self.verticalLayout_8.addWidget(self.tabWidget_rnn2)
        self.dockWidget_rnn2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_rnn2)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget_rnn1.setCurrentIndex(0)
        self.tabWidget_rnn2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RnnEmulator"))
        self.comboBox_ProcessingType.setItemText(0, _translate("MainWindow", "Predict"))
        self.comboBox_ProcessingType.setItemText(1, _translate("MainWindow", "Novelty filter"))
        self.label_18.setText(_translate("MainWindow", "Novelty filtering with weights gain"))
        self.label_5.setText(_translate("MainWindow", "and detection border"))
        self.label_24.setText(_translate("MainWindow", " for "))
        self.label_9.setText(_translate("MainWindow", "steps;"))
        self.label_17.setText(_translate("MainWindow", "Predict for:"))
        self.label_4.setText(_translate("MainWindow", "steps;"))
        self.pushButton_CopyModel.setText(_translate("MainWindow", "Copy model"))
        self.dockWidget_rnn1.setWindowTitle(_translate("MainWindow", "RNN 1"))
        self.pushButton_rnn1_begin.setText(_translate("MainWindow", "Bgn"))
        self.pushButton_rnn1_next.setText(_translate("MainWindow", "Nxt"))
        self.pushButton_rnn1_end.setText(_translate("MainWindow", "End"))
        self.pushButton_rnn1_clear.setText(_translate("MainWindow", "Clr"))
        self.rnn1_flag_learn.setText(_translate("MainWindow", "Train"))
        self.rnn1_flag_clear_learning.setText(_translate("MainWindow", "Clear_mode"))
        self.label_3.setText(_translate("MainWindow", "alpha:"))
        self.label_6.setText(_translate("MainWindow", "h: "))
        self.label_2.setText(_translate("MainWindow", "gInc: "))
        self.label_21.setText(_translate("MainWindow", "gDec: "))
        self.rnn1_borderType.setItemText(0, _translate("MainWindow", "Const"))
        self.rnn1_borderType.setItemText(1, _translate("MainWindow", "Concurrent"))
        self.label_12.setText(_translate("MainWindow", "Value:"))
        self.label_11.setText(_translate("MainWindow", "Excitation border:"))
        self.label_15.setText(_translate("MainWindow", "Const border:"))
        self.label_19.setText(_translate("MainWindow", "Concurrent border:"))
        self.label_20.setText(_translate("MainWindow", "Num of winners:"))
        self.label.setText(_translate("MainWindow", "InputData:"))
        self.pushButton_rnn1_refreshParams.setText(_translate("MainWindow", "Refresh params"))
        self.tabWidget_rnn1.setTabText(self.tabWidget_rnn1.indexOf(self.tab_rnn1_params), _translate("MainWindow", "RNN1 params"))
        self.tabWidget_rnn1.setTabText(self.tabWidget_rnn1.indexOf(self.tab_rnn1_lr1), _translate("MainWindow", "1st layer"))
        self.tabWidget_rnn1.setTabText(self.tabWidget_rnn1.indexOf(self.tab_rnn1_lr2), _translate("MainWindow", "2nd layer"))
        self.dockWidget_rnn2.setWindowTitle(_translate("MainWindow", "RNN2"))
        self.pushButton_rnn2_next.setText(_translate("MainWindow", "Nxt"))
        self.pushButton_rnn2_end.setText(_translate("MainWindow", "End"))
        self.label_8.setText(_translate("MainWindow", "alpha:"))
        self.label_7.setText(_translate("MainWindow", "h: "))
        self.label_13.setText(_translate("MainWindow", "Excitation border:"))
        self.label_16.setText(_translate("MainWindow", "Const border:"))
        self.rnn2_borderType.setItemText(0, _translate("MainWindow", "Const"))
        self.rnn2_borderType.setItemText(1, _translate("MainWindow", "Concurrent"))
        self.label_14.setText(_translate("MainWindow", "Value:"))
        self.label_22.setText(_translate("MainWindow", "Concurrent border:"))
        self.label_23.setText(_translate("MainWindow", "Num of winners:"))
        self.pushButton_rnn2_refreshParams.setText(_translate("MainWindow", "Refresh params"))
        self.tabWidget_rnn2.setTabText(self.tabWidget_rnn2.indexOf(self.tab_rnn2_params), _translate("MainWindow", "RNN2 params"))
        self.tabWidget_rnn2.setTabText(self.tabWidget_rnn2.indexOf(self.tab_rnn2_lr1), _translate("MainWindow", "1st layer"))
        self.tabWidget_rnn2.setTabText(self.tabWidget_rnn2.indexOf(self.tab_rnn2_lr2), _translate("MainWindow", "2nd layer"))
