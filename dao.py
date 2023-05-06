# pip install pyodbc
import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-3BGR1M3\CSDLPT6'
DATABASE_NAME = 'QLKS_NA'
USER_NAME = 'sa'
PASSWORD = '1234'

def open_connection():
    # Tạo biến connection.
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + SERVER_NAME + ';DATABASE=' +
                          DATABASE_NAME + ';UID=' + USER_NAME + ';PWD=' + PASSWORD)
    return conn


def thong_ke_tieu_dung():

    sql_query = "SELECT Customer.customer_id AS id, SUM(price + surcharge) AS cnt FROM Customer, Booking " \
                "WHERE Customer.customer_id = Booking.customer_id GROUP BY Customer.customer_id ORDER BY cnt DESC;"

    try:
        conn = open_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        # In dữ liệu câu lệnh SELECT.

        rows = []
        for row in cursor:
            print(row)
            rows.append(row)
        conn.close()
        return rows
    except:
        print('Lỗi truy vấn!!!')


def cap_nhat_loai_kh(dinh_muc = 10000000):
    try:
        conn = open_connection()
        cursor = conn.cursor()

        sql_query = '''UPDATE Customer SET phone = '0111111112'
         WHERE Customer.customer_id in
         (
         SELECT Customer.customer_id from Customer, Booking
         WHERE Customer.customer_id = Booking.customer_id GROUP BY Customer.customer_id  HAVING sum(price + surcharge) > ?
         )'''

        cursor.execute(sql_query, (dinh_muc))
        conn.commit()
        conn.close()
        return True
    except :
        print('Lỗi truy vấn!!!')
        return False

def them_thong_tin_kh(fullname = '', phone = '', address = ''):
    try:
        conn = open_connection()
        cursor = conn.cursor()

        sql_query = 'SELECT TOP 1 customer_id from Customer ORDER BY customer_id DESC;'
        cursor.execute(sql_query)

        customer_id = ''
        for row in cursor:
            customer_id = 'KHNA' + "%06d"%(int(row[0][4:])+1)

        sql_query = "INSERT INTO Customer (customer_id, full_name, phone, address) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_query, (customer_id, fullname, phone, address))

        conn.commit()
        conn.close()
        return True
    except:
        print('Lỗi truy vấn!!!')
        return False

def xem_thong_tin_kh():
    try:
        conn = open_connection()
        cursor = conn.cursor()

        sql_query = 'SELECT customer_id, full_name, phone, address FROM Customer;'
        cursor.execute(sql_query)

        rows = []
        for row in cursor:
            print(row)
            rows.append(row)

        conn.close()
        return rows
    except:
        print('Lỗi truy vấn!')

