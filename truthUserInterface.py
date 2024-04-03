# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QByteArray


LOGO = (b"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAABhElEQVQ4y43TTYjNURgG8N+5rpANYTOF3"
        b"JWPKENZTEYkxaCwVJrNOIViZyGriawsNOgfC421ZjWF22Q1e8mUJt2blKWFncw4Nu/tXtdtzFun856P5znvx3OSfqtKQgM5ZmihKadm//XUBx"
        b"7FE7TxCTewPk4LxvFVTu86kFoPeBxz2IezuIL7eN/zWANNVZn4m6Aqx/AM9dj/jgVsxiU8wHJEsQZPVeVEN4WqTGIdlvBNTlMDajOCw7iLLVj"
        b"E3nrkfRk7g/CcQZbTPOZV5SJGI6LtNZzHrkinktOsle0jfuIVbtV6WrWIO/5vC5jqtLkWYf/CNC6sgmAGe7Ct04VWMF7FoVUQjOFM+O0anmMr"
        b"dmB4RWhVGngYq994Ww/FHYnNA1HlD3L6PIDiJF6E/0VOs3U5FVW5hjfYEFFMq8ptvIy2DuNgjE3x+lhXiTnNhe6XsRYboy4z2I0JHO8B35TT6"
        b"0Gf6RT2414oE37gMY5iCNc74H8JukSno9IdjbTxCC05LfVe/QOS32gKZZGhUgAAAABJRU5ErkJggg==")


def icon(base64):
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray.fromBase64(base64))
    _icon = QIcon(pixmap)
    return _icon


