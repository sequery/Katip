# U must install pywin32 and import modules:
import win32print, win32ui, win32con, os
import PyPDF2
# X from the left margin, Y from top margin 
# both in pixels
X=50; Y=50
# Separate lines from Your string 

fd = open("Record.txt", "rb")


input_string = fd.read()

# pdfReader = PyPDF2.PdfFileReader(fd)
 
# # creating a page object
# pageObj = pdfReader.getPage(0)
 
# # extracting text from page
# input_string = pageObj.extractText()
 
# print(input_string)
# # new string for example: multi_line_string 
multi_line_string = input_string.splitlines()  
hDC = win32ui.CreateDC()
# Set default printer from Windows:
hDC.CreatePrinterDC ( win32print.GetDefaultPrinter ())
hDC.StartDoc ("the_name_will_appear_on_printer_spool")
hDC.StartPage ()
for line in multi_line_string:
     hDC.TextOut(X,Y,line)
     Y += 100
hDC.EndPage ()
hDC.EndDoc ()

# closing the pdf file object
fd.close()