#!/usr/bin/env python
class View:
    @staticmethod
    def show_users(list):
        print(f'in database {len(list)} users. they are:')
        for item in list:
            print(item.info)
    @staticmethod
    def delete_users(list):
        print('Deleted')
    @staticmethod
    def change_info_users(list):
        print('Data is changed')
    @staticmethod
    def show_divisions(list):
        print(f'in database {len(list)} divisions. they are:')
        for item in list:
            print(item.info_div)
    @staticmethod
    def delete_divisions(list):
        print('Deleted')
    @staticmethod
    def change_info_divisions(list):
        print('Data is changed')

    @staticmethod
    def show_technics(list):
        print(f'in database {len(list)} technics. they are:')
        for item in list:
            print(item.info_tec)

    @staticmethod
    def delete_technics(list):
        print('Deleted')

    @staticmethod
    def change_info_technics(list):
        print('Data is changed')
    @staticmethod
    def show_documents(list):
        print(f'in database {len(list)} documents. they are:')
        for item in list:
            print(item.info_doc)

    @staticmethod
    def delete_documents(list):
        print('Deleted')

    @staticmethod
    def change_info_documents(list):
        print('Data is changed')

    @staticmethod
    def show_invoices(list):
        print(f'in database {len(list)} invoicess. they are:')
        for item in list:
            print(item.info_inv)

    @staticmethod
    def delete_invoices(list):
        print('Deleted')

    @staticmethod
    def change_info_invoices(list):
        print('Data is changed')

    @staticmethod
    def delete_backups(list):
        print('Deleted')

    @staticmethod
    def change_info_backups(list):
        print('Data is changed')

    @staticmethod
    def show_trs(list):
        print(f'in database {len(list)} technics_repair. they are:')
        for item in list:
            print(item.info_tr)

    @staticmethod
    def delete_trs(list):
        print('Deleted')

    @staticmethod
    def change_info_trs(list):
        print('Data is changed')

    @staticmethod
    def get_data(text):
        return input('enter ' + text + ':')
    @staticmethod
    def show_menu():
        print('what do you want:\n'+
            '\t (1) show users\n'+
            '\t (2) delete users\n' +
            '\t (3) change_info_users\n' +
            '\t (4) add user\n'+
            '\t (5) show divisions\n' +
            '\t (6) delete divisions\n' +
            '\t (7) change_info_divisions\n' +
            '\t (8) add division\n' +
            '\t (9) show technics\n' +
            '\t (10) delete technics\n' +
            '\t (11) change_info_technics\n' +
            '\t (12) add technic\n' +
            '\t (13) show documents\n' +
            '\t (14) delete documents\n' +
            '\t (15) change_info_documents\n' +
            '\t (16) add document\n' +
            '\t (17) show invoices\n' +
            '\t (18) delete invoices\n' +
            '\t (19) change_info_invoices\n' +
            '\t (20) add invoice\n' +
            '\t (21) delete backups\n' +
            '\t (22) change_info_backups\n' +
            '\t (23) add backup\n' +
            '\t (24) show trs\n' 
            '\t (25) delete trs\n' +
            '\t (26) change_info_trs\n' +
            '\t (27) add tr\n' +
            '\t (28) exit\n')