class UiTruthtableWindow(object):

    def setupUi(self, truthtable_window):
        truthtable_window.setObjectName("truthtable_window")
        truthtable_window.setWindowModality(QtCore.Qt.NonModal)
        truthtable_window.resize(640, 480)
        truthtable_window.setMinimumSize(QtCore.QSize(640, 480))
        truthtable_window.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(truthtable_window)
        self.centralwidget.setObjectName("centralwidget")
        self.functions_group = QtWidgets.QGroupBox(self.centralwidget)
        self.functions_group.setGeometry(QtCore.QRect(10, 10, 300, 350))
        self.functions_group.setMinimumSize(QtCore.QSize(300, 350))
        self.functions_group.setMaximumSize(QtCore.QSize(300, 350))
        self.functions_group.setObjectName("functions_group")
        self.widget = QtWidgets.QWidget(self.functions_group)
        self.widget.setGeometry(QtCore.QRect(10, 20, 281, 321))
        self.widget.setObjectName("widget")
        self.functions_layout = QtWidgets.QVBoxLayout(self.widget)
        self.functions_layout.setContentsMargins(0, 0, 0, 0)
        self.functions_layout.setObjectName("functions_layout")
        self.func_list = QtWidgets.QListWidget(self.widget)
        self.func_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.func_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.func_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.func_list.setObjectName("func_list")
        self.functions_layout.addWidget(self.func_list)
        self.gridlayout3 = QtWidgets.QGridLayout()
        self.gridlayout3.setObjectName("gridlayout3")
        self.gridlayout2 = QtWidgets.QGridLayout()
        self.gridlayout2.setObjectName("gridlayout2")
        self.add_func_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_func_btn.sizePolicy().hasHeightForWidth())
        self.add_func_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.add_func_btn.setFont(font)
        self.add_func_btn.setObjectName("add_func_btn")
        self.gridlayout2.addWidget(self.add_func_btn, 0, 0, 1, 1)
        self.del_func_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_func_btn.sizePolicy().hasHeightForWidth())
        self.del_func_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.del_func_btn.setFont(font)
        self.del_func_btn.setObjectName("del_func_btn")
        self.del_func_btn.setEnabled(False)
        self.gridlayout2.addWidget(self.del_func_btn, 0, 1, 1, 1)
        self.gridlayout3.addLayout(self.gridlayout2, 0, 0, 1, 1)
        self.clear_functions_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_functions_btn.sizePolicy().hasHeightForWidth())
        self.clear_functions_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.clear_functions_btn.setFont(font)
        self.clear_functions_btn.setObjectName("clear_functions_btn")
        self.gridlayout3.addWidget(self.clear_functions_btn, 0, 1, 1, 1)
        self.functions_layout.addLayout(self.gridlayout3)
        self.func_edit = QtWidgets.QLineEdit(self.widget)
        self.func_edit.setObjectName("func_edit")
        self.functions_layout.addWidget(self.func_edit)
        self.groupbox4 = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox4.sizePolicy().hasHeightForWidth())
        self.groupbox4.setSizePolicy(sizePolicy)
        self.groupbox4.setMinimumSize(QtCore.QSize(0, 80))
        self.groupbox4.setTitle("")
        self.groupbox4.setObjectName("groupbox4")
        self.widget1 = QtWidgets.QWidget(self.groupbox4)
        self.widget1.setGeometry(QtCore.QRect(3, 12, 271, 61))
        self.widget1.setObjectName("widget1")
        self.gridlayout4 = QtWidgets.QGridLayout(self.widget1)
        self.gridlayout4.setContentsMargins(0, 0, 0, 0)
        self.gridlayout4.setObjectName("gridlayout4")
        self.not_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_btn.sizePolicy().hasHeightForWidth())
        self.not_btn.setSizePolicy(sizePolicy)
        self.not_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.not_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.not_btn.setFont(font)
        self.not_btn.setObjectName("not_btn")
        self.gridlayout4.addWidget(self.not_btn, 0, 0, 1, 1)
        self.and_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.and_btn.sizePolicy().hasHeightForWidth())
        self.and_btn.setSizePolicy(sizePolicy)
        self.and_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.and_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.and_btn.setFont(font)
        self.and_btn.setObjectName("and_btn")
        self.gridlayout4.addWidget(self.and_btn, 0, 1, 1, 1)
        self.or_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.or_btn.sizePolicy().hasHeightForWidth())
        self.or_btn.setSizePolicy(sizePolicy)
        self.or_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.or_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.or_btn.setFont(font)
        self.or_btn.setObjectName("or_btn")
        self.gridlayout4.addWidget(self.or_btn, 0, 2, 1, 1)
        self.follow_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.follow_btn.sizePolicy().hasHeightForWidth())
        self.follow_btn.setSizePolicy(sizePolicy)
        self.follow_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.follow_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.follow_btn.setFont(font)
        self.follow_btn.setObjectName("follow_btn")
        self.gridlayout4.addWidget(self.follow_btn, 0, 3, 1, 1)
        self.equal_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal_btn.sizePolicy().hasHeightForWidth())
        self.equal_btn.setSizePolicy(sizePolicy)
        self.equal_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.equal_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.equal_btn.setFont(font)
        self.equal_btn.setObjectName("equal_btn")
        self.gridlayout4.addWidget(self.equal_btn, 0, 4, 1, 1)
        self.xor_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xor_btn.sizePolicy().hasHeightForWidth())
        self.xor_btn.setSizePolicy(sizePolicy)
        self.xor_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.xor_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.xor_btn.setFont(font)
        self.xor_btn.setObjectName("xor_btn")
        self.gridlayout4.addWidget(self.xor_btn, 0, 5, 1, 1)
        self.x_var_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_var_btn.sizePolicy().hasHeightForWidth())
        self.x_var_btn.setSizePolicy(sizePolicy)
        self.x_var_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.x_var_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.x_var_btn.setFont(font)
        self.x_var_btn.setObjectName("x_var_btn")
        self.gridlayout4.addWidget(self.x_var_btn, 0, 6, 1, 1)
        self.y_var_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_var_btn.sizePolicy().hasHeightForWidth())
        self.y_var_btn.setSizePolicy(sizePolicy)
        self.y_var_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.y_var_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.y_var_btn.setFont(font)
        self.y_var_btn.setObjectName("y_var_btn")
        self.gridlayout4.addWidget(self.y_var_btn, 0, 7, 1, 1)
        self.closebrackets_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closebrackets_btn.sizePolicy().hasHeightForWidth())
        self.closebrackets_btn.setSizePolicy(sizePolicy)
        self.closebrackets_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.closebrackets_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.closebrackets_btn.setFont(font)
        self.closebrackets_btn.setObjectName("closebrackets_btn")
        self.gridlayout4.addWidget(self.closebrackets_btn, 0, 8, 1, 1)
        self.z_var_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_var_btn.sizePolicy().hasHeightForWidth())
        self.z_var_btn.setSizePolicy(sizePolicy)
        self.z_var_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.z_var_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.z_var_btn.setFont(font)
        self.z_var_btn.setObjectName("z_var_btn")
        self.gridlayout4.addWidget(self.z_var_btn, 1, 0, 1, 1)
        self.w_var_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_var_btn.sizePolicy().hasHeightForWidth())
        self.w_var_btn.setSizePolicy(sizePolicy)
        self.w_var_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.w_var_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.w_var_btn.setFont(font)
        self.w_var_btn.setObjectName("w_var_btn")
        self.gridlayout4.addWidget(self.w_var_btn, 1, 1, 1, 1)
        self.a_var_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_var_btn.sizePolicy().hasHeightForWidth())
        self.a_var_btn.setSizePolicy(sizePolicy)
        self.a_var_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.a_var_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.a_var_btn.setFont(font)
        self.a_var_btn.setObjectName("a_var_btn")
        self.gridlayout4.addWidget(self.a_var_btn, 1, 2, 1, 1)
        self.b_var_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_var_btn.sizePolicy().hasHeightForWidth())
        self.b_var_btn.setSizePolicy(sizePolicy)
        self.b_var_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.b_var_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b_var_btn.setFont(font)
        self.b_var_btn.setObjectName("b_var_btn")
        self.gridlayout4.addWidget(self.b_var_btn, 1, 3, 1, 1)
        self.c_var_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_var_btn.sizePolicy().hasHeightForWidth())
        self.c_var_btn.setSizePolicy(sizePolicy)
        self.c_var_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.c_var_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.c_var_btn.setFont(font)
        self.c_var_btn.setObjectName("c_var_btn")
        self.gridlayout4.addWidget(self.c_var_btn, 1, 4, 1, 1)
        self.d_var_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_var_btn.sizePolicy().hasHeightForWidth())
        self.d_var_btn.setSizePolicy(sizePolicy)
        self.d_var_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.d_var_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.d_var_btn.setFont(font)
        self.d_var_btn.setObjectName("d_var_btn")
        self.gridlayout4.addWidget(self.d_var_btn, 1, 5, 1, 1)
        self.zero_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_btn.sizePolicy().hasHeightForWidth())
        self.zero_btn.setSizePolicy(sizePolicy)
        self.zero_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.zero_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.zero_btn.setFont(font)
        self.zero_btn.setObjectName("zero_btn")
        self.gridlayout4.addWidget(self.zero_btn, 1, 6, 1, 1)
        self.one_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one_btn.sizePolicy().hasHeightForWidth())
        self.one_btn.setSizePolicy(sizePolicy)
        self.one_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.one_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.one_btn.setFont(font)
        self.one_btn.setObjectName("one_btn")
        self.gridlayout4.addWidget(self.one_btn, 1, 7, 1, 1)
        self.openbrackets_btn = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openbrackets_btn.sizePolicy().hasHeightForWidth())
        self.openbrackets_btn.setSizePolicy(sizePolicy)
        self.openbrackets_btn.setMinimumSize(QtCore.QSize(21, 0))
        self.openbrackets_btn.setMaximumSize(QtCore.QSize(21, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openbrackets_btn.setFont(font)
        self.openbrackets_btn.setObjectName("openbrackets_btn")
        self.gridlayout4.addWidget(self.openbrackets_btn, 1, 8, 1, 1)
        self.functions_layout.addWidget(self.groupbox4)
        self.confirm_func_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_func_btn.sizePolicy().hasHeightForWidth())
        self.confirm_func_btn.setSizePolicy(sizePolicy)
        self.confirm_func_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirm_func_btn.setFont(font)
        self.confirm_func_btn.setObjectName("confirm_func_btn")
        self.functions_layout.addWidget(self.confirm_func_btn)
        self.fragment_group = QtWidgets.QGroupBox(self.centralwidget)
        self.fragment_group.setEnabled(False)
        self.fragment_group.setGeometry(QtCore.QRect(330, 10, 300, 400))
        self.fragment_group.setMinimumSize(QtCore.QSize(300, 400))
        self.fragment_group.setMaximumSize(QtCore.QSize(300, 400))
        self.fragment_group.setObjectName("fragment_group")
        self.widget2 = QtWidgets.QWidget(self.fragment_group)
        self.widget2.setGeometry(QtCore.QRect(10, 20, 281, 371))
        self.widget2.setObjectName("widget2")
        self.fragment_layout = QtWidgets.QVBoxLayout(self.widget2)
        self.fragment_layout.setContentsMargins(0, 0, 0, 0)
        self.fragment_layout.setObjectName("fragment_layout")
        self.check_if_last = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.check_if_last.setFont(font)
        self.check_if_last.setObjectName("check_if_last")
        self.fragment_layout.addWidget(self.check_if_last)
        self.generate_head_btn = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.generate_head_btn.setFont(font)
        self.generate_head_btn.setObjectName("generate_head_btn")
        self.fragment_layout.addWidget(self.generate_head_btn)
        self.fragment_table = QtWidgets.QTableView(self.widget2)
        self.fragment_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.fragment_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.fragment_table.setObjectName("fragment_table")
        self.fragment_layout.addWidget(self.fragment_table)
        self.gridlayout6 = QtWidgets.QGridLayout()
        self.gridlayout6.setObjectName("gridlayout6")
        self.label1 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.gridlayout6.addWidget(self.label1, 0, 0, 1, 1)
        self.gridlayout5 = QtWidgets.QGridLayout()
        self.gridlayout5.setObjectName("gridlayout5")
        self.add_row_btn = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_row_btn.sizePolicy().hasHeightForWidth())
        self.add_row_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_row_btn.setFont(font)
        self.add_row_btn.setObjectName("add_row_btn")
        self.gridlayout5.addWidget(self.add_row_btn, 0, 0, 1, 1)
        self.del_row_btn = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_row_btn.sizePolicy().hasHeightForWidth())
        self.del_row_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.del_row_btn.setFont(font)
        self.del_row_btn.setObjectName("del_row_btn")
        self.gridlayout5.addWidget(self.del_row_btn, 0, 1, 1, 1)
        self.change_row_btn = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_row_btn.sizePolicy().hasHeightForWidth())
        self.change_row_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.change_row_btn.setFont(font)
        self.change_row_btn.setObjectName("change_row_btn")
        self.gridlayout5.addWidget(self.change_row_btn, 1, 0, 1, 1)
        self.apply_change_row_btn = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_change_row_btn.sizePolicy().hasHeightForWidth())
        self.apply_change_row_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.apply_change_row_btn.setFont(font)
        self.apply_change_row_btn.setObjectName("apply_change_row_btn")
        self.gridlayout5.addWidget(self.apply_change_row_btn, 1, 1, 1, 1)
        self.gridlayout6.addLayout(self.gridlayout5, 0, 1, 1, 1)
        self.fragment_layout.addLayout(self.gridlayout6)
        self.horizontallayout = QtWidgets.QHBoxLayout()
        self.horizontallayout.setObjectName("horizontallayout")
        self.label2 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.horizontallayout.addWidget(self.label2)
        self.row_edit = QtWidgets.QLineEdit(self.widget2)
        self.row_edit.setObjectName("row_edit")
        self.horizontallayout.addWidget(self.row_edit)
        self.fragment_layout.addLayout(self.horizontallayout)
        self.label3 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.fragment_layout.addWidget(self.label3)
        self.result_group = QtWidgets.QGroupBox(self.centralwidget)
        self.result_group.setEnabled(False)
        self.result_group.setGeometry(QtCore.QRect(10, 370, 300, 100))
        self.result_group.setMinimumSize(QtCore.QSize(300, 100))
        self.result_group.setMaximumSize(QtCore.QSize(300, 100))
        self.result_group.setObjectName("result_group")
        self.results_list = QtWidgets.QListView(self.result_group)
        self.results_list.setGeometry(QtCore.QRect(10, 20, 281, 71))
        self.results_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.results_list.setObjectName("results_list")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 414, 301, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridlayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setObjectName("gridlayout")
        self.get_result_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_result_btn.sizePolicy().hasHeightForWidth())
        self.get_result_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.get_result_btn.setFont(font)
        self.get_result_btn.setObjectName("get_result_btn")
        self.gridlayout.addWidget(self.get_result_btn, 0, 0, 1, 1)
        self.clearall_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearall_btn.sizePolicy().hasHeightForWidth())
        self.clearall_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.clearall_btn.setFont(font)
        self.clearall_btn.setObjectName("clearall_btn")
        self.gridlayout.addWidget(self.clearall_btn, 0, 1, 1, 1)
        truthtable_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(truthtable_window)
        QtCore.QMetaObject.connectSlotsByName(truthtable_window)

    def retranslateUi(self, truthtable_window):
        _translate = QtCore.QCoreApplication.translate
        truthtable_window.setWindowTitle(_translate("truthtable_window", "Truth tables computing"))
        truthtable_window.setWindowIcon(icon(LOGO))
        self.functions_group.setTitle(_translate("truthtable_window", "Functions"))
        self.func_list.setSortingEnabled(False)
        self.add_func_btn.setText(_translate("truthtable_window", "Add"))
        self.del_func_btn.setText(_translate("truthtable_window", "Delete"))
        self.clear_functions_btn.setText(_translate("truthtable_window", "Clear"))
        self.not_btn.setText(_translate("truthtable_window", "¬"))
        self.and_btn.setText(_translate("truthtable_window", "∧"))
        self.or_btn.setText(_translate("truthtable_window", "∨"))
        self.follow_btn.setText(_translate("truthtable_window", "→"))
        self.equal_btn.setText(_translate("truthtable_window", "≡"))
        self.xor_btn.setText(_translate("truthtable_window", "⊕"))
        self.x_var_btn.setText(_translate("truthtable_window", "x"))
        self.y_var_btn.setText(_translate("truthtable_window", "y"))
        self.closebrackets_btn.setText(_translate("truthtable_window", ")"))
        self.z_var_btn.setText(_translate("truthtable_window", "z"))
        self.w_var_btn.setText(_translate("truthtable_window", "w"))
        self.a_var_btn.setText(_translate("truthtable_window", "a"))
        self.b_var_btn.setText(_translate("truthtable_window", "b"))
        self.c_var_btn.setText(_translate("truthtable_window", "c"))
        self.d_var_btn.setText(_translate("truthtable_window", "d"))
        self.zero_btn.setText(_translate("truthtable_window", "0"))
        self.one_btn.setText(_translate("truthtable_window", "1"))
        self.openbrackets_btn.setText(_translate("truthtable_window", "("))
        self.confirm_func_btn.setText(_translate("truthtable_window", "Confirm and lock"))
        self.fragment_group.setTitle(_translate("truthtable_window", "Fragment of table"))
        self.check_if_last.setText(_translate("truthtable_window", "Function values are the last columns"))
        self.generate_head_btn.setText(_translate("truthtable_window", "Generate table head"))
        self.label1.setText(_translate("truthtable_window", "Row of values:"))
        self.add_row_btn.setText(_translate("truthtable_window", "Add"))
        self.del_row_btn.setText(_translate("truthtable_window", "Delete"))
        self.change_row_btn.setText(_translate("truthtable_window", "Change"))
        self.apply_change_row_btn.setText(_translate("truthtable_window", "Apply"))
        self.label2.setText(_translate("truthtable_window", "Values:"))
        self.label3.setText(_translate("truthtable_window", "Separate - whitespace; N if unknown"))
        self.result_group.setTitle(_translate("truthtable_window", "Result"))
        self.get_result_btn.setText(_translate("truthtable_window", "Get result"))
        self.clearall_btn.setText(_translate("truthtable_window", "Clear all"))

    def connect(self):
        pass
