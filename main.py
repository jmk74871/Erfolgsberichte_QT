import csv
import os
import sys
import time

from qtpy import QtWidgets

from login.mainwindow import Ui_MainWindow
from sucsessreports.User import User
from ui.mainwindow import Ui_Erfolgsberichte

# ToDo:
#     create method to create the report
#     find way to make sure entry data is correct (mainly the date)
#       make tabel_erfolge readonly
#     check mailadress with regex when creating user


app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Erfolgsberichte()
        self.ui.setupUi(self)

        self.user = User(None, None)

        self.ui.tabel_erfolge.hideColumn(0)
        self.ui.tabel_erfolge.hideColumn(2)

        self.ui.mw_feedback_label.hide()

        self.ui.mw_button_show.clicked.connect(self.show_erfolge)
        self.ui.mw_button_new.clicked.connect(self._show_entry_widgets)
        self.ui.mw_button_save.clicked.connect(self.add_line)
        self.ui.mw_sammeln_button.clicked.connect(self.get_mail)
        self.ui.mw_cr_button.clicked.connect(self.create_report)

    def _hide_report_widgets(self):
        self.ui.mw_cr_button.hide()
        self.ui.mw_cr_cat_box.hide()
        self.ui.mw_cr_cat_label.hide()
        self.ui.mw_cr_from_date.hide()
        self.ui.mw_cr_from_label.hide()
        self.ui.mw_cr_to_date.hide()
        self.ui.mw_cr_to_label.hide()

    def _show_report_widgets(self):
        self.ui.mw_cr_button.show()
        self.ui.mw_cr_cat_box.show()
        self.ui.mw_cr_cat_label.show()
        self.ui.mw_cr_from_date.show()
        self.ui.mw_cr_from_label.show()
        self.ui.mw_cr_to_date.show()
        self.ui.mw_cr_to_label.show()

    def _hide_entry_widgets(self):
        self.ui.mw_button_save.hide()
        self.ui.mw_button_save.setDefault(False)
        self.ui.mw_ae_cat.hide()
        self.ui.mw_ae_date.hide()
        self.ui.mw_ae_text.hide()
        self.ui.mw_ae_cat_label.hide()
        self.ui.mw_ae_date_label.hide()
        self.ui.mw_ae_text_label.hide()

    def _show_entry_widgets(self):
        self.ui.mw_feedback_label.setText('Achtung: ungespeicherte Änderungen!')
        self.ui.mw_sammeln_button.clicked.connect(self.get_mail)
        self.ui.mw_button_save.show()
        self.ui.mw_button_save.setDefault(True)
        self.ui.mw_ae_cat.show()
        self.ui.mw_ae_date.show()
        self.ui.mw_ae_text.show()
        self.ui.mw_ae_cat_label.show()
        self.ui.mw_ae_date_label.show()
        self.ui.mw_ae_text_label.show()

    def get_user(self, user):
        self.user = user
        self.ui.label_user.setText(f'Angemeldet als: {self.user.name}')

    def get_mail(self):
        self._hide_report_widgets()
        self._hide_entry_widgets()

        self.save_erfolge()
        self.user.get_mail()
        self.show_erfolge()

    def add_line(self):
        date = '{year:04d}-{month:02d}-{day:02d}'.format(day=self.ui.mw_ae_date.date().day(),
                                                         month=self.ui.mw_ae_date.date().month(),
                                                         year=self.ui.mw_ae_date.date().year())

        row = self.ui.tabel_erfolge.rowCount()
        self.ui.tabel_erfolge.insertRow(row)
        self.ui.tabel_erfolge.setItem(row, 0, QtWidgets.QTableWidgetItem('---'))
        self.ui.tabel_erfolge.setItem(row, 1, QtWidgets.QTableWidgetItem(date))
        self.ui.tabel_erfolge.setItem(row, 2, QtWidgets.QTableWidgetItem(self.user.name))
        self.ui.tabel_erfolge.setItem(row, 3, QtWidgets.QTableWidgetItem(self.ui.mw_ae_cat.currentText()))
        self.ui.tabel_erfolge.setItem(row, 4, QtWidgets.QTableWidgetItem(self.ui.mw_ae_text.toPlainText()))

        self.save_erfolge()
        self._hide_entry_widgets()
        self.ui.mw_feedback_label.setText('')

    def show_erfolge(self):
        if self.ui.mw_feedback_label.text() == 'Achtung: ungespeicherte Änderungen!':
            pass
        else:
            self.ui.tabel_erfolge.setRowCount(0)
            with open(self.user.db_path, 'r', encoding='utf_8') as user_db:
                reader = csv.DictReader(user_db)
                for line in reader:
                    row = self.ui.tabel_erfolge.rowCount()
                    self.ui.tabel_erfolge.insertRow(row)
                    self.ui.tabel_erfolge.setItem(row, 0, QtWidgets.QTableWidgetItem(line['UID']))
                    self.ui.tabel_erfolge.setItem(row, 1, QtWidgets.QTableWidgetItem(line['DATE']))
                    self.ui.tabel_erfolge.setItem(row, 2, QtWidgets.QTableWidgetItem(line['FROM']))
                    self.ui.tabel_erfolge.setItem(row, 3, QtWidgets.QTableWidgetItem(line['CATEGORY']))
                    self.ui.tabel_erfolge.setItem(row, 4, QtWidgets.QTableWidgetItem(line['TEXT']))
            self.ui.mw_feedback_label.hide()

    def save_erfolge(self):
        if self.ui.tabel_erfolge.rowCount() == 0:
            pass
        else:
            with open(self.user.db_path, 'w', encoding='utf_8') as user_db:
                fnames = ["UID", "DATE", "FROM", "CATEGORY", "TEXT"]
                writer = csv.DictWriter(user_db, fnames, restval="---")
                writer.writeheader()  # nur ein mal

                for row in range(0, self.ui.tabel_erfolge.rowCount()):
                    writer.writerow({'UID': self.ui.tabel_erfolge.item(row, 0).text(),
                                     "DATE": self.ui.tabel_erfolge.item(row, 1).text(),
                                     "FROM": self.ui.tabel_erfolge.item(row, 2).text(),
                                     "CATEGORY": self.ui.tabel_erfolge.item(row, 3).text(),
                                     "TEXT": self.ui.tabel_erfolge.item(row, 4).text()})
            self.ui.mw_feedback_label.setText('Daten erfolgreich gespeichert')
            self.ui.mw_feedback_label.show()
            time.sleep(0.2)
            self.ui.mw_button_show.setFlat(False)
            self.show_erfolge()

    def create_report(self):
        # pass the filters
        self.user.create_report()


