import PyPDF2

file =   open("sample.pdf", "rb")

reader = PyPDF2.PdfFileReader(file)
page1 = reader.getPage(0)
pdfdata = page1.extractText()
print("data from page 1 "+pdfdata)
print(reader.numPages)


page2 = reader.getPage(1)
pdfdata = page2.extractText()
print("data from page 2 " +pdfdata)

assert  "demonstration" in pdfdata

assert  "demonstration" in pdfdata