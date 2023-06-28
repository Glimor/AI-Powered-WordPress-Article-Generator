from PyQt6 import QtWidgets
import sys
from gui.settings import Ui_Dialog
from gui.main import Main_Dialog
from db.database_settings import DatabaseSettings
from publisher.main import StartBot

class Settings(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.save_settings)
        self.settings = DatabaseSettings()
        self.settings.get_api_key()
        self.datas = self.settings.get_all_data("settings")
        if self.datas != []:
            self.load_settings()

    def load_settings(self):
        self.api_key = self.datas[0][1]
        self.wp_api_url = self.datas[0][2]
        self.wp_username = self.datas[0][3]
        self.wp_password = self.datas[0][4]
        self.sleep_time = self.datas[0][5]
        self.max_length = self.datas[0][6]

        self.ui.lineEdit.setText(self.api_key)
        self.ui.lineEdit_2.setText(self.wp_api_url)
        self.ui.lineEdit_3.setText(self.wp_username)
        self.ui.lineEdit_4.setText(self.wp_password)
        self.ui.lineEdit_5.setText(self.sleep_time)
        self.ui.lineEdit_6.setText(self.max_length)

    def save_settings(self):

        self.api_key = self.ui.lineEdit.text()
        self.wp_api_url = self.ui.lineEdit_2.text()
        self.wp_username = self.ui.lineEdit_3.text()
        self.wp_password = self.ui.lineEdit_4.text()
        self.sleep_time = self.ui.lineEdit_5.text()
        self.max_length = self.ui.lineEdit_6.text()

        if self.settings.get_api_key() is None:
            self.settings.insert_one(api_key=self.api_key, wp_api_url=self.wp_api_url, wp_username=self.wp_username, wp_password=self.wp_password, sleep_time=self.sleep_time, max_length=self.max_length)
        else:
            self.settings.update_one(api_key=self.api_key, wp_api_url=self.wp_api_url, wp_username=self.wp_username, wp_password=self.wp_password, sleep_time=self.sleep_time, max_length=self.max_length)
        self.main = Main()
        self.main.show()
        self.close()


class Main(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Main_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
        self.settings = DatabaseSettings()
        self.datas = self.settings.get_all_data("settings")
        self.sleep_time = self.datas[0][5]
        self.ui.label_5.setText(":" + self.sleep_time)

    def read_text(self):
        text = self.ui.textEdit.toPlainText()
        return text.splitlines()

    def start(self):
        self.text = self.read_text()
        for text in self.text:
            self.settings.insert_keyword(text)
        start = StartBot(self.ui)
        start.crawl()
        start.generate()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Settings()
    window.show()
    sys.exit(app.exec())