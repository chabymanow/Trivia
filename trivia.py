import requests
import json
import webbrowser
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QDoubleValidator, QValidator
from PyQt5 import QtGui
from mainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.currentCat = ""
        self.categories = {"artliterature":"Art and Literature", "language":"Language","sciencenature":"Science and nature","general":"General",
                    "fooddrink":"Food and drink","peopleplaces":"People and places","geography":"Geography","historyholidays":"History and holidays","entertainment":"Entertainment",
                    "toysgames":"Toys and games","music":"Music","mathematics":"Mathematics","religionmythology":"Religion and mythology","sportsleisure":"Sports and leisure"}
        self.api_url = 'https://api.api-ninjas.com/v1/trivia?category='
        self.categoriesBox.activated.connect(self.selectCat)
        self.getButton.clicked.connect(self.getData)
        self.googleButton.clicked.connect(self.searchGoogle)
        self.fillCat()
        # self.getData()

    def searchGoogle(self):
        url = "http://www.google.com/search?q=" + self.questionLabel.text()
        webbrowser.open_new_tab(url)

    def fillCat(self):
        for cat in self.categories.keys():
            self.categoriesBox.addItem(self.categories[cat])
        self.categoryLabel.setText(self.categories["general"])
        self.categoriesBox.setCurrentIndex(3)
        
    def selectCat(self):
        keys_list = list(self.categories)
        self.currentCat = keys_list[self.categoriesBox.currentIndex()]
        self.categoryLabel.setText(self.categories[keys_list[self.categoriesBox.currentIndex()]])
        print(self.currentCat)

    def getData(self):  
        currURL = self.api_url + self.currentCat
        response = requests.get(currURL, headers={'X-Api-Key': 'GET_YOUR_API_KEY'})
        data = response.json()
        if response.status_code == requests.codes.ok:
            self.questionLabel.setText(data[0]["question"])
            self.answerLabel.setText(data[0]["answer"])
        else:
            print("Error:", response.status_code, response.text)

app = QtWidgets.QApplication(sys.argv)    
app.setWindowIcon(QtGui.QIcon('pngwing.com.png'))
window = MainWindow()
window.show()
app.exec()





