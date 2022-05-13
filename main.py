import sys
from unittest import result
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import mysql.connector  as con

class LoginApp(QDialog):
    def __init__(self):
        super(LoginApp,self).__init__()
        loadUi("login.ui",self)
        self.b1.clicked.connect(self.login)
        self.b3.clicked.connect(self.show_reg)

    

    def login(self):
        un=self.tb1.text()
        pw=self.tb2.text()
        db=con.connect(host="localhost",user="root",password="",db="case_entry")
        cursor=db.cursor()
        cursor.execute("select * from users where username = '"+ un +"' and password = '"+ pw +"'")
        result=cursor.fetchone()
        self.tb1.text()
        self.tb1.setText("")
        self.tb2.setText("")
        if result:
            QMessageBox.information(self,"Login Output","congrats")
        else:
            QMessageBox.information(self,"Login Output","Invalid user")

    
    def show_reg(self):
        widget.setCurrentIndex(1)


class RegApp(QDialog):
    def __init__(self):
        super(RegApp,self).__init__()
        loadUi("sign-up.ui",self)
        self.b2.clicked.connect(self.signup)
        self.b4.clicked.connect(self.show_login)

    def signup(self):
        un=self.tb3.text()
        ph=self.tb4.text()
        pw=self.tb5.text()
        db=con.connect(host="localhost",user="root",password="",db="case_entry")
        cursor=db.cursor()
        cursor.execute("select * from users where username = '"+ un +"'")
        result=cursor.fetchone()
        if result:
            QMessageBox.information(self,"Signup Output","Already exists")
        else:
            cursor.execute("INSERT INTO `users`(`username`, `password`, `phone`) VALUES ('"+ un +"' ,'"+ pw +"','"+ ph +"')")
            db.commit()
            self.tb3.setText("")
            self.tb4.setText("")
            self.tb5.setText("")
            QMessageBox.information(self,"Signup Output","congrats !!! login now ")
    
    def show_login(self):
        widget.setCurrentIndex(0)




app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
loginform=LoginApp()
registratioform=RegApp()
widget.addWidget(loginform)
widget.addWidget(registratioform)
widget.setCurrentIndex(0)
widget.setFixedWidth(400)
widget.setFixedHeight(500)
widget.show()

app.exec_()

