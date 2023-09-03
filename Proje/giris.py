import sys
from PyQt5.QtWidgets import *
from giris_ui import Ui_Giris
from anaekran import Anaekran

class GirisPenceresi(QWidget, Ui_Giris):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # **** şifre olarak göstermek için
        self.sifreText.setEchoMode(QLineEdit.Password)
        self.GirisButonu.clicked.connect(self.fGirisKontrol)

    def fGirisKontrol(self):
        self.mesajLabel.setText("Giriş Butonu Tıklandı")
        # bolum 2
        eposta = self.epostaText.text()
        sifre = self.sifreText.text()
        if eposta == "ali" and sifre == "12345":
            self.mesajLabel.setText("Giriş Onaylandı")
            self.close()
            self.ype = Anaekran()
            self.ype.show()
        else:
            self.mesajLabel.setText("Hatalı Giriş Yapıldı")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GirisPenceresi()
    pencere.show()
    sys.exit(app.exec_())

# python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
