#!/usr/bin/env python
import mysql.connector
from datetime import date
class User:
    def __init__(self, user_id=0, user_post=None, user_date_start_work=None, user_date_end_work=None, user_password=None, user_login=None, user_FIO=None, Division_Division_num=0):
        self.user_id = user_id
        self.user_post = user_post
        self.user_date_start_work = user_date_start_work
        self.user_date_end_work = user_date_end_work
        self.user_password = user_password
        self.user_login = user_login
        self.user_FIO = user_FIO
        self.Division_Division_num = Division_Division_num
    @property
    def info(self):
        return f'{self.user_id} | {self.user_post} | {self.user_date_start_work} | {self.user_date_end_work} | {self.user_login} | {self.user_FIO } | {self.Division_Division_num }'
    @staticmethod
    def get_user():
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        result = []
        c.execute('select * from user')
        rows = c.fetchall()
        for row in rows:
            user = User(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7])
            result.append(user)
        c.close()
        conn.close()
        return result

    @staticmethod
    def del_user(user_id):
        try:
            dl = "DELETE FROM user WHERE user_id = %s"
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            c.execute(dl, (user_id,))
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def add_user(user_id, user_post, user_date_start_work, user_date_end_work, user_password, user_login, user_FIO, Division_Division_num ):
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        c.execute('insert into user values(%s, %s, %s, %s, %s, %s, %s, %s)', \
            (int(user_id), user_post, date.fromisoformat(user_date_start_work), date.fromisoformat(user_date_end_work), user_password, user_login, user_FIO,int(Division_Division_num), ))
        conn.commit()
        c.close()
        conn.close()
    def change_user(user_id, user_post, user_date_start_work, user_date_end_work, user_password, user_login, user_FIO, Division_Division_num ):
        try:
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            ch1 = """UPDATE user SET user_post = %s, user_date_start_work = %s, user_date_end_work = %s, user_password = %s, user_login = %s, user_FIO = %s, Division_Division_num = %s WHERE user_id = %s"""
            ch2=( user_post, user_date_start_work, user_date_end_work, user_password, user_login, user_FIO, Division_Division_num, user_id)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()
