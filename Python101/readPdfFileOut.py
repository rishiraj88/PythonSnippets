# script to read text out of a PDF file
# may be readied in the form of a utility module as well
import pyttsx3
import PyPDF2

speaker = pyttsx3.init()
speaker.say("I'll read out for you.")

#code for previous version of library PyPDF2
'''pdfFile = open("privacyPolicy-GDPR+Wefox.pdf",mode="rb")
reader = PyPDF2.PdfFileReader(pdfFile)
nPages = reader.numPages
print(nPages)

pdfPage = reader.getPage(0)
content = pdfPage.extractText()
speaker.say(content)
speaker.runAndWait()'''

# nice and working code for currently updated version of library PyPDF2
pdfFile = open("o2c_otc.pdf",mode="rb")
reader = PyPDF2.PdfReader(pdfFile)
nPages = reader.pages
print(nPages)

pdfPage = reader.pages[0]
content = pdfPage.extract_text()
speaker.say(content)
speaker.runAndWait()
