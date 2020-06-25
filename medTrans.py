import sys
import os
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtCore import QBasicTimer
import pandas as pd

form_class = uic.loadUiType("medTrans.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.loadbtn.clicked.connect(self.open_sheet)

        self.savebtn.clicked.connect(self.save_sheet)

        self.comboBox.currentIndexChanged.connect(self.comboBoxFunction)

        ## qt designer에서 편집안되는 부분 추가
        col_headers = ['Ko', 'En']
        self.tableWidget.setHorizontalHeaderLabels(col_headers)

    global count

    ## 기능 정의

    # 시트 불러오기
    def open_sheet(self):
        self.check_change = False
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], encoding='utf-8', newline='\n') as csv_file:
                self.dir_line.setText(path[0])
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(2)
                my_file = csv.reader(csv_file)
                for row_data in my_file:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    if len(row_data) > 10:
                        self.tableWidget.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.tableWidget.setItem(row, column, item)
        self.tableWidget.removeRow(0)
        self.check_change = True

    # 시트 저장
    def save_sheet(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
    #구글 api 사용
    def translate_google(self):

        import translate_with_glossary
        row_init = self.tableWidget.rowCount()
        for row in range(self.tableWidget.rowCount()):
            row_data = []

            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            row_data[1] = translate_with_glossary.translate_text_with_glossary(row_data[0])

            row = self.tableWidget.rowCount()
            print(row)
            self.console_line.appendPlainText(str(row - row_init + 1) + "번 째 열이 번역되었습니다")

            self.tableWidget.insertRow(row)
            if len(row_data) > 10:
                self.tableWidget.setColumnCount(len(row_data))
            for column, stuff in enumerate(row_data):
                item = QTableWidgetItem(stuff)
                self.tableWidget.setItem(row, column, item)

        row = int(self.tableWidget.rowCount() / 2)
        print(row)
        for i in range(row):
            self.tableWidget.removeRow(0)

    # papago api 사용
    def translate_naver(self):

        import Papago_api

        row_init = self.tableWidget.rowCount()
        for row in range(self.tableWidget.rowCount()):
            row_data = []

            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')

            row_data[1] = Papago_api.translate_papago(row_data[0])

            row = self.tableWidget.rowCount()
            self.console_line.appendPlainText(str(row - row_init + 1) + "번 째 열이 번역되었습니다")

            self.tableWidget.insertRow(row)
            if len(row_data) > 10:
                self.tableWidget.setColumnCount(len(row_data))
            for column, stuff in enumerate(row_data):
                item = QTableWidgetItem(stuff)
                self.tableWidget.setItem(row, column, item)

        row = int(self.tableWidget.rowCount() / 2)
        print(row)
        for i in range(row):
            self.tableWidget.removeRow(0)
    # 구글, 파파고 선택 콤보박스
    def comboBoxFunction(self):
        if self.comboBox.currentText() == "Google":
            self.transbtn.clicked.connect(self.translate_google)
        elif self.comboBox.currentText() == "Papago":
            self.transbtn.clicked.connect(self.translate_naver)


##기능정의 여기까지


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
