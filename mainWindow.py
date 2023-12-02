# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowzhvYEn.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QSize(800, 600))
        mainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.dropshadowFrame = QFrame(self.centralwidget)
        self.dropshadowFrame.setObjectName(u"dropshadowFrame")
        self.dropshadowFrame.setStyleSheet(u"background-color: #2e3440;\n"
"border-radius: 5px;")
        self.dropshadowFrame.setFrameShape(QFrame.NoFrame)
        self.dropshadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.dropshadowFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.dropshadowFrame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 30))
        self.titleBar.setStyleSheet(u"background-color:none;")
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleFrame = QFrame(self.titleBar)
        self.titleFrame.setObjectName(u"titleFrame")
        font = QFont()
        self.titleFrame.setFont(font)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.title_label = QLabel(self.titleFrame)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: #81a1c1;")

        self.horizontalLayout_2.addWidget(self.title_label)


        self.horizontalLayout.addWidget(self.titleFrame)

        self.titleButtons = QFrame(self.titleBar)
        self.titleButtons.setObjectName(u"titleButtons")
        self.titleButtons.setMaximumSize(QSize(70, 16777215))
        self.titleButtons.setFrameShape(QFrame.StyledPanel)
        self.titleButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titleButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minButton = QPushButton(self.titleButtons)
        self.minButton.setObjectName(u"minButton")
        self.minButton.setMinimumSize(QSize(16, 16))
        self.minButton.setMaximumSize(QSize(16, 16))
        self.minButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	background-color: #ebcb8b;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: #a3be8c;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.minButton)

        self.closeButton = QPushButton(self.titleButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(16, 16))
        self.closeButton.setMaximumSize(QSize(16, 16))
        self.closeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: #d08770;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: #bf616a;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.titleButtons)


        self.verticalLayout.addWidget(self.titleBar)

        self.mainInterface = QFrame(self.dropshadowFrame)
        self.mainInterface.setObjectName(u"mainInterface")
        self.mainInterface.setFont(font)
        self.mainInterface.setStyleSheet(u"background-color:none;")
        self.mainInterface.setFrameShape(QFrame.NoFrame)
        self.mainInterface.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainInterface)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedHome = QStackedWidget(self.mainInterface)
        self.stackedHome.setObjectName(u"stackedHome")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.verticalLayout_4 = QVBoxLayout(self.pageHome)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.pageHome)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.scanFrame = QFrame(self.frame_content_home)
        self.scanFrame.setObjectName(u"scanFrame")
        self.scanFrame.setGeometry(QRect(140, 180, 160, 160))
        self.scanFrame.setMinimumSize(QSize(160, 160))
        self.scanFrame.setMaximumSize(QSize(160, 160))
        self.scanFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.scanFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: 5px solid #81a1c1;\n"
"	border-radius: 80px;\n"
"}\n"
"QFrame:hover\n"
"{\n"
"	border: 5px solid #b48ead;\n"
"}\n"
"	")
        self.scanFrame.setFrameShape(QFrame.StyledPanel)
        self.scanFrame.setFrameShadow(QFrame.Raised)
        self.scanlabel = QLabel(self.scanFrame)
        self.scanlabel.setObjectName(u"scanlabel")
        self.scanlabel.setGeometry(QRect(30, 100, 101, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.scanlabel.setFont(font2)
        self.scanlabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"\n"
"	")
        self.scanlabel.setAlignment(Qt.AlignCenter)
        self.scanImg = QLabel(self.scanFrame)
        self.scanImg.setObjectName(u"scanImg")
        self.scanImg.setGeometry(QRect(30, 10, 100, 100))
        self.scanImg.setMinimumSize(QSize(100, 100))
        self.scanImg.setMaximumSize(QSize(100, 100))
        self.scanImg.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(0, 255, 38);\n"
"	border:none;\n"
"}\n"
"")
        self.scanImg.setPixmap(QPixmap(u"img/search.png"))
        self.scanImg.setScaledContents(True)
        self.updateFrame = QFrame(self.frame_content_home)
        self.updateFrame.setObjectName(u"updateFrame")
        self.updateFrame.setGeometry(QRect(467, 181, 160, 160))
        self.updateFrame.setMinimumSize(QSize(160, 160))
        self.updateFrame.setMaximumSize(QSize(160, 160))
        self.updateFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: 5px solid #81a1c1;\n"
