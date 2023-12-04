import win32print
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QObject, pyqtSlot, QUrl, QSizeF, QMarginsF, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import QPrinter
import sys
import codecs
import kk


################################################
html="C:\\Users\\User\\Desktop\\DjangoAdmin\\templates\\receipt1.html"
file = codecs.open(html,'r','utf-8')
################################################
def print_complete(result):
    app.quit()


# Start printing small ticket
def goto_print_litbill():
    webview.page().print(printer, print_complete)


################################################
#######Program Entry
################################################
if  __name__ == '__main__':
    app = QApplication(sys.argv)
    webview = QWebEngineView()
    webview.setHtml(file.read())
    #webview.show()
    win32print.SetDefaultPrinter("LocalPrinter on 192.168.1.125")  #Set as the default printer
    printer = QPrinter()
    printer.setPageSizeMM(QSizeF(80, 300))
    ########## Printing must be delayed, otherwise the web page has not been loaded yet, and the printing is blank #########
    timer = QTimer()
    timer.timeout.connect(goto_print_litbill)
    timer.setSingleShot(True)
    timer.start(800)
    ###################################################
    sys.exit(app.exec_())
