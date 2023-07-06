import os 
from PyPDF2 import PdfReader, PdfWriter, Transformation

def add_blank_page_to_the_right(pdfFolder, pdfFile):
    """
    param pdfFolder: path of the folder which contains the PDF to be processed
    param pdfFile: the PDF file to be process
    """
    
    # blank page 
    basefile = PdfReader("blankpage.pdf")
    blankpage = basefile.pages[0]
    x = float(blankpage.mediabox[2])/2
    y = float(blankpage.mediabox[3])
    blankX, blankY = x - 40, y - 40 

    # get the pdf file path
    if pdfFile[-4:].lower() != ".pdf":
        pdfFile += ".pdf"
    fname = pdfFolder + "/" + pdfFile

    # read the pdf
    reader = PdfReader(fname)
    n = reader.getNumPages()

    # generate a pdf writer object
    writer = PdfWriter()

    # start merging the pdf and the blank page
    for i in range(n):

        writer.add_blank_page(width=842, height=595)   

        pagei = writer.pages[i]
        pagei.merge_page(blankpage)

        page = reader.pages[i]

        # transformation: scale page along y axis   
        pageY = float(page.mediabox[3])
        scaleY = blankY / pageY
        if scaleY < 1:
            reduction = Transformation().scale(sx=scaleY, sy=scaleY)
            page.add_transformation(reduction)
        elif scaleY > 1:
            page.scale_by(scaleY)


        # transformation: scale horizontally 
        pageX = float(page.mediabox[2])
        pageX *= scaleY if scaleY < 1 else 1
        scaleX = blankX / pageX
        if scaleX < 1: 
            reduction = Transformation().scale(sx=scaleX, sy=scaleX)
            page.add_transformation(reduction)

        # transformation: translate/move left
        pointL = x - blankX
        leftShift = Transformation().translate(tx = pointL)
        page.add_transformation(leftShift)

        # transformation: translate/move up 
        finalY = pageY
        finalY *= scaleY
        finalY *= scaleX if scaleX < 1 else 1
        topShift = Transformation().translate(ty = (y - finalY)/2)
        page.add_transformation(topShift)

        # merge them
        pagei.merge_page(page)

    # get the new working directory to save the merged pdf
    save_to_folder = pdfFolder + "/PyPDF"
    if not os.path.exists(save_to_folder):
        os.makedirs(save_to_folder)
    save_to_path = save_to_folder + "/" + pdfFile

    # write the merged or processed pdf to the working directory
    with open(save_to_path, "wb") as fp:
        writer.write(fp)

