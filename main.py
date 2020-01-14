import sys
from PyQt5.QtWidgets import *

class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.okienko()
        
    def okienko(self):
        self.resize(500,100)
        self.setWindowTitle("Kalkulator")
        
        podajliczbe1 = QLabel("Podaj liczbe:", self)
        podajliczbe2 = QLabel("Podaj liczbe", self)
        wynik1 = QLabel("Wynik:", self)

        szkielet = QGridLayout()
        szkielet.addWidget(podajliczbe1, 0, 0)
        szkielet.addWidget(podajliczbe2, 0, 1)
        szkielet.addWidget(wynik1, 0, 2)

        self.setLayout(szkielet)
        self.setGeometry(20, 20, 300, 100)
        
        self.liczba1 = QLineEdit()
        self.liczba2 = QLineEdit()
        self.wynik = QLineEdit()
        self.wynik.readonly = True
       
        szkielet.addWidget(self.liczba1, 1, 0)
        szkielet.addWidget(self.liczba2, 1, 1)
        szkielet.addWidget(self.wynik, 1, 2)

        dodawanie = QPushButton("Dodaj", self)
        odejmowanie = QPushButton("Odejmij", self)
        dzielenie = QPushButton("Pomnóż", self)
        mnozenie = QPushButton("Podziel", self)

        przyciski = QHBoxLayout()
        przyciski.addWidget(dodawanie)
        przyciski.addWidget(odejmowanie)
        przyciski.addWidget(dzielenie)
        przyciski.addWidget(mnozenie)

        szkielet.addLayout(przyciski, 2, 0, 1, 3)
    
        dodawanie.clicked.connect(self.dzialanie)
        odejmowanie.clicked.connect(self.dzialanie)
        dzielenie.clicked.connect(self.dzialanie)
        mnozenie.clicked.connect(self.dzialanie)
        
        
        clear = QPushButton("Wyczysc pola", self)
        czyszczenie = QHBoxLayout()
        czyszczenie.addWidget(clear)
        
        szkielet.addLayout(czyszczenie, 3,0,1,4)
        clear.clicked.connect(self.czyszczenie)
        
        pytanie = QLabel("Czy jestes zadowolony z aplikacji?",self)
        odpowiedz1 = QRadioButton("TAK",self)
        odpowiedz2 = QRadioButton("NIE",self)
        
        ankieta = QHBoxLayout()
        
        ankieta.addWidget(odpowiedz1)
        ankieta.addWidget(odpowiedz2)
        
        szkielet.addWidget(pytanie, 4,0,1,4)
        szkielet.addLayout(ankieta, 5,0,1,4)
    
        self.show()
        
    def dzialanie(self):
        source = self.sender()
        try:
            liczba1 = float(self.liczba1.text())
            liczba2 = float(self.liczba2.text())
            
            if source.text() == "Dodaj":
                wynik = liczba1 + liczba2
            if source.text() == "Odejmij":
                wynik = liczba1 - liczba2
            if source.text() == "Pomnóż":
                wynik = liczba1 * liczba2
            if source.text() == "Podziel":
                wynik = liczba1 / liczba2
            if source.text() == "Podziel":
                round(self.wynik.setText(str(wynik)),2)
            else:
                self.wynik.setText(str(wynik))
        except ValueError:
            self.wynik.setText("Wprowadź poprawne liczby")
    def czyszczenie(self):
        source = self.sender()
        if source.text() == "Wyczysc pola":
            self.liczba1.setText("")
            self.liczba2.setText("")
            self.wynik.setText("")
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())