from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):

    def setSizePolicy(self, object: QtWidgets.QWidget, h: QtWidgets.QSizePolicy, v: QtWidgets.QSizePolicy):
        sizePolicy = QtWidgets.QSizePolicy(h, v)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object.sizePolicy().hasHeightForWidth())
        object.setSizePolicy(sizePolicy)

    def addHSpacer(self):
        return QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum)

    def addVSpacer(self):
        return QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding)

    def setCheckBox(self):
        pass

    def setPushButton(self):
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 600)

        # main window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # mode
        self.horizontalLayout_mode = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mode.setObjectName("horizontalLayout_mode")
        self.comboBox_ProcessingType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ProcessingType.setEnabled(False)
        self.comboBox_ProcessingType.setObjectName("comboBox_ProcessingType")
        self.comboBox_ProcessingType.addItem("")
        self.comboBox_ProcessingType.addItem("")
        self.horizontalLayout_mode.addWidget(self.comboBox_ProcessingType)
        self.horizontalLayout_mode.addItem(self.addHSpacer())
        self.verticalLayout.addLayout(self.horizontalLayout_mode)

        # mode params
        self.gridLayout_modeParams = QtWidgets.QGridLayout()
        self.gridLayout_modeParams.setObjectName("gridLayout_modeParams")

        # novelty
        self.horizontalLayout_novelty = QtWidgets.QHBoxLayout()
        self.horizontalLayout_novelty.setObjectName("horizontalLayout_novelty")
        self.label_NovFilt = QtWidgets.QLabel(self.centralwidget)
        self.label_NovFilt.setObjectName("label_NovFilt")
        self.horizontalLayout_novelty.addWidget(self.label_NovFilt)
        self.novFiltWeightsGain = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.novFiltWeightsGain.setEnabled(True)
        self.novFiltWeightsGain.setMaximum(9999.99)
        self.novFiltWeightsGain.setObjectName("novFiltWeightsGain")
        self.horizontalLayout_novelty.addWidget(self.novFiltWeightsGain)
        self.label_DetectBorder = QtWidgets.QLabel(self.centralwidget)
        self.setSizePolicy(self.label_DetectBorder,
                           QtWidgets.QSizePolicy.Preferred,
                           QtWidgets.QSizePolicy.Maximum)
        self.label_DetectBorder.setObjectName("label_DetectBorder")
        self.horizontalLayout_novelty.addWidget(self.label_DetectBorder)
        self.novFiltDetectBorder = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.novFiltDetectBorder.setEnabled(True)
        self.novFiltDetectBorder.setObjectName("novFiltDetectBorder")
        self.horizontalLayout_novelty.addWidget(self.novFiltDetectBorder)
        self.label_DetectBorderStepsPrefix = \
            QtWidgets.QLabel(self.centralwidget)
        self.label_DetectBorderStepsPrefix.setObjectName(
            "label_DetectBorderStepsPrefix")
        self.horizontalLayout_novelty.addWidget(
            self.label_DetectBorderStepsPrefix)
        self.novFiltStepsNum = QtWidgets.QSpinBox(self.centralwidget)
        self.novFiltStepsNum.setEnabled(True)
        self.novFiltStepsNum.setObjectName("novFiltStepsNum")
        self.horizontalLayout_novelty.addWidget(self.novFiltStepsNum)
        self.label_DetectBorderStepsSuffix = \
            QtWidgets.QLabel(self.centralwidget)
        self.label_DetectBorderStepsSuffix.setEnabled(True)
        self.setSizePolicy(self.label_DetectBorderStepsSuffix,
                           QtWidgets.QSizePolicy.Preferred,
                           QtWidgets.QSizePolicy.Maximum)
        self.label_DetectBorderStepsSuffix.setObjectName(
            "label_DetectBorderStepsSuffix")
        self.horizontalLayout_novelty.addWidget(
            self.label_DetectBorderStepsSuffix)
        self.horizontalLayout_novelty.addItem(self.addHSpacer())
        self.gridLayout_modeParams.addLayout(
            self.horizontalLayout_novelty, 3, 0, 1, 1)

        # predict
        self.horizontalLayout_predict = \
            QtWidgets.QHBoxLayout()
        self.horizontalLayout_predict.setObjectName(
            "horizontalLayout_predict")
        self.label_PredictStepsNumPrefix = \
            QtWidgets.QLabel(self.centralwidget)
        self.label_PredictStepsNumPrefix.setObjectName(
            "label_PredictStepsNumPrefix")
        self.horizontalLayout_predict.addWidget(
            self.label_PredictStepsNumPrefix)
        self.predictStepsNum = QtWidgets.QSpinBox(self.centralwidget)
        self.predictStepsNum.setEnabled(True)
        self.predictStepsNum.setObjectName("predictStepsNum")
        self.horizontalLayout_predict.addWidget(self.predictStepsNum)
        self.label_PredictStepsNumSuffix = \
            QtWidgets.QLabel(self.centralwidget)
        self.label_PredictStepsNumSuffix.setEnabled(True)
        self.setSizePolicy(self.label_PredictStepsNumSuffix,
                           QtWidgets.QSizePolicy.Preferred,
                           QtWidgets.QSizePolicy.Maximum)
        self.label_PredictStepsNumSuffix.setObjectName(
            "label_PredictStepsNumSuffix")
        self.horizontalLayout_predict.addWidget(
            self.label_PredictStepsNumSuffix)
        self.horizontalLayout_predict.addItem(self.addHSpacer())
        self.gridLayout_modeParams.addLayout(
            self.horizontalLayout_predict, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_modeParams)
        self.verticalLayout.addItem(self.addVSpacer())

        # COPY button
        self.horizontalLayout_copyButton = QtWidgets.QHBoxLayout()
        self.horizontalLayout_copyButton.setObjectName(
            "horizontalLayout_copyButton")
        self.horizontalLayout_copyButton.addItem(self.addHSpacer())
        self.pushButton_CopyModel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CopyModel.setEnabled(False)
        self.pushButton_CopyModel.setObjectName("pushButton_CopyModel")
        self.horizontalLayout_copyButton.addWidget(self.pushButton_CopyModel)
        self.horizontalLayout_copyButton.addItem(self.addHSpacer())
        self.verticalLayout.addLayout(self.horizontalLayout_copyButton)

        # central widget
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Rnn-1
        self.dockWidget_rnn1 = QtWidgets.QDockWidget(MainWindow)
        self.setSizePolicy(self.dockWidget_rnn1,
                           QtWidgets.QSizePolicy.Preferred,
                           QtWidgets.QSizePolicy.Minimum)
        self.dockWidget_rnn1.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable |
            QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_rnn1.setObjectName("dockWidget_rnn1")
        self.dockWidgetContents_rnn1 = QtWidgets.QWidget()
        self.dockWidgetContents_rnn1.setObjectName(
            "dockWidgetContents_rnn1")
        self.verticalLayout_rnn1widgets = \
            QtWidgets.QVBoxLayout(self.dockWidgetContents_rnn1)
        self.verticalLayout_rnn1widgets.setObjectName(
            "verticalLayout_rnn1widgets")
        self.horizontalLayout_rnn1buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rnn1buttons.setObjectName(
            "horizontalLayout_rnn1buttons")
        self.horizontalLayout_rnn1buttons.addItem(self.addHSpacer())

        # Rnn1 buttons
        self.pushButton_rnn1_begin = \
            QtWidgets.QPushButton(self.dockWidgetContents_rnn1)
        self.pushButton_rnn1_begin.setEnabled(True)
        self.setSizePolicy(self.pushButton_rnn1_begin,
                           QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Fixed)
        self.pushButton_rnn1_begin.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn1_begin.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn1_begin.setObjectName("pushButton_rnn1_begin")
        self.horizontalLayout_rnn1buttons.addWidget(self.pushButton_rnn1_begin)
        self.pushButton_rnn1_next = \
            QtWidgets.QPushButton(self.dockWidgetContents_rnn1)
        self.pushButton_rnn1_next.setEnabled(True)
        self.setSizePolicy(self.pushButton_rnn1_next,
                           QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Fixed)
        self.pushButton_rnn1_next.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn1_next.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn1_next.setObjectName("pushButton_rnn1_next")
        self.horizontalLayout_rnn1buttons.addWidget(self.pushButton_rnn1_next)
        self.pushButton_rnn1_end = \
            QtWidgets.QPushButton(self.dockWidgetContents_rnn1)
        self.pushButton_rnn1_end.setEnabled(True)
        self.setSizePolicy(self.pushButton_rnn1_end,
                           QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Fixed)
        self.pushButton_rnn1_end.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn1_end.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn1_end.setObjectName("pushButton_rnn1_end")
        self.horizontalLayout_rnn1buttons.addWidget(self.pushButton_rnn1_end)
        self.pushButton_rnn1_clear = \
            QtWidgets.QPushButton(self.dockWidgetContents_rnn1)
        self.pushButton_rnn1_clear.setEnabled(True)
        self.setSizePolicy(self.pushButton_rnn1_clear,
                           QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Fixed)
        self.pushButton_rnn1_clear.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn1_clear.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn1_clear.setObjectName("pushButton_rnn1_clear")
        self.horizontalLayout_rnn1buttons.addWidget(self.pushButton_rnn1_clear)
        self.horizontalLayout_rnn1buttons.addItem(self.addHSpacer())
        self.verticalLayout_rnn1widgets.addLayout(
            self.horizontalLayout_rnn1buttons)

        # Rnn1 settings and layers
        self.tabWidget_rnn1 = QtWidgets.QTabWidget(
            self.dockWidgetContents_rnn1)
        self.tabWidget_rnn1.setObjectName("tabWidget_rnn1")
        self.tab_rnn1_params = QtWidgets.QWidget()
        self.tab_rnn1_params.setObjectName("tab_rnn1_params")
        self.verticalLayout_tabrnn1 = \
            QtWidgets.QVBoxLayout(self.tab_rnn1_params)
        self.verticalLayout_tabrnn1.setObjectName("verticalLayout_tabrnn1")
        self.horizontalLayout_rnn1checkParams = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rnn1checkParams.setObjectName(
            "horizontalLayout_rnn1checkParams")
        self.rnn1_flag_learn = QtWidgets.QCheckBox(
            self.tab_rnn1_params)
        self.rnn1_flag_learn.setEnabled(True)
        self.setSizePolicy(self.rnn1_flag_learn,
                           QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Fixed)
        self.rnn1_flag_learn.setObjectName("rnn1_flag_learn")
        self.horizontalLayout_rnn1checkParams.addWidget(
            self.rnn1_flag_learn)
        self.rnn1_flag_clear_learning = QtWidgets.QCheckBox(
            self.tab_rnn1_params)
        self.rnn1_flag_clear_learning.setEnabled(True)
        self.setSizePolicy(self.rnn1_flag_clear_learning,
                           QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Fixed)
        self.rnn1_flag_clear_learning.setObjectName(
            "rnn1_flag_clear_learning")
        self.horizontalLayout_rnn1checkParams.addWidget(
            self.rnn1_flag_clear_learning)
        self.horizontalLayout_rnn1checkParams.addItem(
            self.addHSpacer())
        self.verticalLayout_tabrnn1.addLayout(
            self.horizontalLayout_rnn1checkParams)
        self.horizontalLayout_rnn1bParams = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rnn1bParams.setObjectName(
            "horizontalLayout_rnn1bParams")
        self.label_rnn1alpha = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_rnn1alpha.setObjectName("label_rnn1alpha")
        self.horizontalLayout_rnn1bParams.addWidget(self.label_rnn1alpha)
        self.rnn1_alpha = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_alpha.setProperty("value", 20.0)
        self.rnn1_alpha.setObjectName("rnn1_alpha")
        self.horizontalLayout_rnn1bParams.addWidget(self.rnn1_alpha)
        self.label_rnn1h = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_rnn1h.setObjectName("label_rnn1h")
        self.horizontalLayout_rnn1bParams.addWidget(self.label_rnn1h)
        self.rnn1_h = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_h.setProperty("value", 2.0)
        self.rnn1_h.setObjectName("rnn1_h")
        self.horizontalLayout_rnn1bParams.addWidget(self.rnn1_h)
        self.horizontalLayout_rnn1bParams.addItem(self.addHSpacer())
        self.verticalLayout_tabrnn1.addLayout(
            self.horizontalLayout_rnn1bParams)
        self.horizontalLayout_rnn1kParams = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rnn1kParams.setObjectName(
            "horizontalLayout_rnn1kParams")
        self.label_gInc = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_gInc.setObjectName("label_gInc")
        self.horizontalLayout_rnn1kParams.addWidget(self.label_gInc)
        self.rnn1_gInc = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_gInc.setSingleStep(0.1)
        self.rnn1_gInc.setProperty("value", 0.5)
        self.rnn1_gInc.setObjectName("rnn1_gInc")
        self.horizontalLayout_rnn1kParams.addWidget(self.rnn1_gInc)
        self.label_gDec = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_gDec.setObjectName("label_gDec")
        self.horizontalLayout_rnn1kParams.addWidget(self.label_gDec)
        self.rnn1_gDec = QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_gDec.setDecimals(4)
        self.rnn1_gDec.setSingleStep(0.1)
        self.rnn1_gDec.setProperty("value", 0.5)
        self.rnn1_gDec.setObjectName("rnn1_gDec")
        self.horizontalLayout_rnn1kParams.addWidget(self.rnn1_gDec)
        self.horizontalLayout_rnn1kParams.addItem(self.addHSpacer())
        self.verticalLayout_tabrnn1.addLayout(
            self.horizontalLayout_rnn1kParams)
        self.gridLayout_rnn1borderParams = QtWidgets.QGridLayout()
        self.gridLayout_rnn1borderParams.setObjectName(
            "gridLayout_rnn1borderParams")
        self.rnn1_borderType = QtWidgets.QComboBox(
            self.tab_rnn1_params)
        self.rnn1_borderType.setObjectName("rnn1_borderType")
        self.rnn1_borderType.addItem("")
        self.rnn1_borderType.addItem("")
        self.gridLayout_rnn1borderParams.addWidget(
            self.rnn1_borderType, 1, 0, 1, 1)
        self.label_rnn1cbValue = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_rnn1cbValue.setObjectName("label_rnn1cbValue")
        self.gridLayout_rnn1borderParams.addWidget(
            self.label_rnn1cbValue, 2, 2, 1, 1)
        self.rnn1_borderConstValue = \
            QtWidgets.QDoubleSpinBox(self.tab_rnn1_params)
        self.rnn1_borderConstValue.setSingleStep(0.1)
        self.rnn1_borderConstValue.setProperty("value", 1.0)
        self.rnn1_borderConstValue.setObjectName("rnn1_borderConstValue")
        self.gridLayout_rnn1borderParams.addWidget(
            self.rnn1_borderConstValue, 2, 3, 1, 1)
        self.label_rnn1border = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_rnn1border.setObjectName("label_rnn1border")
        self.gridLayout_rnn1borderParams.addWidget(
            self.label_rnn1border, 0, 0, 1, 1)
        self.gridLayout_rnn1borderParams.addItem(self.addHSpacer(), 2, 4, 1, 1)
        self.label_rnn1constBorder = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_rnn1constBorder.setObjectName("label_rnn1constBorder")
        self.gridLayout_rnn1borderParams.addWidget(
            self.label_rnn1constBorder, 2, 0, 1, 1)
        self.label_rnn1concurrentBorder = \
            QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_rnn1concurrentBorder.setObjectName(
            "label_rnn1concurrentBorder")
        self.gridLayout_rnn1borderParams.addWidget(
            self.label_rnn1concurrentBorder, 3, 0, 1, 1)
        self.label_rnn1numWinners = QtWidgets.QLabel(self.tab_rnn1_params)
        self.label_rnn1numWinners.setObjectName("label_rnn1numWinners")
        self.gridLayout_rnn1borderParams.addWidget(
            self.label_rnn1numWinners, 3, 2, 1, 1)
        self.rnn1_borderConcurrentWinners = \
            QtWidgets.QSpinBox(self.tab_rnn1_params)
        self.rnn1_borderConcurrentWinners.setMaximum(999)
        self.rnn1_borderConcurrentWinners.setObjectName(
            "rnn1_borderConcurrentWinners")
        self.gridLayout_rnn1borderParams.addWidget(
            self.rnn1_borderConcurrentWinners, 3, 3, 1, 1)
        self.verticalLayout_tabrnn1.addLayout(self.gridLayout_rnn1borderParams)
        self.horizontalLayout_inputData = QtWidgets.QHBoxLayout()
        self.horizontalLayout_inputData.setObjectName(
            "horizontalLayout_inputData")
        self.label_InputData = QtWidgets.QLabel(
            self.tab_rnn1_params)
        self.setSizePolicy(self.label_InputData,
                           QtWidgets.QSizePolicy.Preferred,
                           QtWidgets.QSizePolicy.Maximum)
        self.label_InputData.setObjectName("label_InputData")
        self.horizontalLayout_inputData.addWidget(self.label_InputData)
        self.rnn1_input_data_file_path = \
            QtWidgets.QLineEdit(self.tab_rnn1_params)
        self.rnn1_input_data_file_path.setEnabled(True)
        self.rnn1_input_data_file_path.setObjectName(
            "rnn1_input_data_file_path")
        self.horizontalLayout_inputData.addWidget(
            self.rnn1_input_data_file_path)
        self.horizontalLayout_inputData.addItem(self.addHSpacer())
        self.verticalLayout_tabrnn1.addLayout(
            self.horizontalLayout_inputData)
        self.pushButton_rnn1_refreshParams = \
            QtWidgets.QPushButton(self.tab_rnn1_params)
        self.pushButton_rnn1_refreshParams.setObjectName(
            "pushButton_rnn1_refreshParams")
        self.verticalLayout_tabrnn1.addWidget(
            self.pushButton_rnn1_refreshParams)
        self.verticalLayout_tabrnn1.addItem(self.addVSpacer())
        self.tabWidget_rnn1.addTab(self.tab_rnn1_params, "")
        self.tab_rnn1_lr1 = QtWidgets.QWidget()
        self.tab_rnn1_lr1.setObjectName("tab_rnn1_lr1")
        self.verticalLayout_tabrnn1lr1 = \
            QtWidgets.QVBoxLayout(self.tab_rnn1_lr1)
        self.verticalLayout_tabrnn1lr1.setObjectName(
            "verticalLayout_tabrnn1lr1")
        self.graphicsView_rnn1_lr1 = QtWidgets.QGraphicsView(self.tab_rnn1_lr1)
        self.graphicsView_rnn1_lr1.setObjectName("graphicsView_rnn1_lr1")
        self.verticalLayout_tabrnn1lr1.addWidget(self.graphicsView_rnn1_lr1)
        self.tabWidget_rnn1.addTab(self.tab_rnn1_lr1, "")
        self.tab_rnn1_lr2 = QtWidgets.QWidget()
        self.tab_rnn1_lr2.setObjectName("tab_rnn1_lr2")
        self.verticalLayout_tabrnn1lr2 = \
            QtWidgets.QVBoxLayout(self.tab_rnn1_lr2)
        self.verticalLayout_tabrnn1lr2.setObjectName(
            "verticalLayout_tabrnn1lr2")
        self.graphicsView_rnn1_lr2 = QtWidgets.QGraphicsView(self.tab_rnn1_lr2)
        self.graphicsView_rnn1_lr2.setObjectName("graphicsView_rnn1_lr2")
        self.verticalLayout_tabrnn1lr2.addWidget(self.graphicsView_rnn1_lr2)
        self.tabWidget_rnn1.addTab(self.tab_rnn1_lr2, "")
        self.verticalLayout_rnn1widgets.addWidget(self.tabWidget_rnn1)
        self.dockWidget_rnn1.setWidget(self.dockWidgetContents_rnn1)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),
                                 self.dockWidget_rnn1)

        # Rnn2
        self.dockWidget_rnn2 = QtWidgets.QDockWidget(MainWindow)
        self.setSizePolicy(self.dockWidget_rnn2,
                           QtWidgets.QSizePolicy.Preferred,
                           QtWidgets.QSizePolicy.Minimum)
        self.dockWidget_rnn2.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable |
            QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_rnn2.setObjectName("dockWidget_rnn2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_tabrnn2 = \
            QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_tabrnn2.setObjectName("verticalLayout_tabrnn2")
        self.horizontalLayout_rnn2buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rnn2buttons.setObjectName(
            "horizontalLayout_rnn2buttons")
        self.horizontalLayout_rnn2buttons.addItem(self.addHSpacer())

        # Rnn-2 buttons
        self.pushButton_rnn2_next = QtWidgets.QPushButton(
            self.dockWidgetContents_2)
        self.pushButton_rnn2_next.setEnabled(True)
        self.setSizePolicy(self.pushButton_rnn2_next,
                           QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Fixed)
        self.pushButton_rnn2_next.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn2_next.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn2_next.setObjectName("pushButton_rnn2_next")
        self.horizontalLayout_rnn2buttons.addWidget(self.pushButton_rnn2_next)
        self.pushButton_rnn2_end = QtWidgets.QPushButton(
            self.dockWidgetContents_2)
        self.pushButton_rnn2_end.setEnabled(True)
        self.setSizePolicy(self.pushButton_rnn2_end,
                           QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Fixed)
        self.pushButton_rnn2_end.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_rnn2_end.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_rnn2_end.setObjectName("pushButton_rnn2_end")
        self.horizontalLayout_rnn2buttons.addWidget(self.pushButton_rnn2_end)
        self.horizontalLayout_rnn2buttons.addItem(self.addHSpacer())
        self.verticalLayout_tabrnn2.addLayout(
            self.horizontalLayout_rnn2buttons)

        # Rnn2 settings and layers
        self.tabWidget_rnn2 = \
            QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget_rnn2.setObjectName("tabWidget_rnn2")
        self.tab_rnn2_params = QtWidgets.QWidget()
        self.tab_rnn2_params.setObjectName("tab_rnn2_params")
        self.verticalLayout_rnn2prms = \
            QtWidgets.QVBoxLayout(self.tab_rnn2_params)
        self.verticalLayout_rnn2prms.setObjectName(
            "verticalLayout_rnn2prms")
        self.horizontalLayout_rnn2checkParams = \
            QtWidgets.QHBoxLayout()
        self.horizontalLayout_rnn2checkParams.setObjectName(
            "horizontalLayout_rnn2checkParams")
        self.horizontalLayout_rnn2checkParams.addItem(self.addHSpacer())
        self.verticalLayout_rnn2prms.addLayout(
            self.horizontalLayout_rnn2checkParams)
        self.horizontalLayout_rnn2kParams = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rnn2kParams.setObjectName(
            "horizontalLayout_rnn2kParams")
        self.label_rnn2alpha = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_rnn2alpha.setObjectName("label_rnn2alpha")
        self.horizontalLayout_rnn2kParams.addWidget(self.label_rnn2alpha)
        self.rnn2_alpha = QtWidgets.QDoubleSpinBox(self.tab_rnn2_params)
        self.rnn2_alpha.setEnabled(True)
        self.rnn2_alpha.setProperty("value", 20.0)
        self.rnn2_alpha.setObjectName("rnn2_alpha")
        self.horizontalLayout_rnn2kParams.addWidget(self.rnn2_alpha)
        self.label_rnn2h = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_rnn2h.setObjectName("label_rnn2h")
        self.horizontalLayout_rnn2kParams.addWidget(self.label_rnn2h)
        self.rnn2_h = QtWidgets.QDoubleSpinBox(self.tab_rnn2_params)
        self.rnn2_h.setEnabled(True)
        self.rnn2_h.setProperty("value", 2.0)
        self.rnn2_h.setObjectName("rnn2_h")
        self.horizontalLayout_rnn2kParams.addWidget(
            self.rnn2_h)
        self.horizontalLayout_rnn2kParams.addItem(
            self.addHSpacer())
        self.verticalLayout_rnn2prms.addLayout(
            self.horizontalLayout_rnn2kParams)
        self.gridLayout_rnn2borderParams = \
            QtWidgets.QGridLayout()
        self.gridLayout_rnn2borderParams.setObjectName(
            "gridLayout_rnn2borderParams")
        self.label_rnn2border = QtWidgets.QLabel(
            self.tab_rnn2_params)
        self.label_rnn2border.setObjectName(
            "label_rnn2border")
        self.gridLayout_rnn2borderParams.addWidget(
            self.label_rnn2border, 0, 0, 1, 1)
        self.label_rnn2constBorder = QtWidgets.QLabel(
            self.tab_rnn2_params)
        self.label_rnn2constBorder.setObjectName(
            "label_rnn2constBorder")
        self.gridLayout_rnn2borderParams.addWidget(
            self.label_rnn2constBorder, 2, 0, 1, 1)
        self.rnn2_borderType = QtWidgets.QComboBox(
            self.tab_rnn2_params)
        self.rnn2_borderType.setObjectName("rnn2_borderType")
        self.rnn2_borderType.addItem("")
        self.rnn2_borderType.addItem("")
        self.gridLayout_rnn2borderParams.addWidget(
            self.rnn2_borderType, 1, 0, 1, 1)
        self.gridLayout_rnn2borderParams.addItem(
            self.addHSpacer(), 2, 4, 1, 1)
        self.label_rnn2cbValue = QtWidgets.QLabel(
            self.tab_rnn2_params)
        self.label_rnn2cbValue.setObjectName(
            "label_rnn2cbValue")
        self.gridLayout_rnn2borderParams.addWidget(
            self.label_rnn2cbValue, 2, 2, 1, 1)
        self.rnn2_borderConstValue = \
            QtWidgets.QDoubleSpinBox(self.tab_rnn2_params)
        self.rnn2_borderConstValue.setSingleStep(0.1)
        self.rnn2_borderConstValue.setProperty("value", 0.5)
        self.rnn2_borderConstValue.setObjectName(
            "rnn2_borderConstValue")
        self.gridLayout_rnn2borderParams.addWidget(
            self.rnn2_borderConstValue, 2, 3, 1, 1)
        self.label_rnn2concurrentBorder = \
            QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_rnn2concurrentBorder.setObjectName(
            "label_rnn2concurrentBorder")
        self.gridLayout_rnn2borderParams.addWidget(
            self.label_rnn2concurrentBorder, 3, 0, 1, 1)
        self.label_rnn2numWinnders = QtWidgets.QLabel(self.tab_rnn2_params)
        self.label_rnn2numWinnders.setObjectName("label_rnn2numWinnders")
        self.gridLayout_rnn2borderParams.addWidget(
            self.label_rnn2numWinnders, 3, 2, 1, 1)
        self.rnn2_borderConcurrentWinners = \
            QtWidgets.QSpinBox(self.tab_rnn2_params)
        self.rnn2_borderConcurrentWinners.setMaximum(999)
        self.rnn2_borderConcurrentWinners.setObjectName(
            "rnn2_borderConcurrentWinners")
        self.gridLayout_rnn2borderParams.addWidget(
            self.rnn2_borderConcurrentWinners, 3, 3, 1, 1)
        self.verticalLayout_rnn2prms.addLayout(
            self.gridLayout_rnn2borderParams)
        self.pushButton_rnn2_refreshParams = \
            QtWidgets.QPushButton(self.tab_rnn2_params)
        self.pushButton_rnn2_refreshParams.setObjectName(
            "pushButton_rnn2_refreshParams")
        self.verticalLayout_rnn2prms.addWidget(
            self.pushButton_rnn2_refreshParams)
        self.verticalLayout_rnn2prms.addItem(self.addVSpacer())
        self.tabWidget_rnn2.addTab(self.tab_rnn2_params, "")
        self.tab_rnn2_lr1 = QtWidgets.QWidget()
        self.tab_rnn2_lr1.setObjectName("tab_rnn2_lr1")
        self.verticalLayout_tabrnn2lr1 = \
            QtWidgets.QVBoxLayout(self.tab_rnn2_lr1)
        self.verticalLayout_tabrnn2lr1.setObjectName(
            "verticalLayout_tabrnn2lr1")
        self.graphicsView_rnn2_lr1 = QtWidgets.QGraphicsView(self.tab_rnn2_lr1)
        self.graphicsView_rnn2_lr1.setObjectName("graphicsView_rnn2_lr1")
        self.verticalLayout_tabrnn2lr1.addWidget(self.graphicsView_rnn2_lr1)
        self.tabWidget_rnn2.addTab(self.tab_rnn2_lr1, "")
        self.tab_rnn2_lr2 = QtWidgets.QWidget()
        self.tab_rnn2_lr2.setObjectName("tab_rnn2_lr2")
        self.verticalLayout_tabrnn2lr2 = \
            QtWidgets.QVBoxLayout(self.tab_rnn2_lr2)
        self.verticalLayout_tabrnn2lr2.setObjectName(
            "verticalLayout_tabrnn2lr2")
        self.graphicsView_rnn2_lr2 = QtWidgets.QGraphicsView(self.tab_rnn2_lr2)
        self.graphicsView_rnn2_lr2.setObjectName("graphicsView_rnn2_lr2")
        self.verticalLayout_tabrnn2lr2.addWidget(self.graphicsView_rnn2_lr2)
        self.tabWidget_rnn2.addTab(self.tab_rnn2_lr2, "")
        self.verticalLayout_tabrnn2.addWidget(self.tabWidget_rnn2)
        self.dockWidget_rnn2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8),
                                 self.dockWidget_rnn2)
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
        self.comboBox_ProcessingType.setItemText(
            0, _translate("MainWindow", "Predict"))
        self.comboBox_ProcessingType.setItemText(
            1, _translate("MainWindow", "Novelty filter"))
        self.label_NovFilt.setText(
            _translate("MainWindow", "Novelty filtering with weights gain"))
        self.label_DetectBorder.setText(
            _translate("MainWindow", "and detection border"))
        self.label_DetectBorderStepsPrefix.setText(
            _translate("MainWindow", " for "))
        self.label_DetectBorderStepsSuffix.setText(
            _translate("MainWindow", "steps;"))
        self.label_PredictStepsNumPrefix.setText(
            _translate("MainWindow", "Predict for:"))
        self.label_PredictStepsNumSuffix.setText(
            _translate("MainWindow", "steps;"))
        self.pushButton_CopyModel.setText(
            _translate("MainWindow", "Copy model"))
        self.dockWidget_rnn1.setWindowTitle(
            _translate("MainWindow", "RNN 1"))
        self.pushButton_rnn1_begin.setText(
            _translate("MainWindow", "Bgn"))
        self.pushButton_rnn1_next.setText(
            _translate("MainWindow", "Nxt"))
        self.pushButton_rnn1_end.setText(
            _translate("MainWindow", "End"))
        self.pushButton_rnn1_clear.setText(
            _translate("MainWindow", "Clr"))
        self.rnn1_flag_learn.setText(
            _translate("MainWindow", "Train"))
        self.rnn1_flag_clear_learning.setText(
            _translate("MainWindow", "Clear_mode"))
        self.label_rnn1alpha.setText(_translate("MainWindow", "alpha:"))
        self.label_rnn1h.setText(_translate("MainWindow", "h: "))
        self.label_gInc.setText(_translate("MainWindow", "gInc: "))
        self.label_gDec.setText(_translate("MainWindow", "gDec: "))
        self.rnn1_borderType.setItemText(
            0, _translate("MainWindow", "Const"))
        self.rnn1_borderType.setItemText(
            1, _translate("MainWindow", "Concurrent"))
        self.label_rnn1cbValue.setText(
            _translate("MainWindow", "Value:"))
        self.label_rnn1border.setText(
            _translate("MainWindow", "Excitation border:"))
        self.label_rnn1constBorder.setText(
            _translate("MainWindow", "Const border:"))
        self.label_rnn1concurrentBorder.setText(
            _translate("MainWindow", "Concurrent border:"))
        self.label_rnn1numWinners.setText(
            _translate("MainWindow", "Num of winners:"))
        self.label_InputData.setText(
            _translate("MainWindow", "InputData:"))
        self.pushButton_rnn1_refreshParams.setText(
            _translate("MainWindow", "Refresh params"))
        self.tabWidget_rnn1.setTabText(
            self.tabWidget_rnn1.indexOf(self.tab_rnn1_params),
            _translate("MainWindow", "RNN1 params"))
        self.tabWidget_rnn1.setTabText(
            self.tabWidget_rnn1.indexOf(self.tab_rnn1_lr1),
            _translate("MainWindow", "1st layer"))
        self.tabWidget_rnn1.setTabText(
            self.tabWidget_rnn1.indexOf(self.tab_rnn1_lr2),
            _translate("MainWindow", "2nd layer"))
        self.dockWidget_rnn2.setWindowTitle(
            _translate("MainWindow", "RNN2"))
        self.pushButton_rnn2_next.setText(
            _translate("MainWindow", "Nxt"))
        self.pushButton_rnn2_end.setText(
            _translate("MainWindow", "End"))
        self.label_rnn2alpha.setText(
            _translate("MainWindow", "alpha:"))
        self.label_rnn2h.setText(
            _translate("MainWindow", "h: "))
        self.label_rnn2border.setText(
            _translate("MainWindow", "Excitation border:"))
        self.label_rnn2constBorder.setText(
            _translate("MainWindow", "Const border:"))
        self.rnn2_borderType.setItemText(
            0, _translate("MainWindow", "Const"))
        self.rnn2_borderType.setItemText(
            1, _translate("MainWindow", "Concurrent"))
        self.label_rnn2cbValue.setText(
            _translate("MainWindow", "Value:"))
        self.label_rnn2concurrentBorder.setText(
            _translate("MainWindow", "Concurrent border:"))
        self.label_rnn2numWinnders.setText(
            _translate("MainWindow", "Num of winners:"))
        self.pushButton_rnn2_refreshParams.setText(
            _translate("MainWindow", "Refresh params"))
        self.tabWidget_rnn2.setTabText(self.tabWidget_rnn2.indexOf(
            self.tab_rnn2_params), _translate("MainWindow", "RNN2 params"))
        self.tabWidget_rnn2.setTabText(self.tabWidget_rnn2.indexOf(
            self.tab_rnn2_lr1), _translate("MainWindow", "1st layer"))
        self.tabWidget_rnn2.setTabText(self.tabWidget_rnn2.indexOf(
            self.tab_rnn2_lr2), _translate("MainWindow", "2nd layer"))
