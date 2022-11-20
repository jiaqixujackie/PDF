from PyPDF2 import PdfMerger, PdfFileReader

def insertNewPage(fname:str):

    blankpage = open("blankpage.pdf","rb")  # the blank page

    curr_pdf = open(fname,"rb")             # original pdf
    n = PdfFileReader(curr_pdf).numPages    # number of pages

    newpdf = PdfMerger()                    # create the merging object

    for i in range(n):       # doing the actual merge
        newpdf.append(fileobj = curr_pdf, pages = (i, i+1))
        newpdf.append(fileobj = blankpage, pages = (0,1))

    # write ouput to the computer
    output = open(fname+"_new.pdf", "wb") 
    newpdf.write(output)

    # close all files
    blankpage.close()
    curr_pdf.close()
    newpdf.close()
    output.close()