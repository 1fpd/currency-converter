import requests
import sys
import random
from PyQt5.QtWidgets import QApplication, QDialog   
from untitled import Ui_Dialog  
import qdarktheme

class CurrencyConverterApp(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.api_keys = [
            "b2733b0d275fa957e085b4e02906e18f",
            "3c47c018956967328dc1391f95d72071",
            "c38f096d4fdcd0fc7668d138771d35a8",
            "7100710c99e3e4a5bf67693ff58d7329"
        ]
        self.rates = {}
        self.load_exchange_rates()
        
        
        currencies = ["USD","AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "CNH", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL", "SOS", "SRD", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XCG", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]
        self.currfrom.addItems(currencies)
        self.currto.addItems(currencies)
        
        
        self.currfrommoney.textChanged.connect(self.convert_currency)
        self.currfrom.currentTextChanged.connect(self.convert_currency)
        self.currto.currentTextChanged.connect(self.convert_currency)

    def load_exchange_rates(self):
        try:
            random_key = random.choice(self.api_keys)
            url = f"http://data.fixer.io/api/latest?access_key={random_key}"
            data = requests.get(url).json()
            if data.get("success"):
                self.rates = data["rates"]
                self.bigmoney.setText("Ready")
            else:
                self.bigmoney.setText("Error")
        except Exception as e:
            self.bigmoney.setText("Network Error")

    def convert_currency(self):
        if not self.rates:
            return
        try:
            from_currency = self.currfrom.currentText().strip()
            to_currency = self.currto.currentText().strip()
            amount_text = self.currfrommoney.text().strip()
            
            if not amount_text or not from_currency or not to_currency:
                return
            amount = float(amount_text)
            
            
            if from_currency != 'EUR':
                converted = amount / self.rates[from_currency]
            converted = round(converted * self.rates[to_currency], 2)
            
            
            self.currtomoney.setText(str(converted))
            self.bigmoney.setText(f"{amount} {from_currency}")
            self.equalsmoney.setText(f"= {converted} {to_currency}")
            
        except ValueError:
            self.currtomoney.setText("Invalid")
        except Exception as e:
            self.currtomoney.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet())
    window = CurrencyConverterApp()
    window.show()
    sys.exit(app.exec_())   