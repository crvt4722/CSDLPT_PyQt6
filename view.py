from PyQt6.QtWidgets import  QMainWindow,QApplication, QTableWidgetItem, QTableWidget
from PyQt6 import  uic
import sys
import dao
import time

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/main.ui',self)

class InsertCustomer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/insert_cus.ui',self)

class UpdateTypeCustomer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/update_type_cus.ui',self)

class UI():
    def __init__(self):
        self.main = Main()
        self.main.show()

        # Tạo và làm việc với đối tượng cập nhật
        self.update_view = UpdateTypeCustomer()
        self.main.update_btn.clicked.connect(self.showUpdateGUI)

        # Tạo và làm việc với đối tượng INSERT.
        self.insert_view = InsertCustomer()
        self.main.insert_btn.clicked.connect(self.showInsertGUI)

        # Tạo và làm việc với đối tượng thống kê tiêu dùng
        self.main.select_btn.clicked.connect(self.processStatistics)

        # Tạo và làm việc với đối tượng xem thông tin KH.
        self.main.select_cus.clicked.connect(self.processSelectCustomer)

    def processStatistics(self):

        result = dao.thong_ke_tieu_dung()
        column_name = ['Mã KH', 'Tổng chi tiêu']
        self.main.tableWidget.setColumnCount(2)
        self.main.tableWidget.setHorizontalHeaderLabels(column_name)
        self.main.tableWidget.setRowCount(0)
        self.main.tableWidget.show()

        print(result)
        for row_num, row_data in enumerate(result):
            self.main.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.main.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def processSelectCustomer(self):
        result = dao.xem_thong_tin_kh()
        column_name = ['Mã KH', 'Họ và tên', 'SĐT', 'Địa chỉ']
        self.main.tableWidget.setColumnCount(4)
        self.main.tableWidget.setHorizontalHeaderLabels(column_name)
        self.main.tableWidget.setRowCount(0)
        self.main.tableWidget.show()

        print(result)
        for row_num, row_data in enumerate(result):
            self.main.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.main.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def showUpdateGUI(self):
        self.update_view.show()
        self.update_view.pushButton.clicked.connect(self.processUpdateTypeCustomer)
    def showInsertGUI(self):
        self.insert_view.show()
        self.insert_view.submit_btn.clicked.connect(self.processInsertCustomer)
    def processUpdateTypeCustomer(self):
        my_text = self.update_view.lineEdit.text()

        try:
            my_text = int(my_text)

            if dao.cap_nhat_loai_kh(my_text) == False:
                self.update_view.alert_label.setText('Cập nhật thất bại!')

            else:
                self.update_view.alert_label.setText('Cập nhật thành công!')
                # self.update_view.hide()
        except:
            self.update_view.alert_label.setText('Hãy nhập ký tự số!')

    def processInsertCustomer(self):
        try:
            fullname = self.insert_view.fullname.text()
            phone = self.insert_view.phone.text()
            address = self.insert_view.address.text()
            if dao.them_thong_tin_kh(fullname, phone, address):
                self.insert_view.alert_label.setText('Thêm thông tin KH thành công!')
            else:
                self.insert_view.alert_label.setText('Thất bại!')
        except:
            print('Error!')
if __name__ =='__main__':
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec())