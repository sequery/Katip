from selenium import webdriver
import win32com.client
import win32print
import time

def printpdf(pdf,printer):
    current_printer = win32print.GetDefaultPrinter()
    win32print.SetDefaultPrinter(printer)
    driver = webdriver.Chrome()
    driver.get(pdf)
    time.sleep(1) #Adjust as necessary
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('^p')
    time.sleep(1) #Adjust as necessary
    shell.SendKeys('{ENTER}') #dismiss the print dialog box
    driver.close()
    win32print.SetDefaultPrinter(current_printer)
    