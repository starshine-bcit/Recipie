# Form implementation generated from reading ui file '.\testing\recipie_test\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutTop = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTop.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayoutTop.setObjectName("horizontalLayoutTop")
        self.labelRecipieLogo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRecipieLogo.sizePolicy().hasHeightForWidth())
        self.labelRecipieLogo.setSizePolicy(sizePolicy)
        self.labelRecipieLogo.setMaximumSize(QtCore.QSize(150, 75))
        self.labelRecipieLogo.setText("")
        self.labelRecipieLogo.setPixmap(QtGui.QPixmap(".\\testing\\recipie_test\\../../../image/RecipieLogo.png"))
        self.labelRecipieLogo.setScaledContents(True)
        self.labelRecipieLogo.setObjectName("labelRecipieLogo")
        self.horizontalLayoutTop.addWidget(self.labelRecipieLogo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayoutTop.addItem(spacerItem)
        self.labelTopBarText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTopBarText.sizePolicy().hasHeightForWidth())
        self.labelTopBarText.setSizePolicy(sizePolicy)
        self.labelTopBarText.setMinimumSize(QtCore.QSize(0, 75))
        self.labelTopBarText.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(11)
        self.labelTopBarText.setFont(font)
        self.labelTopBarText.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.labelTopBarText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTopBarText.setWordWrap(True)
        self.labelTopBarText.setObjectName("labelTopBarText")
        self.horizontalLayoutTop.addWidget(self.labelTopBarText)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayoutTop.addItem(spacerItem1)
        self.horizontalLayoutTop.setStretch(1, 1)
        self.horizontalLayoutTop.setStretch(2, 3)
        self.horizontalLayoutTop.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayoutTop)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidgetSearch = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        self.tabWidgetSearch.setFont(font)
        self.tabWidgetSearch.setObjectName("tabWidgetSearch")
        self.TabSearchInput = QtWidgets.QWidget()
        self.TabSearchInput.setObjectName("TabSearchInput")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.TabSearchInput)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayoutEnterIngredient = QtWidgets.QHBoxLayout()
        self.horizontalLayoutEnterIngredient.setObjectName("horizontalLayoutEnterIngredient")
        self.lineEditIngredientEntry = QtWidgets.QLineEdit(self.TabSearchInput)
        self.lineEditIngredientEntry.setObjectName("lineEditIngredientEntry")
        self.horizontalLayoutEnterIngredient.addWidget(self.lineEditIngredientEntry)
        self.commandLinkButtonEnterIngredient = QtWidgets.QCommandLinkButton(self.TabSearchInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButtonEnterIngredient.sizePolicy().hasHeightForWidth())
        self.commandLinkButtonEnterIngredient.setSizePolicy(sizePolicy)
        self.commandLinkButtonEnterIngredient.setMinimumSize(QtCore.QSize(20, 20))
        self.commandLinkButtonEnterIngredient.setMaximumSize(QtCore.QSize(30, 40))
        self.commandLinkButtonEnterIngredient.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.commandLinkButtonEnterIngredient.setText("")
        self.commandLinkButtonEnterIngredient.setObjectName("commandLinkButtonEnterIngredient")
        self.horizontalLayoutEnterIngredient.addWidget(self.commandLinkButtonEnterIngredient)
        self.verticalLayout_6.addLayout(self.horizontalLayoutEnterIngredient)
        self.listWidgetSearchInput = QtWidgets.QListWidget(self.TabSearchInput)
        self.listWidgetSearchInput.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidgetSearchInput.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.listWidgetSearchInput.setObjectName("listWidgetSearchInput")
        self.verticalLayout_6.addWidget(self.listWidgetSearchInput)
        self.frameSearchOptions = QtWidgets.QFrame(self.TabSearchInput)
        self.frameSearchOptions.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameSearchOptions.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frameSearchOptions.setObjectName("frameSearchOptions")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameSearchOptions)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayoutRadioHolder = QtWidgets.QHBoxLayout()
        self.horizontalLayoutRadioHolder.setObjectName("horizontalLayoutRadioHolder")
        self.radioButtonInclusive = QtWidgets.QRadioButton(self.frameSearchOptions)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        self.radioButtonInclusive.setFont(font)
        self.radioButtonInclusive.setChecked(True)
        self.radioButtonInclusive.setObjectName("radioButtonInclusive")
        self.horizontalLayoutRadioHolder.addWidget(self.radioButtonInclusive)
        self.radioButtonExclusive = QtWidgets.QRadioButton(self.frameSearchOptions)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        self.radioButtonExclusive.setFont(font)
        self.radioButtonExclusive.setObjectName("radioButtonExclusive")
        self.horizontalLayoutRadioHolder.addWidget(self.radioButtonExclusive)
        self.horizontalLayoutRadioHolder.setStretch(0, 1)
        self.horizontalLayoutRadioHolder.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayoutRadioHolder)
        self.horizontalLayoutSearchButtonHolder = QtWidgets.QHBoxLayout()
        self.horizontalLayoutSearchButtonHolder.setObjectName("horizontalLayoutSearchButtonHolder")
        self.pushButtonResetSearch = QtWidgets.QPushButton(self.frameSearchOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonResetSearch.sizePolicy().hasHeightForWidth())
        self.pushButtonResetSearch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        self.pushButtonResetSearch.setFont(font)
        self.pushButtonResetSearch.setObjectName("pushButtonResetSearch")
        self.horizontalLayoutSearchButtonHolder.addWidget(self.pushButtonResetSearch)
        self.pushButtonRemoveSelected = QtWidgets.QPushButton(self.frameSearchOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRemoveSelected.sizePolicy().hasHeightForWidth())
        self.pushButtonRemoveSelected.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        self.pushButtonRemoveSelected.setFont(font)
        self.pushButtonRemoveSelected.setObjectName("pushButtonRemoveSelected")
        self.horizontalLayoutSearchButtonHolder.addWidget(self.pushButtonRemoveSelected)
        self.horizontalLayoutSearchButtonHolder.setStretch(0, 1)
        self.horizontalLayoutSearchButtonHolder.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayoutSearchButtonHolder)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_6.addWidget(self.frameSearchOptions)
        self.verticalLayout_6.setStretch(1, 1)
        self.tabWidgetSearch.addTab(self.TabSearchInput, "")
        self.tabFilter = QtWidgets.QWidget()
        self.tabFilter.setObjectName("tabFilter")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabFilter)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkBox = QtWidgets.QCheckBox(self.tabFilter)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_7.addWidget(self.checkBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.frame = QtWidgets.QFrame(self.tabFilter)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonResetFilters = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonResetFilters.sizePolicy().hasHeightForWidth())
        self.pushButtonResetFilters.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        self.pushButtonResetFilters.setFont(font)
        self.pushButtonResetFilters.setObjectName("pushButtonResetFilters")
        self.verticalLayout_2.addWidget(self.pushButtonResetFilters, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_7.addWidget(self.frame)
        self.tabWidgetSearch.addTab(self.tabFilter, "")
        self.horizontalLayout.addWidget(self.tabWidgetSearch)
        self.tabWidgetRecipe = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.tabWidgetRecipe.setFont(font)
        self.tabWidgetRecipe.setUsesScrollButtons(False)
        self.tabWidgetRecipe.setObjectName("tabWidgetRecipe")
        self.tabRecipeDisplay = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabRecipeDisplay.sizePolicy().hasHeightForWidth())
        self.tabRecipeDisplay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.tabRecipeDisplay.setFont(font)
        self.tabRecipeDisplay.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.tabRecipeDisplay.setStatusTip("")
        self.tabRecipeDisplay.setWhatsThis("")
        self.tabRecipeDisplay.setAccessibleName("")
        self.tabRecipeDisplay.setObjectName("tabRecipeDisplay")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabRecipeDisplay)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelRecipeName = QtWidgets.QLabel(self.tabRecipeDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRecipeName.sizePolicy().hasHeightForWidth())
        self.labelRecipeName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro")
        font.setPointSize(24)
        self.labelRecipeName.setFont(font)
        self.labelRecipeName.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.labelRecipeName.setObjectName("labelRecipeName")
        self.verticalLayout_3.addWidget(self.labelRecipeName)
        self.line = QtWidgets.QFrame(self.tabRecipeDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.labelRecipeIngredients = QtWidgets.QLabel(self.tabRecipeDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRecipeIngredients.sizePolicy().hasHeightForWidth())
        self.labelRecipeIngredients.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro")
        font.setPointSize(11)
        self.labelRecipeIngredients.setFont(font)
        self.labelRecipeIngredients.setObjectName("labelRecipeIngredients")
        self.verticalLayout_3.addWidget(self.labelRecipeIngredients)
        self.textBrowserRecipeIngredients = QtWidgets.QTextBrowser(self.tabRecipeDisplay)
        self.textBrowserRecipeIngredients.setMinimumSize(QtCore.QSize(300, 100))
        self.textBrowserRecipeIngredients.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        self.textBrowserRecipeIngredients.setFont(font)
        self.textBrowserRecipeIngredients.setAutoFormatting(QtWidgets.QTextEdit.AutoFormattingFlag.AutoNone)
        self.textBrowserRecipeIngredients.setAcceptRichText(False)
        self.textBrowserRecipeIngredients.setObjectName("textBrowserRecipeIngredients")
        self.verticalLayout_3.addWidget(self.textBrowserRecipeIngredients)
        self.labelRecipeDirections = QtWidgets.QLabel(self.tabRecipeDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRecipeDirections.sizePolicy().hasHeightForWidth())
        self.labelRecipeDirections.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro")
        font.setPointSize(11)
        self.labelRecipeDirections.setFont(font)
        self.labelRecipeDirections.setObjectName("labelRecipeDirections")
        self.verticalLayout_3.addWidget(self.labelRecipeDirections)
        self.textBrowserRecipeDirections = QtWidgets.QTextBrowser(self.tabRecipeDisplay)
        self.textBrowserRecipeDirections.setMinimumSize(QtCore.QSize(300, 100))
        self.textBrowserRecipeDirections.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        self.textBrowserRecipeDirections.setFont(font)
        self.textBrowserRecipeDirections.setObjectName("textBrowserRecipeDirections")
        self.verticalLayout_3.addWidget(self.textBrowserRecipeDirections)
        self.horizontalLayoutBottomRecipeDisplay = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBottomRecipeDisplay.setObjectName("horizontalLayoutBottomRecipeDisplay")
        self.pushButtonDisplayRecipeNewWindow = QtWidgets.QPushButton(self.tabRecipeDisplay)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.pushButtonDisplayRecipeNewWindow.setFont(font)
        self.pushButtonDisplayRecipeNewWindow.setObjectName("pushButtonDisplayRecipeNewWindow")
        self.horizontalLayoutBottomRecipeDisplay.addWidget(self.pushButtonDisplayRecipeNewWindow)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayoutBottomRecipeDisplay.addItem(spacerItem3)
        self.pushButtonRecipeClear = QtWidgets.QPushButton(self.tabRecipeDisplay)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.pushButtonRecipeClear.setFont(font)
        self.pushButtonRecipeClear.setObjectName("pushButtonRecipeClear")
        self.horizontalLayoutBottomRecipeDisplay.addWidget(self.pushButtonRecipeClear)
        self.pushButtonRandom = QtWidgets.QPushButton(self.tabRecipeDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRandom.sizePolicy().hasHeightForWidth())
        self.pushButtonRandom.setSizePolicy(sizePolicy)
        self.pushButtonRandom.setMinimumSize(QtCore.QSize(110, 25))
        self.pushButtonRandom.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.pushButtonRandom.setFont(font)
        self.pushButtonRandom.setObjectName("pushButtonRandom")
        self.horizontalLayoutBottomRecipeDisplay.addWidget(self.pushButtonRandom)
        self.verticalLayout_3.addLayout(self.horizontalLayoutBottomRecipeDisplay)
        self.tabWidgetRecipe.addTab(self.tabRecipeDisplay, "")
        self.tabSearchResults = QtWidgets.QWidget()
        self.tabSearchResults.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.tabSearchResults.setObjectName("tabSearchResults")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSearchResults)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidgetSearchResults = QtWidgets.QListWidget(self.tabSearchResults)
        self.listWidgetSearchResults.setObjectName("listWidgetSearchResults")
        self.verticalLayout_4.addWidget(self.listWidgetSearchResults)
        self.tabWidgetRecipe.addTab(self.tabSearchResults, "")
        self.horizontalLayout.addWidget(self.tabWidgetRecipe)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSearch = QtWidgets.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setIconVisibleInMenu(False)
        self.actionExit.setObjectName("actionExit")
        self.actionRandom = QtGui.QAction(MainWindow)
        self.actionRandom.setIconVisibleInMenu(False)
        self.actionRandom.setObjectName("actionRandom")
        self.actionReset_Search = QtGui.QAction(MainWindow)
        self.actionReset_Search.setIconVisibleInMenu(False)
        self.actionReset_Search.setObjectName("actionReset_Search")
        self.actionRemove_Selected = QtGui.QAction(MainWindow)
        self.actionRemove_Selected.setIconVisibleInMenu(False)
        self.actionRemove_Selected.setObjectName("actionRemove_Selected")
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setIconVisibleInMenu(False)
        self.actionPrint.setObjectName("actionPrint")
        self.menuFile.addAction(self.actionRandom)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionExit)
        self.menuSearch.addAction(self.actionReset_Search)
        self.menuSearch.addAction(self.actionRemove_Selected)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidgetSearch.setCurrentIndex(0)
        self.tabWidgetRecipe.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "recipie --BETA--"))
        MainWindow.setToolTip(_translate("MainWindow", "Recipie"))
        self.labelTopBarText.setText(_translate("MainWindow", "Welcome to Recipie Beta, please hit \'Random Recipe to try it out!"))
        self.lineEditIngredientEntry.setPlaceholderText(_translate("MainWindow", "Enter Ingredients Here"))
        self.radioButtonInclusive.setText(_translate("MainWindow", "Partial"))
        self.radioButtonExclusive.setText(_translate("MainWindow", "Exact"))
        self.pushButtonResetSearch.setText(_translate("MainWindow", "Reset Search"))
        self.pushButtonRemoveSelected.setText(_translate("MainWindow", "Remove Selected"))
        self.tabWidgetSearch.setTabText(self.tabWidgetSearch.indexOf(self.TabSearchInput), _translate("MainWindow", "Search"))
        self.checkBox.setText(_translate("MainWindow", "CheckBoxDietary"))
        self.pushButtonResetFilters.setText(_translate("MainWindow", "Reset Filters"))
        self.tabWidgetSearch.setTabText(self.tabWidgetSearch.indexOf(self.tabFilter), _translate("MainWindow", "Filter"))
        self.tabRecipeDisplay.setToolTip(_translate("MainWindow", "Recipe"))
        self.labelRecipeName.setText(_translate("MainWindow", "Recipe Name"))
        self.labelRecipeIngredients.setText(_translate("MainWindow", "Ingredients:"))
        self.labelRecipeDirections.setText(_translate("MainWindow", "Directions:"))
        self.pushButtonDisplayRecipeNewWindow.setText(_translate("MainWindow", "Open In New Window"))
        self.pushButtonDisplayRecipeNewWindow.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.pushButtonRecipeClear.setText(_translate("MainWindow", "Clear Display"))
        self.pushButtonRandom.setToolTip(_translate("MainWindow", "Get A Random Recipe"))
        self.pushButtonRandom.setText(_translate("MainWindow", "Random Recipe"))
        self.tabWidgetRecipe.setTabText(self.tabWidgetRecipe.indexOf(self.tabRecipeDisplay), _translate("MainWindow", "Recipe"))
        self.tabWidgetRecipe.setTabText(self.tabWidgetRecipe.indexOf(self.tabSearchResults), _translate("MainWindow", "Search Results"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSearch.setTitle(_translate("MainWindow", "Search"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRandom.setText(_translate("MainWindow", "Random"))
        self.actionReset_Search.setText(_translate("MainWindow", "Reset Search"))
        self.actionRemove_Selected.setText(_translate("MainWindow", "Remove Selected"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
