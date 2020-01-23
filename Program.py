from PyQt5.QtWidgets import QLabel,QVBoxLayout,QWidget,QApplication,QPushButton,QComboBox
import requests
import sys
from PyQt5.QtGui import QIcon

class Program(QWidget):
    def __init__(self):
        super().__init__()

        self.aq()

    def aq(self):

        url = "http://data.fixer.io/api/latest?access_key=APIKEYINIZBURAYAYAZILIR&format=1"
        response = requests.get(url)
        jsonveri = response.json()

        self.tarh = QLabel("")
        b = (jsonveri["date"])
        self.tarh.setText(b + " Şu tarihteki dövizler  : ")

        self.bir = QComboBox(self)
        self.birad = QLabel("Çevirilecek birinci değer : ")

        a = (jsonveri["rates"].keys())
        self.bir.addItems(a)

        self.iki = QComboBox(self)
        self.ikiad = QLabel("Çevirilecek ikinci değer : ")
        self.iki.addItems(a)

        self.yaz = QLabel("")

        self.button = QPushButton("Çevir!")


        vbox = QVBoxLayout()
        vbox.addWidget(self.tarh)
        vbox.addWidget(self.birad)
        vbox.addWidget(self.bir)
        vbox.addWidget(self.ikiad)
        vbox.addWidget(self.iki)
        vbox.addWidget(self.yaz)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.show()
        self.setGeometry(400,150,250,200)
        self.setWindowTitle("Döviz Çevirme")

        self.button.clicked.connect(self.tkla)

    def tkla(self):

        url1 = "http://data.fixer.io/api/latest?access_key=58bc90d630d2078958e35693b47afd6c&format=1"
        response = requests.get(url1)
        jsonveri2 = response.json()

        bra = self.bir.currentText()
        lan = (jsonveri2["rates"][bra])

        kra = self.iki.currentText()
        van = (jsonveri2["rates"][kra])


        opa = van / lan

        self.yaz.setText("1 {}, {} {} yapar.".format(bra,opa,kra))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('AK.78.png'))
    aaaa = Program()
    sys.exit(app.exec_())
