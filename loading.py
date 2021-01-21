from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import webget
import re
try:
    def get():


        class Ui_MainWindow(object):
            def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 200)
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
                MainWindow.setPalette(palette)
                MainWindow.setAutoFillBackground(True)
                font = QtGui.QFont()
                font.setPointSize(20)
                MainWindow.setFont(font)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/untitled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                MainWindow.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(-40, 10, 1000, 1000))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("../../图片/u=3087922616,849567065&fm=26&gp=0.jpg"))
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(0, 20, 801, 131))
                font = QtGui.QFont()
                font.setPointSize(32)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

            def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "加载中……"))
                self.label_2.setText(_translate("MainWindow", "正在加载天气，请稍后……"))
            def close():
                mainwindow.close()
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

        webside = webget.get(webside = r"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=80035161_2_dg&wd=%E5%A4%A9%E6%B0%94&oq=%25E5%25A4%25A9%25E6%25B0%2594&rsv_pq=8873d4610004b455&rsv_t=1c88w5krAsUOHNOyw1MAFR90Vjnt%2FxwxsMotIghXubeTv6TXY%2FWARBEh0RwfzB6qfzjcyQ&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t", rod = "")
        webside = str(webside)
        def run():
            MainWindow.close()
        with open("webcode.txt", "w", encoding = "utf-8") as file:
            file.write(webside)
        with open("webcode.txt", encoding = "utf-8") as file:
            for x in range(4000):
                y = file.readline()
                y = ""
            for x in range(1000):
                y = y + file.readline() + "\n"
        c = re.findall(r'>.{1,10}<', y)
        start = 0
        bre = False
        bret = False
        for list_ in c:
            start += 1
            if "(实时)" in list_:
                w = list_
                bre = True
            elif "℃" in list_ and not bret:
                degree = c[start-2]
                degree = degree[1:-1]
                degreet = c[start-1]
                degreet = degreet[1:-1]
                degree = degree + degreet
                bret = True
            elif bre and bret:
                break
        n = w.find("(")
        n = w[1:n]
        welise = ["晴", "多云", "阴", "", "", "雷阵雨", "雨夹雪", "雨", "小雨",
                  "中雨", "大雨", "暴雨", "大暴雨", "", "雪", "小雪", "中雪", "大雪",
                  "雾", "", "扬沙"]
        nn = welise.index(n)
        if n == "晴":
            read2 = "icons/0[2].jpg"
        elif n == "雾":
            read2 = "icons/31[2].jpg"
        elif n == "阴":
            read2 = "icons/3[2].jpg"
        elif n == "扬沙":
            read2 = "icons/4[2].jpg"
        elif n == "雨夹雪":
            read2 = "icons/7[2].jpg"
        elif "雨" in n:
            read2 = "icons/1[2].jpg"
        else:
            read2 = "icons/29[2].jpg"
        if len(str(nn)) <= 1:
            read = r"D:/icons/0" + str(nn) + "[1].png"
        else:
            read = r"D:/icons/" + str(nn) + "[1].png"
        MainWindow.close()
        return n,[read,read2],degree
    def update():
        #静默数据更新
        webside = webget.get(webside = r"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=80035161_2_dg&wd=%E5%A4%A9%E6%B0%94&oq=%25E5%25A4%25A9%25E6%25B0%2594&rsv_pq=8873d4610004b455&rsv_t=1c88w5krAsUOHNOyw1MAFR90Vjnt%2FxwxsMotIghXubeTv6TXY%2FWARBEh0RwfzB6qfzjcyQ&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t", rod = "")
        webside = str(webside)
        def run():
            MainWindow.close()
        with open("webcode.txt", "w", encoding = "utf-8") as file:
            file.write(webside)
        with open("webcode.txt", encoding = "utf-8") as file:
            for x in range(4000):
                y = file.readline()
                y = ""
            for x in range(1000):
                y = y + file.readline() + "\n"
        c = re.findall(r'>.{1,10}<', y)
        start = 0
        bre = False
        bret = False
        for list_ in c:
            start += 1
            if "(实时)" in list_:
                w = list_
                bre = True
            elif "℃" in list_ and not bret:
                degree = c[start-2]
                degree = degree[1:-1]
                degreet = c[start-1]
                degreet = degreet[1:-1]
                degree = degree + degreet
                bret = True
            elif bre and bret:
                break
        n = w.find("(")
        n = w[1:n]
        welise = ["晴", "多云", "阴", "", "", "雷阵雨", "雨夹雪", "雨", "小雨",
                  "中雨", "大雨", "暴雨", "大暴雨", "", "雪", "小雪", "中雪", "大雪",
                  "雾", "", "扬沙"]
        nn = welise.index(n)
        if n == "晴":
            read2 = "icons/0[2].jpg"
        elif n == "雾":
            read2 = "icons/31[2].jpg"
        elif n == "阴":
            read2 = "icons/3[2].jpg"
        elif n == "扬沙":
            read2 = "icons/4[2].jpg"
        elif n == "雨夹雪":
            read2 = "icons/7[2].jpg"
        elif "雨" in n:
            read2 = "icons/1[2].jpg"
        else:
            read2 = "icons/29[2].jpg"
        print(read2)
        if len(str(nn)) <= 1:
            read = r"icons/0" + str(nn) + "[1].png"
        else:
            read = r"icons/" + str(nn) + "[1].png"
        return n,[read,read2],degree
    def printz():
        update()
except SystemExit:
    pass
