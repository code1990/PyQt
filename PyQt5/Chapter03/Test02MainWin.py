from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(678, 431)
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(80, 30, 531, 321))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap(":/pic/images/python.jpg"))
		self.label.setObjectName("label")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))

# import apprcc_rc
