import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from google_currency import convert

import requests
api_key = '21XTTGBDL2CBO627'
def convert(input_currency,output_currency,input_amount):
    from_d = input_currency
    to_c = output_currency

    # Kiritiladigan qiymat
    amount = input_amount

    base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
    main_url = base_url + '&from_currency=' + from_d + '&to_currency=' + to_c + '&apikey=' + api_key

    response = requests.get(main_url)
    result = response.json()

    key = result['Realtime Currency Exchange Rate']
    rate = key['5. Exchange Rate']
    rate=float(rate)
    x=rate*amount

    return round(x,2)


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.setFixedSize(480, 700)

    def init_UI(self):
        self.setWindowTitle('Valyuta konverter dasturi.  By @MrCoder_99')
        self.setWindowIcon(QIcon('logo.ico'))
        self.ui.input_currency.setPlaceholderText('Qaysi valyutadan:')
        self.ui.input_amount.setPlaceholderText('Mavjud valyuta:')
        self.ui.output_currency.setPlaceholderText('Qaysi valyutaga:')
        self.ui.output_amount.setPlaceholderText('Summa:')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):

        input_currency = self.ui.input_currency.text()
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_amount.text())     
        output_amount = convert(input_currency,output_currency,input_amount)
        self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
 
sys.exit(app.exec())


