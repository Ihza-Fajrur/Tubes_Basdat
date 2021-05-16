import Menu
import MenuAdmin
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        LoginWindow.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Login_view = QtWidgets.QGroupBox(self.centralwidget)
        self.Login_view.setGeometry(QtCore.QRect(110, 110, 571, 381))
        self.Login_view.setAutoFillBackground(False)
        self.Login_view.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0.494, stop:0 rgba(54, 54, 54, 199), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.Login_view.setTitle("")
        self.Login_view.setObjectName("Login_view")

        self.Username = QtWidgets.QLineEdit(self.Login_view)
        self.Username.setGeometry(QtCore.QRect(130, 160, 311, 41))
        self.Username.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.Username.setText("")
        self.Username.setClearButtonEnabled(False)
        self.Username.setObjectName("Username")

        self.Password = QtWidgets.QLineEdit(self.Login_view)
        self.Password.setGeometry(QtCore.QRect(130, 230, 311, 41))
        self.Password.setStyleSheet("background:transparent;\n"
        "color: rgb(0, 0, 0);\n"
        "border:none;\n"
        "border-bottom:1px solid;")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setClearButtonEnabled(False)
        self.Password.setObjectName("Password")

        self.Login_button = QtWidgets.QPushButton(self.Login_view)
        self.Login_button.setGeometry(QtCore.QRect(330, 320, 111, 41))
        self.Login_button.setAutoFillBackground(False)
        self.Login_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Login_button.setDefault(True)
        self.Login_button.setObjectName("Login_button")

        self.userIcon = QtWidgets.QLabel(self.Login_view)
        self.userIcon.setGeometry(QtCore.QRect(250, 50, 51, 51))
        self.userIcon.setText("")
        self.userIcon.setPixmap(QtGui.QPixmap("icon/login.png"))
        self.userIcon.setScaledContents(True)
        self.userIcon.setObjectName("userIcon")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        #code here
        #login button pressed
        self.Login_button.pressed.connect(self.loginkan)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.Password.setPlaceholderText(_translate("LoginWindow", "Password"))
        self.Username.setPlaceholderText(_translate("LoginWindow", "Username"))
        self.Login_button.setText(_translate("LoginWindow", "Login"))

    def loginkan(self):
        self.username = self.Username.text()
        if not (self.username):
            self.show_Popup("Username dan Password tidak boleh kosong!")
            return 0
        mycursor.execute("Select password from login_info where username  = '" + self.username + "\'")
        result = mycursor.fetchall()
        #kalau username tidak ada
        if not result:
            self.show_Popup("Username atau Password anda salah!")
            return 0
        #get the password
        result = (result[0])[0]
        print(type(result))
        print(result)
        if result == self.Password.text():
            self.show_Popup("Anda Berhasil Login!")
            mycursor.execute("Select Account_role from login_info where username  = '" + self.username + "\'")
            result = mycursor.fetchall()
            result = (result[0])[0]
            if result == 'admin':
                #admin
                print("Dia Admin")
                self.gotoMenuAdmin(LoginWindow)
            else:
                #user biasa
                self.gotoMenu(LoginWindow)
        else:
            self.show_Popup("Username atau Password and a salah!")

    def gotoMenuAdmin(self,LoginWindow):
        self.Menu = QtWidgets.QMainWindow()
        self.ui = MenuAdmin.Ui_MenuAdmin()
        self.ui.getMeAName(self.username)
        self.ui.setupUi(self.Menu)
        self.Menu.show()
        LoginWindow.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Muncullah(Menu))


    def gotoMenu(self,LoginWindow):
        self.Menu = QtWidgets.QMainWindow()
        self.ui = Menu.Ui_Menu()
        self.ui.getMeAName(self.username)
        self.ui.setupUi(self.Menu)
        self.Menu.show()
        LoginWindow.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Muncullah(Menu))

    def Muncullah(self,Menu):
        self.Menu.hide()
        LoginWindow.show()

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()

# def CallMenu():
#     ui.MunculMenu()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