"	border-radius: 80px;\n"
"}\n"
"QFrame:hover\n"
"{\n"
"	border: 5px solid #b48ead;\n"
"}\n"
"	")
        self.updateFrame.setFrameShape(QFrame.StyledPanel)
        self.updateFrame.setFrameShadow(QFrame.Raised)
        self.updateImg = QLabel(self.updateFrame)
        self.updateImg.setObjectName(u"updateImg")
        self.updateImg.setGeometry(QRect(30, 10, 100, 100))
        self.updateImg.setMinimumSize(QSize(100, 100))
        self.updateImg.setMaximumSize(QSize(100, 100))
        self.updateImg.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(0, 255, 38);\n"
"	border:none;\n"
"}\n"
"")
        self.updateImg.setPixmap(QPixmap(u"img/update.png"))
        self.updateImg.setScaledContents(True)
        self.updateLabel = QLabel(self.updateFrame)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(50, 110, 61, 21))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.updateLabel.setFont(font3)
        self.updateLabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"\n"
"	")
        self.aboutLabel = QLabel(self.frame_content_home)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setGeometry(QRect(20, 480, 31, 31))
        self.aboutLabel.setFont(font1)
        self.aboutLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutLabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(0, 182, 24);\n"
"	border:none;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:rgb(0, 255, 38);\n"
"	border:1px solid rgb(255, 255, 255);\n"
"}")
        self.aboutLabel.setPixmap(QPixmap(u"img/info.png"))
        self.aboutLabel.setScaledContents(True)
        self.voyagerHome = QLabel(self.frame_content_home)
        self.voyagerHome.setObjectName(u"voyagerHome")
        self.voyagerHome.setGeometry(QRect(0, -10, 801, 551))
        self.voyagerHome.setPixmap(QPixmap(u"img/voyager.png"))
        self.voyagerHome.setScaledContents(True)
        self.voyagerHome.raise_()
        self.scanFrame.raise_()
        self.updateFrame.raise_()
        self.aboutLabel.raise_()

        self.verticalLayout_4.addWidget(self.frame_content_home)

        self.stackedHome.addWidget(self.pageHome)
        self.pageScan = QWidget()
        self.pageScan.setObjectName(u"pageScan")
        self.verticalLayout_5 = QVBoxLayout(self.pageScan)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedHome.addWidget(self.pageScan)
        self.pageUpdate = QWidget()
        self.pageUpdate.setObjectName(u"pageUpdate")
        self.pageUpdate.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.pageUpdate)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedHome.addWidget(self.pageUpdate)
        self.pageAbout = QWidget()
        self.pageAbout.setObjectName(u"pageAbout")
        self.verticalLayout_7 = QVBoxLayout(self.pageAbout)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frameHomeAbout = QFrame(self.pageAbout)
        self.frameHomeAbout.setObjectName(u"frameHomeAbout")
        self.frameHomeAbout.setMinimumSize(QSize(764, 169))
        self.frameHomeAbout.setMaximumSize(QSize(764, 169))
        self.frameHomeAbout.setFrameShape(QFrame.StyledPanel)
        self.frameHomeAbout.setFrameShadow(QFrame.Raised)
        self.homeButtonAbout = QPushButton(self.frameHomeAbout)
        self.homeButtonAbout.setObjectName(u"homeButtonAbout")
        self.homeButtonAbout.setGeometry(QRect(9, 20, 182, 120))
        self.homeButtonAbout.setMinimumSize(QSize(120, 120))
        self.homeButtonAbout.setFont(font3)
        self.homeButtonAbout.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButtonAbout.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")
        icon = QIcon()
        icon.addFile(u"img/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButtonAbout.setIcon(icon)
        self.homeButtonAbout.setIconSize(QSize(50, 50))
        self.moonG3 = QLabel(self.frameHomeAbout)
        self.moonG3.setObjectName(u"moonG3")
        self.moonG3.setGeometry(QRect(630, 0, 191, 171))
        self.moonG3.setPixmap(QPixmap(u"img/pixelmoon.png"))
        self.moonG3.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.frameHomeAbout)

        self.frameAboutContent = QFrame(self.pageAbout)
        self.frameAboutContent.setObjectName(u"frameAboutContent")
        self.frameAboutContent.setFrameShape(QFrame.StyledPanel)
        self.frameAboutContent.setFrameShadow(QFrame.Raised)
        self.ProjectTitle = QLabel(self.frameAboutContent)
        self.ProjectTitle.setObjectName(u"ProjectTitle")
        self.ProjectTitle.setGeometry(QRect(0, 20, 211, 21))
        self.ProjectTitle.setMinimumSize(QSize(0, 21))
        self.ProjectTitle.setMaximumSize(QSize(16777215, 21))
        self.ProjectTitle.setFont(font3)
        self.ProjectTitle.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"\n"
