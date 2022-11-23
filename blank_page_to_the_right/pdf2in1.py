from PyPDF2 import PdfReader, PdfWriter, Transformation


def add_blank_page_to_the_right(fname):

    basefile = PdfReader("blankpage.pdf")
    blankpage = basefile.pages[0]
    x = float(blankpage.mediabox[2])/2
    y = float(blankpage.mediabox[3])
    blankX, blankY = x - 40, y - 40 


    reader = PdfReader(fname)
    n = reader.getNumPages()

    writer = PdfWriter()

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

        
    # write the new pdf file 
    
    newname = fname.split(".pdf")[0]
    newname += "_PyPDF2.pdf"
    
    with open(newname, "wb") as fp:
        writer.write(fp)

        
if __name__ == "__main__":
#     add_blank_page_to_the_right("test.pdf")
