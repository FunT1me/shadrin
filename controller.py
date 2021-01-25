#!/usr/bin/env python
from model import User,Division,Technics,Document,Invoice,Backups,Technics_repair
from view import View
class Controller:
    def show_users(self):
        users = User.get_user()
        return View.show_users(users)
    def delete_users(self):
        num=View.get_data('user_id')
        users = User.del_user(num)
        return View.delete_users(users)
    def change_info_users(self):
        user_id = View.get_data('user_id')
        user_post = View.get_data('user_post')
        user_date_start_work = View.get_data('user_date_start_work')
        user_date_end_work = View.get_data('user_date_end_work')
        user_password = View.get_data('user_password')
        user_login = View.get_data('user_login')
        user_FIO = View.get_data('user_FIO')
        Division_Division_num = View.get_data('Division_Division_num')
        users = User.change_user(user_id,user_post, user_date_start_work, user_date_end_work, user_password,user_login, user_FIO, Division_Division_num )
        return View.change_info_users(users)
    def add_user(self):
        user_id = View.get_data('user_id')
        user_post = View.get_data('user_post')
        user_date_start_work = View.get_data('user_date_start_work')
        user_date_end_work = View.get_data('user_date_end_work')
        user_password = View.get_data('user_password')
        user_login = View.get_data('user_login')
        user_FIO = View.get_data('user_FIO')
        Division_Division_num = View.get_data('Division_Division_num')
        users = User.add_user(user_id, user_post, user_date_start_work, user_date_end_work, user_password, user_login ,user_FIO, Division_Division_num)
    def show_divisions(self):
        divisions = Division.get_division()
        return View.show_divisions(divisions)
    def delete_divisions(self):
        num = View.get_data('Division_num')
        divisions = Division.del_division(num)
        return View.delete_divisions(divisions)
    def change_info_divisions(self):
        num = View.get_data('Division_num')
        num1 = View.get_data('Division_name')
        divisions = Division.change_division(num, num1)
        return View.change_info_divisions(divisions)

    def add_division(self):
        Division_num = View.get_data('Division_num')
        Division_name = View.get_data('Division_name')
        Divisions = Division.add_division(Division_num, Division_name)

    def show_technics(self):
        technics = Technics.get_technic()
        return View.show_technics(technics)
    def delete_technics(self):
        num = View.get_data('technics_inventory_num')
        technics = Technics.del_technic(num)
        return View.delete_technics (technics)
    def change_info_technics(self):
        technics_inventory_num = View.get_data('technics_inventory_num')
        technics_name = View.get_data('technics_name')
        technics_model = View.get_data('technics_model')
        technics_year_of_release = View.get_data('technics_year_of_release')
        Division_Division_num = View.get_data('technics_inventory_num')
        technics = Technics.change_technic(technics_inventory_num, technics_name, technics_model, technics_year_of_release, Division_Division_num)
        return View.change_info_technics(technics)

    def add_technic(self):
        technics_inventory_num = View.get_data('technics_inventory_num')
        technics_name = View.get_data('technics_name')
        technics_model = View.get_data('technics_model')
        technics_year_of_release = View.get_data('technics_year_of_release')
        Division_Division_num = View.get_data('technics_inventory_num')
        technics = Technics.add_technic(technics_inventory_num, technics_name, technics_model,technics_year_of_release, Division_Division_num)

    def show_documents(self):
        documents = Document.get_document()
        return View.show_documents(documents)

    def delete_documents(self):
        num = View.get_data('document_num')
        documents = Document.del_document(num)
        return View.delete_documents(documents)

    def change_info_documents(self):
        document_num = View.get_data('document_num')
        document_date_of_transfer = View.get_data('document_date_of_transfer')
        technics_technics_inventory_num = View.get_data('technics_technics_inventory_num')
        technics_Division_Division_num = View.get_data('technics_year_of_release')
        documents = Document.change_document(document_num, document_date_of_transfer, technics_technics_inventory_num,
                                             technics_Division_Division_num)
        return View.change_info_documents(documents)

    def add_document(self):
        document_num = View.get_data('document_num')
        document_date_of_transfer = View.get_data('document_date_of_transfer')
        technics_technics_inventory_num = View.get_data('technics_technics_inventory_num')
        technics_Division_Division_num = View.get_data('technics_year_of_release')
        documents = Document.add_document(document_num, document_date_of_transfer, technics_technics_inventory_num,
                                          technics_Division_Division_num)

    def show_invoices(self):
        invoices = Invoice.get_invoice()
        return View.show_invoices(invoices)
    def delete_invoices(self):
        num = View.get_data('invoice_num')
        invoices = Invoice.del_invoice(num)
        return View.delete_invoices (invoices)
    def change_info_invoices(self):
        invoice_num = View.get_data('invoice_num')
        invoice_price_componentParrt = View.get_data('invoice_price_componentParrt')
        invoice_list_of_required_spare_parts = View.get_data('invoice_list_of_required_spare_parts')
        technics_technics_inventory_num= View.get_data('technics_technics_inventory_num')
        technics_Division_Division_num= View.get_data('technics_Division_Division_num')
        invoices = Invoice.change_invoice(invoice_num, invoice_price_componentParrt,invoice_list_of_required_spare_parts,technics_technics_inventory_num, technics_Division_Division_num)
        return View.change_info_invoices(invoices)

    def add_invoice(self):
        invoice_num = View.get_data('invoice_num')
        invoice_price_componentParrt = View.get_data('invoice_price_componentParrt')
        invoice_list_of_required_spare_parts = View.get_data('invoice_list_of_required_spare_parts')
        technics_technics_inventory_num = View.get_data('technics_technics_inventory_num')
        technics_Division_Division_num = View.get_data('technics_Division_Division_num')
        invoices = Invoice.add_invoice(invoice_num, invoice_price_componentParrt,invoice_list_of_required_spare_parts,technics_technics_inventory_num, technics_Division_Division_num)

    def delete_backups(self):
        num = View.get_data('backups_num')
        backups = Backups.del_backup(num)
        return View.delete_backups (backups)
    def change_info_backups(self):
        backups_num = View.get_data('backups_num')
        backups_date = View.get_data('backups_date')
        backups_versional = View.get_data('backups_versional')
        backups = Backups.change_backup(backups_num, backups_date,backups_versional)
        return View.change_info_backups(backups)

    def add_backup(self):
        backups_num = View.get_data('backups_num')
        backups_date = View.get_data('backups_date')
        backups_versional = View.get_data('backups_versional')
        backups = Backups.add_backup(backups_num, backups_date,backups_versional)

    def show_trs(self):
        trs = Technics_repair.get_tr()
        return View.show_trs(trs)
    def delete_trs(self):
        num = View.get_data('technics_repair_num')
        trs = Technics_repair.del_tr(num)
        return View.delete_trs (trs)
    def change_info_trs(self):
        technics_repair_num = View.get_data('technics_repair_num')
        Date_of_delivery_for_repair = View.get_data('Date_of_delivery_for_repair')
        Repair_period = View.get_data('Repair_period')
        Type_of_repair= View.get_data('Type_of_repair')
        Date_of_transfer= View.get_data('Date_of_transfer')
        FIO_Employee_passed_repair = View.get_data('FIO_Employee_passed_repair')
        Number__Employee_passed_repair = View.get_data('Number__Employee_passed_repair')
        FIO_Employee_accepted_repair = View.get_data('FIO_Employee_accepted_repair')
        Number__Employee_accepted_repair= View.get_data('Number__Employee_accepted_repair')
        Position_of_repair_person= View.get_data('Position_of_repair_person')
        technics_technics_inventory_num = View.get_data('technics_technics_inventory_num')
        technics_Division_Division_num = View.get_data('technics_Division_Division_num')
        trs = Technics_repair.change_tr(technics_repair_num, Date_of_delivery_for_repair, Repair_period,Type_of_repair,Date_of_transfer, FIO_Employee_passed_repair, Number__Employee_passed_repair, FIO_Employee_accepted_repair,  Number__Employee_accepted_repair, Position_of_repair_person, technics_technics_inventory_num, technics_Division_Division_num)
        return View.change_info_trs(trs)

    def add_tr(self):
        technics_repair_num = View.get_data('technics_repair_num')
        Date_of_delivery_for_repair = View.get_data('Date_of_delivery_for_repair')
        Repair_period = View.get_data('Repair_period')
        Type_of_repair= View.get_data('Type_of_repair')
        Date_of_transfer= View.get_data('Date_of_transfer')
        FIO_Employee_passed_repair = View.get_data('FIO_Employee_passed_repair')
        Number__Employee_passed_repair = View.get_data('Number__Employee_passed_repair')
        FIO_Employee_accepted_repair = View.get_data('FIO_Employee_accepted_repair')
        Number__Employee_accepted_repair= View.get_data('Number__Employee_accepted_repair')
        Position_of_repair_person= View.get_data('Position_of_repair_person')
        technics_technics_inventory_num = View.get_data('technics_technics_inventory_num')
        technics_Division_Division_num = View.get_data('technics_Division_Division_num')
        trs = Technics_repair.add_tr(technics_repair_num, Date_of_delivery_for_repair, Repair_period,Type_of_repair,Date_of_transfer, FIO_Employee_passed_repair, Number__Employee_passed_repair, FIO_Employee_accepted_repair,  Number__Employee_accepted_repair, Position_of_repair_person, technics_technics_inventory_num, technics_Division_Division_num)


    def run(self):
        choice = 0
        choices = {
            1 : lambda : self.show_users(),
            2: lambda: self.delete_users(),
            3: lambda: self.change_info_users(),
            4 : lambda : self.add_user(),
            5: lambda: self.show_divisions(),
            6: lambda: self.delete_divisions(),
            7: lambda: self.change_info_divisions(),
            8: lambda: self.add_division(),
            9: lambda: self.show_technics(),
            10: lambda: self.delete_technics(),
            11: lambda: self.change_info_technics(),
            12: lambda: self.add_technic(),
            13: lambda: self.show_documents(),
            14: lambda: self.delete_documents(),
            15: lambda: self.change_info_documents(),
            16: lambda: self.add_document(),
            17: lambda: self.show_invoices(),
            18: lambda: self.delete_invoices(),
            19: lambda: self.change_info_invoices(),
            20: lambda: self.add_invoice(),
            21: lambda: self.delete_backups(),
            22: lambda: self.change_info_backups(),
            23: lambda: self.add_backup(),
            24: lambda: self.show_trs(),
            25: lambda: self.delete_trs(),
            26: lambda: self.change_info_trs(),
            27: lambda: self.add_tr()
         }
        while (choice != 28):
            View.show_menu()
            choice = int(View.get_data('choice option'))
            if choice in choices:
                choices[choice]()


if __name__ == '__main__':
    Controller().run()
