# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'interface.ui'
##
# Created by: Qt User Interface Compiler version 6.4.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
                               QVBoxLayout, QWidget)
import resouce_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(746, 711)
        MainWindow.setStyleSheet(u"*{\n"
                                 "border: none;\n"
                                 "background-color: transparent;\n"
                                 "background: transparent;\n"
                                 "padding:0;\n"
                                 "margin:0;\n"
                                 "color:#fff;\n"
                                 "\n"
                                 "}\n"
                                 "#centralwidget{\n"
                                 "	background-color: #2c313c;\n"
                                 "}\n"
                                 "\n"
                                 "#leftMenuSubContainer{\n"
                                 "	background-color: #006D77;\n"
                                 "\n"
                                 "}\n"
                                 "#leftMenuSubContainer QPushButton{\n"
                                 "text-align: left;\n"
                                 "padding: 5px 10px;\n"
                                 "border-top-left-radius: 10px;\n"
                                 "border-bottom-left-radius: 10px;\n"
                                 "}\n"
                                 "#centerMenuSubConatiner{\n"
                                 "backgorund-color: #2c313c;\n"
                                 "}\n"
                                 "#frame_4{\n"
                                 "background-color:#006D77;\n"
                                 "border-radius: 10px\n"
                                 "}\n"
                                 "\n"
                                 "#headerContainer{\n"
                                 "background-color: #2c313c\n"
                                 "}\n"
                                 "#mainBodyContent{\n"
                                 "background-color: #3D4352\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, -1)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setEnabled(True)
        self.menuBtn.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg",
                     QSize(), QIcon.Normal, QIcon.On)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn, 0, Qt.AlignTop)

        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icons/home.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/list.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.dataBtn)

        self.reportBtn = QPushButton(self.frame_2)
        self.reportBtn.setObjectName(u"reportBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/printer.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.reportBtn.setIcon(icon3)
        self.reportBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.reportBtn)

        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.infoBtn.setIcon(icon4)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/help-circle.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.helpBtn.setIcon(icon5)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.helpBtn)

        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.verticalLayout_4.addWidget(self.leftMenuSubContainer)

        self.horizontalLayout.addWidget(
            self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy)
        self.centerMenuContainer.setMinimumSize(QSize(0, 0))
        self.centerMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.centerMenuSubContainer.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/x-circle.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignRight)

        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setEnabled(True)
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(
            self.label_3, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.verticalLayout_5.addWidget(
            self.centerMenuSubContainer, 0, Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        self.mainBodyContainer.setFont(font)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        sizePolicy2.setHeightForWidth(
            self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(30, 30))
        self.label_4.setPixmap(QPixmap(u":/images/twitter-logo.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalLayout_4.addWidget(
            self.frame_5, 0, Qt.AlignLeft | Qt.AlignTop)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimizeWinBtn = QPushButton(self.frame_7)
        self.minimizeWinBtn.setObjectName(u"minimizeWinBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/minus.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.minimizeWinBtn.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.minimizeWinBtn)

        self.restoreWinBtn = QPushButton(self.frame_7)
        self.restoreWinBtn.setObjectName(u"restoreWinBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/square.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.restoreWinBtn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.restoreWinBtn)

        self.closeWinBtn = QPushButton(self.frame_7)
        self.closeWinBtn.setObjectName(u"closeWinBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.On)
        self.closeWinBtn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.closeWinBtn)

        self.horizontalLayout_4.addWidget(
            self.frame_7, 0, Qt.AlignRight | Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.mainContentContainer = QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName(u"mainContentContainer")
        self.verticalLayout_11 = QVBoxLayout(self.mainContentContainer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stackedWidget_2 = QStackedWidget(self.mainContentContainer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(
            self.label_11, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.page_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(100, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.searchBtn = QPushButton(self.frame_6)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(100, 20))
        self.searchBtn.setStyleSheet(u"background-color: rgb(191, 191, 191);\n"
                                     "color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.searchBtn)

        self.verticalLayout_12.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.page_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_15.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_15.addWidget(self.label_10)

        self.verticalLayout_12.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.holder = QWidget(self.page_3)
        self.holder.setObjectName(u"holder")
        self.verticalLayout_16 = QVBoxLayout(self.holder)
        self.scroll_area = QScrollArea(self.holder)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.verticalLayout_16.addWidget(self.scroll_area)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scroll_conatiner = QWidget()

        self.scroll_layout = QVBoxLayout(self.scroll_conatiner)
        self.scroll_area.setWidget(self.scroll_conatiner)

        self.verticalLayout_12.addWidget(self.holder)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_14 = QVBoxLayout(self.page_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.verticalLayout_14.addWidget(
            self.label_7, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.frame_9 = QFrame(self.page_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy4)
        self.frame_9.setMinimumSize(QSize(600, 220))
        self.frame_9.setMaximumSize(QSize(600, 600))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(30, 0, -1, 0)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.label_13)

        self.verticalLayout_14.addWidget(
            self.frame_9, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.frame_10 = QFrame(self.page_4)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy6)
        self.frame_10.setMinimumSize(QSize(150, 350))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/images/polarityChart.png"))
        self.label_14.setScaledContents(True)

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/images/ranks.png"))
        self.label_16.setScaledContents(True)

        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u":/images/Figure_1.jpeg"))
        self.label_17.setScaledContents(True)

        self.gridLayout.addWidget(self.label_17, 1, 1, 1, 1)

        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(
            QPixmap(u":/images/subjectivitychartforpres.png"))
        self.label_15.setScaledContents(True)

        self.gridLayout.addWidget(self.label_15, 0, 1, 1, 1)

        self.verticalLayout_14.addWidget(self.frame_10, 0, Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_13 = QVBoxLayout(self.page_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(
            self.label_8, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.stackedWidget_2.addWidget(self.page_5)

        self.verticalLayout_11.addWidget(self.stackedWidget_2, 0, Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.mainContentContainer)

        self.verticalLayout_9.addWidget(self.mainBodyContent)

        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.menuBtn.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
# if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
# if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Home", None))
# if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Data Analysis", None))
# if QT_CONFIG(tooltip)
        self.reportBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"View Report", None))
#endif // QT_CONFIG(tooltip)
        self.reportBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Report", None))
# if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"More Information", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Information", None))
        self.helpBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"More Menu", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Information", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Help", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Twitter Sentiment Analysis", None))
        self.minimizeWinBtn.setText("")
        self.restoreWinBtn.setText("")
        self.closeWinBtn.setText("")
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Data Analysis", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Enter a topic, hashtage, or name you would like to have analyzed. When done, hit Search to view results.", None))
        self.lineEdit.setText("")
        self.searchBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Search", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"The Polarity Score is: ", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"The Subjectivity score is: ", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Top 25 Movies of 2022 Data Analysis", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"The Menu \n"
                                                         "Puss in Boots: The Last Wish \n"
                                                         "Glass Onion: A Knives Out Mystery \n"
                                                         "The Invitation \n"
                                                         "Smile \n"
                                                         "Don\u2019t Worry Darling \n"
                                                         "Spirited \n"
                                                         "Ticket to Paradise \n"
                                                         "Top Gun: Maverick \n"
                                                         "Bullet Train #BulletTrainMovie\n"
                                                         "Where the Crawdads Sing \n"
                                                         "Elvis \n"
                                                         "Minions: The Rise of Gru\n"
                                                         "", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"My Policeman \n"
                                                         "Death on the Nile \n"
                                                         "Doctor Strange in the Multiverse of Madness \n"
                                                         "Jurassic World: Dominion \n"
                                                         "Avatar: The Way of Water \n"
                                                         "Black Panther: Wakanda Forever \n"
                                                         "A Man Called Otto \n"
                                                         "Pinocchio \n"
                                                         "The Batman \n"
                                                         "Crush \n"
                                                         "Scream 5 \n"
                                                         "Halloween Ends \n"
                                                         "", None))
        self.label_14.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_15.setText("")
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Reports", None))
    # retranslateUi
