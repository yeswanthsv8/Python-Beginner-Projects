"""
Text to Speech{Pdf file}
What is the use of binary mode?
Binary mode allows programmers to manipulate files byte by byte rather than in larger logical structures.

init(): Speaker Intialisation
runAndWait():
This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you.

Modules:
pyttsx3: Text to Speech
PyPDF2:  To read Pdf file
"""


import pyttsx3
import PyPDF2
book=open('OOPS.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()

for num in range(6,pages):
    page=pdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()