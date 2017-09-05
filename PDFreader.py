import PyPDF2

def extract_pdf(filename):
    read_pdf = PyPDF2.PdfFileReader(filename,'rb')
    number_of_pages = read_pdf.numPages
    print(number_of_pages)
    count=0
    text=""

    while count<number_of_pages:
        pageObj=read_pdf.getPage(count)
        count +=1
        text +=pageObj.extractText()
        lines=text.split(".")

    return(lines)
    #return(text)
