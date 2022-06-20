import csv
import PyPDF2
import re
#   ask One: Use Python to extract the Google Drive link from the .csv file.
#   (Hint: Its along the diagonal from top left to bottom right).
#   T ask Two: Download the PDF from the Google Drive link
#   (we already downloaded it for you just in case you can't download from Google Drive)
#   and find the phone number that is in the document. Note: There are different ways of formatting a phone number!
if '__main__' == __name__:
    file = open('find_the_link.csv')
    file_data = csv.reader(file)
    lines = list(file_data)
    #   diagonally existing alphabets
    n = len(lines)
    #   a list to be appended, leading to the completion of the link
    link = []
    j = 0
    for i in range(0, n):
        link.append(lines[i][j])
        j += 1
    extracted_link = ''.join(link)

    pdf_file = open('Find_the_Phone_Number.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_page_list = []
    #   grab each page, extract the text from each page and store in a list
    for a in range(0, pdf_reader.numPages):
        each_page = pdf_reader.getPage(a)
        pdf_page_list.append(each_page.extractText())

    entire_text = ''.join(pdf_page_list)
    phone = re.search('\d\d\d.\d\d\d.\d\d\d\d', entire_text)
    print(phone)


