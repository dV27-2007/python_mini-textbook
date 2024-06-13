# ays labrerinere ognum e ashxatel QT 5 designer het
from PyQt5 import QtWidgets, uic# ogtagorcelu ui-file
import sys


# amen 'app' PyQt5 piti sarqi ir obyektayin 'app'( kam el @kzemplay class-i QApplication )
app = QtWidgets.QApplication(sys.argv)
# nerbrnelu hamar mer sarqac ui-file
window = uic.loadUi('untitled.ui')
# cuyc talu hamar
window.show()
# apahovum e chisht yelqe
sys.exit(app.exec_())