window = MainWindow()


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cu_feedback_label.hide()
        self.ui.login_feedback_label.hide()
        self.ui.login_button.clicked.connect(self.login)
        self.ui.cu_button.clicked.connect(self.create_user)

    def login(self):
        with open('./SR_Data/resources/user_db.csv', 'r', encoding='utf_8') as user_db:
            fnames = ['name', 'mail1', 'mail2', 'city', 'pw']
            reader = csv.DictReader(user_db, fnames, restkey='---')

            for user in reader:
                if user['pw'].strip() == self.ui.login_pw.text().strip() \
                        and user['name'].strip() == self.ui.login_name.text().strip():
                    cert_user = User(user['name'], user['mail1'])
                    window.get_user(cert_user)
                    window.get_mail()
                    window.show()

                    self.close()

        self.ui.login_name.setText('')
        self.ui.login_pw.setText('')
        self.ui.login_feedback_label.setText('Anmeldung fehlgeschlagen. '
                                             'Bitte Login-Daten prüfen und erneut versuchen.')
        self.ui.login_feedback_label.show()

    def create_user(self):
        with open('./SR_Data/resources/user_db.csv', 'a', encoding='utf_8') as user_db:
            fnames = ['name', 'mail1', 'mail2', 'city', 'pw']
            writer = csv.DictWriter(user_db, fnames, restval='---')
            name = self.ui.cu_name.text()
            mail1 = self.ui.cu_mail.text()
            pw = self.ui.cu_pw.text()
            cwd = os.getcwd()
            db_path = os.path.normpath(cwd + f'/SR_Data/userdata/db/{name}_db/')
            rep_path = os.path.normpath(cwd + f'/SR_Data/userdata/reports/{name}_reports/')

            if len(name) < 3:
                self.ui.cu_feedback_label.setText('Fehler: Benutzername muss mindestens 5 Zeichen lang sein!')
                self.ui.cu_feedback_label.show()
            elif os.path.exists(db_path):
                self.ui.cu_feedback_label.setText('Fehler: Ein Nutzer mit diesem Namen existiert bereits!')
                self.ui.cu_feedback_label.show()
            elif len(mail1) < 6:
                self.ui.cu_feedback_label.setText('Fehler: keine Mailadresse erkannt!')
                self.ui.cu_feedback_label.show()
            elif len(pw) < 8:
                self.ui.cu_feedback_label.setText('Fehler: Passwort muss mindestens 8 Zeichen lang sein!')
                self.ui.cu_feedback_label.show()
            elif pw == self.ui.cu_pw_rep.text():

                os.mkdir(db_path)
                os.mkdir(rep_path)
                writer.writerow({'name': name,
                                 'mail1': mail1,
                                 'mail2': self.ui.cu_mail2.text(),
                                 'pw': pw})
                file = f'./SR_Data/userdata/db/{name}_db/{name}_db.csv'
                with open(file, 'w', encoding='utf_8') as user_data:
                    fnames = ["UID", "DATE", "FROM", "CATEGORY", "TEXT"]
                    data_writer = csv.DictWriter(user_data, fnames, restval="---")
                    data_writer.writeheader()
                self.ui.cu_feedback_label.setText(f'Benutzer {name} wurde erfolgreich angelegt.')
                self.ui.cu_feedback_label.show()

                time.sleep(3)
                self.ui.tabWidget.setCurrentIndex(0)

            else:
                self.ui.cu_feedback_label.setText('Fehler beim Anlegen des Benutzers. Bitte prüfe Deine Angaben!')
                self.ui.cu_feedback_label.show()


login = LoginWindow()
login.show()
sys.exit(app.exec_())