"	")
        self.ProjectTitle.setAlignment(Qt.AlignCenter)
        self.AboutGithub = QLabel(self.frameAboutContent)
        self.AboutGithub.setObjectName(u"AboutGithub")
        self.AboutGithub.setGeometry(QRect(10, 280, 101, 41))
        self.AboutGithub.setCursor(QCursor(Qt.PointingHandCursor))
        self.AboutGithub.setStyleSheet(u"")
        self.AboutGithub.setPixmap(QPixmap(u"img/GitHub.png"))
        self.AboutGithub.setScaledContents(True)
        self.AboutGPL = QLabel(self.frameAboutContent)
        self.AboutGPL.setObjectName(u"AboutGPL")
        self.AboutGPL.setGeometry(QRect(140, 280, 91, 41))
        self.AboutGPL.setPixmap(QPixmap(u"img/gpl.png"))
        self.AboutGPL.setScaledContents(True)
        self.label = QLabel(self.frameAboutContent)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 381, 16))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"")
        self.label_2 = QLabel(self.frameAboutContent)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 741, 161))
        font5 = QFont()
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"")
        self.label_3 = QLabel(self.frameAboutContent)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 571, 16))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.frameAboutContent)

        self.stackedHome.addWidget(self.pageAbout)
        self.pageQuarantine = QWidget()
        self.pageQuarantine.setObjectName(u"pageQuarantine")
        self.verticalLayout_8 = QVBoxLayout(self.pageQuarantine)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedHome.addWidget(self.pageQuarantine)

        self.verticalLayout_3.addWidget(self.stackedHome)


        self.verticalLayout.addWidget(self.mainInterface)

        self.statusBar = QFrame(self.dropshadowFrame)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMaximumSize(QSize(16777215, 30))
        self.statusBar.setStyleSheet(u"background-color:none;")
        self.statusBar.setFrameShape(QFrame.NoFrame)
        self.statusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.engineVer = QLabel(self.statusBar)
        self.engineVer.setObjectName(u"engineVer")
        font6 = QFont()
        font6.setPointSize(7)
        font6.setBold(True)
        self.engineVer.setFont(font6)
        self.engineVer.setStyleSheet(u"color: #81a1c1;")

        self.horizontalLayout_6.addWidget(self.engineVer)


        self.verticalLayout.addWidget(self.statusBar)


        self.drop_shadow_layout.addWidget(self.dropshadowFrame)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.stackedHome.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ClamGuard", None))
        self.title_label.setText(QCoreApplication.translate("mainWindow", u"POTHOLE DETECTION", None))
        self.minButton.setText("")
        self.closeButton.setText("")
#if QT_CONFIG(tooltip)
        self.scanFrame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.scanlabel.setText(QCoreApplication.translate("mainWindow", u"BROWSE", None))
        self.scanImg.setText("")
#if QT_CONFIG(tooltip)
        self.updateFrame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.updateImg.setText("")
        self.updateLabel.setText(QCoreApplication.translate("mainWindow", u"START", None))
#if QT_CONFIG(tooltip)
        self.aboutLabel.setToolTip(QCoreApplication.translate("mainWindow", u"About ClamGuard Project", None))
#endif // QT_CONFIG(tooltip)
        self.aboutLabel.setText("")
        self.voyagerHome.setText("")
        self.homeButtonAbout.setText("")
        self.moonG3.setText("")
        self.ProjectTitle.setText(QCoreApplication.translate("mainWindow", u"POTHOLE DETECTION", None))
        self.AboutGithub.setText("")
        self.AboutGPL.setText("")
        self.label.setText(QCoreApplication.translate("mainWindow", u"An AI Powered POTHOLE DETECTION PROJECT", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Developed by: \n"
"Sreelekshmi Prasannakumar, Vignesh Mahesh, Unnikrishnan V H, Sreedev B.\n"
"", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Developed using PySide6 and Python3. ", None))
        self.engineVer.setText(QCoreApplication.translate("mainWindow", u"POTHOLE DETECTION Version: 0.1.1", None))
    # retranslateUi