class Division:
    def __init__(self, Division_num=0, Division_name=None):
        self.Division_num = Division_num
        self.Division_name = Division_name
    @property
    def info_div(self):
        return f'{self.Division_num} | {self.Division_name} '
    @staticmethod
    def get_division():
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        result = []
        c.execute('select * from division')
        rows = c.fetchall()
        for row in rows:
            division = Division(row[0], row[1])
            result.append(division)
        c.close()
        conn.close()
        return result

    @staticmethod
    def del_division(Division_num):
        try:
            dl = "DELETE FROM division WHERE Division_num = %s"
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            c.execute(dl, (Division_num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def change_division(Division_num, Division_name):
        try:
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            ch1 = """UPDATE division SET Division_name = %s WHERE Division_num = %s"""
            ch2=(Division_name, Division_num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def add_division(Division_num, Division_name):
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        c.execute('insert into division values(%s, %s)', \
            (int(Division_num), Division_name, ))
        conn.commit()
        c.close()
        conn.close()
class Technics:
    def __init__(self, technics_inventory_num=0, technics_name=None, technics_model=None, technics_year_of_release=None, Division_Division_num=0):
        self.technics_inventory_num = technics_inventory_num
        self.technics_name = technics_name
        self.technics_model = technics_model
        self.technics_year_of_release = technics_year_of_release
        self.Division_Division_num = Division_Division_num
    @property
    def info_tec(self):
        return f'{self.technics_inventory_num} | {self.technics_name} | {self.technics_model}  | {self.technics_year_of_release}  | {self.Division_Division_num}  '
    @staticmethod
    def get_technic():
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        result = []
        c.execute('select * from technics')
        rows = c.fetchall()
        for row in rows:
            technics = Technics(row[0], row[1], row[2], row[3],row[4])
            result.append(technics)
        c.close()
        conn.close()
        return result

    @staticmethod
    def del_technic(technics_inventory_num):
        try:
            dl = "DELETE FROM technics WHERE technics_inventory_num = %s"
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            c.execute(dl, (technics_inventory_num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def change_technic(technics_inventory_num, technics_name, technics_model, technics_year_of_release,Division_Division_num):
        try:
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            ch1 = """UPDATE technics SET technics_name = %s, technics_model = %s, technics_year_of_release = %s,Division_Division_num = %s WHERE technics_inventory_num = %s"""
            ch2=( technics_name, technics_model, technics_year_of_release,Division_Division_num, technics_inventory_num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def add_technic(technics_inventory_num, technics_name, technics_model, technics_year_of_release,Division_Division_num):
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        c.execute('insert into technics values(%s, %s, %s, %s, %s)', \
            (int(technics_inventory_num), technics_name, technics_model, technics_year_of_release, int(Division_Division_num), ))
        conn.commit()
        c.close()
        conn.close()
class Document:
    def __init__(self, document_num=0, document_date_of_transfer=None, technics_technics_inventory_num=0,  technics_Division_Division_num=0):
        self.document_num = document_num
        self.document_date_of_transfer = document_date_of_transfer
        self.technics_technics_inventory_num = technics_technics_inventory_num
        self.technics_Division_Division_num = technics_Division_Division_num
    @property
    def info_doc(self):
        return f'{self.document_num} | {self.document_date_of_transfer} | {self.technics_technics_inventory_num}  | {self.technics_technics_inventory_num} '
    @staticmethod
    def get_document():
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        result = []
        c.execute('select * from document')
        rows = c.fetchall()
        for row in rows:
            documents = Document(row[0], row[1], row[2], row[3])
            result.append(documents)
        c.close()
        conn.close()
        return result

    @staticmethod
    def del_document(document_num):
        try:
            dl = "DELETE FROM document WHERE document_num = %s"
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            c.execute(dl, (document_num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def change_document(document_num, document_date_of_transfer, technics_technics_inventory_num, technics_Division_Division_num):
        try:
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            ch1 = """UPDATE document SET document_date_of_transfer = %s,technics_technics_inventory_num = %s, technics_Division_Division_num = %s WHERE document_num = %s"""
            ch2=(document_date_of_transfer, technics_technics_inventory_num, technics_Division_Division_num, document_num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def add_document(document_num, document_date_of_transfer, technics_technics_inventory_num, technics_Division_Division_num):
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        c.execute('insert into document values(%s, %s, %s, %s)', \
            (int(document_num),  document_date_of_transfer, int(technics_technics_inventory_num), int(technics_Division_Division_num), ))
        conn.commit()
        c.close()
        conn.close()
class Invoice:
    def __init__(self, invoice_num=0, invoice_price_componentParrt=None, invoice_list_of_required_spare_parts=None, technics_technics_inventory_num=0, technics_Division_Division_num=0):
        self.invoice_num = invoice_num
        self.invoice_price_componentParrt = invoice_price_componentParrt
        self.invoice_list_of_required_spare_parts = invoice_list_of_required_spare_parts
        self.technics_technics_inventory_num = technics_technics_inventory_num
        self.technics_Division_Division_num = technics_Division_Division_num
    @property
    def info_inv(self):
        return f'{self.invoice_num} | {self.invoice_price_componentParrt} | {self.invoice_list_of_required_spare_parts}  | {self.technics_technics_inventory_num}  | {self.technics_Division_Division_num}  '
    @staticmethod
    def get_invoice():
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        result = []
        c.execute('select * from invoice')
        rows = c.fetchall()
        for row in rows:
            invoices = Invoice(row[0], row[1], row[2], row[3],row[4])
            result.append(invoices)
        c.close()
        conn.close()
        return result

    @staticmethod
    def del_invoice(invoice_num):
        try:
            dl = "DELETE FROM invoice WHERE invoice_num = %s"
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            c.execute(dl, (invoice_num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def change_invoice(invoice_num, invoice_price_componentParrt, invoice_list_of_required_spare_parts, technics_technics_inventory_num,technics_Division_Division_num):
        try:
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            ch1 = """UPDATE invoice SET invoice_price_componentParrt = %s, invoice_list_of_required_spare_parts = %s, technics_technics_inventory_num = %s,technics_Division_Division_num = %s WHERE invoice_num = %s"""
            ch2=(invoice_price_componentParrt, invoice_list_of_required_spare_parts, technics_technics_inventory_num,technics_Division_Division_num, invoice_num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def add_invoice(invoice_num, invoice_price_componentParrt, invoice_list_of_required_spare_parts, technics_technics_inventory_num,technics_Division_Division_num):
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        c.execute('insert into invoice values(%s, %s, %s, %s, %s)', \
            (int(invoice_num), invoice_price_componentParrt, invoice_list_of_required_spare_parts, int(technics_technics_inventory_num), int(technics_Division_Division_num), ))
        conn.commit()
        c.close()
        conn.close()

class Backups:
    def __init__(self, backups_num=0, backups_date=None, backups_versional=None):
        self.backups_num = backups_num
        self.backups_date = backups_date
        self.backups_versional = backups_versional


    @staticmethod
    def del_backup(backups_num):
        try:
            dl = "DELETE FROM backups WHERE backups_num = %s"
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            c.execute(dl, (backups_num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def change_backup(backups_num, backups_date, backups_versional):
        try:
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            ch1 = """UPDATE backups SET backups_date = %s, backups_versional = %s WHERE backups_num = %s"""
            ch2=(backups_date,backups_versional,backups_num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def add_backup(backups_num, backups_date, backups_versional):
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        c.execute('insert into backups values(%s, %s, %s)', \
            (int(backups_num), backups_date, backups_versional, ))
        conn.commit()
        c.close()
        conn.close()

class Technics_repair:
    def __init__(self, technics_repair_num=0, Date_of_delivery_for_repair=None, Repair_period=None, Type_of_repair=None, Date_of_transfer=None, FIO_Employee_passed_repair=None, Number__Employee_passed_repair=0, FIO_Employee_accepted_repair=None, Number__Employee_accepted_repair=0,Position_of_repair_person=None, technics_technics_inventory_num=None, technics_Division_Division_num=None):
        self.technics_repair_num = technics_repair_num
        self.Date_of_delivery_for_repair = Date_of_delivery_for_repair
        self.Repair_period = Repair_period
        self.Type_of_repair = Type_of_repair
        self.Date_of_transfer = Date_of_transfer
        self.FIO_Employee_passed_repair = FIO_Employee_passed_repair
        self.Number__Employee_passed_repair = Number__Employee_passed_repair
        self.FIO_Employee_accepted_repair = FIO_Employee_accepted_repair
        self.Number__Employee_accepted_repair = Number__Employee_accepted_repair
        self.Position_of_repair_person = Position_of_repair_person
        self.technics_technics_inventory_num = technics_technics_inventory_num
        self.technics_Division_Division_num = technics_Division_Division_num
    @property
    def info_tr(self):
        return f'{self.technics_repair_num} | {self.Date_of_delivery_for_repair} | {self.Repair_period}  | {self.Type_of_repair}  | {self.Date_of_transfer}  | {self.FIO_Employee_passed_repair} | {self.Number__Employee_passed_repair}  | {self.FIO_Employee_accepted_repair}  | {self.Number__Employee_accepted_repair}  | {self.Position_of_repair_person}  | {self.technics_technics_inventory_num}  | {self.technics_Division_Division_num} '
    @staticmethod
    def get_tr():
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        result = []
        c.execute('select * from technics_repair')
        rows = c.fetchall()
        for row in rows:
            trs = Technics_repair(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8],row[9], row[10], row[11])
            result.append(trs)
        c.close()
        conn.close()
        return result

    @staticmethod
    def del_tr(technics_repair_num):
        try:
            dl = "DELETE FROM technics_repair WHERE technics_repair_num = %s"
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            c.execute(dl, (technics_repair_num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def change_tr(technics_repair_num, Date_of_delivery_for_repair, Repair_period,Type_of_repair,Date_of_transfer, FIO_Employee_passed_repair, Number__Employee_passed_repair, FIO_Employee_accepted_repair,  Number__Employee_accepted_repair, Position_of_repair_person, technics_technics_inventory_num, technics_Division_Division_num):
        try:
            conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
            c = conn.cursor()
            ch1 = """UPDATE technics_repair SET Date_of_delivery_for_repair = %s, Repair_period = %s, Type_of_repair = %s,Date_of_transfer = %s,  FIO_Employee_passed_repair = %s, Number__Employee_passed_repair = %s, FIO_Employee_accepted_repair = %s, Number__Employee_accepted_repair = %s, Position_of_repair_person = %s, technics_technics_inventory_num = %s, technics_Division_Division_num = %s WHERE technics_repair_num = %s"""
            ch2=(Date_of_delivery_for_repair, Repair_period,Type_of_repair,Date_of_transfer, FIO_Employee_passed_repair, Number__Employee_passed_repair, FIO_Employee_accepted_repair,  Number__Employee_accepted_repair, Position_of_repair_person, technics_technics_inventory_num, technics_Division_Division_num, technics_repair_num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def add_tr(technics_repair_num, Date_of_delivery_for_repair, Repair_period,Type_of_repair,Date_of_transfer, FIO_Employee_passed_repair, Number__Employee_passed_repair, FIO_Employee_accepted_repair,  Number__Employee_accepted_repair, Position_of_repair_person, technics_technics_inventory_num, technics_Division_Division_num):
        conn = mysql.connector.connect(user='root', password='1234', host='localhost', database='lab4')
        c = conn.cursor()
        c.execute('insert into technics_repair values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', \
            (int(technics_repair_num), Date_of_delivery_for_repair, Repair_period,Type_of_repair,Date_of_transfer, FIO_Employee_passed_repair, int(Number__Employee_passed_repair), FIO_Employee_accepted_repair,  int(Number__Employee_accepted_repair), Position_of_repair_person, int(technics_technics_inventory_num), int(technics_Division_Division_num), ))
        conn.commit()
        c.close()
        conn.close()