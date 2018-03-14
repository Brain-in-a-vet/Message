#!/Usr/Bin/Python2
import sys
import os
from  pyPdf import PdfFileReader, PdfFileWriter

def merge(input_dir,output_dir,filename):
    input_name= input_dir+filename
    input_one = file(input_name, 'rb')

    
    pdf_input_one = PdfFileReader(input_one)

    
    numOne = pdf_input_one.getNumPages()

    print numOne

    pdf_output = PdfFileWriter()
    
    index_i = 0
    check = numOne%2
    if check == 1 :
        index_center = numOne//2
    else:
        index_center = numOne//2-1
    index_j = index_center+1

    
    while True:
        if index_i > index_center:break

        page1=pdf_input_one.getPage(index_i)
        pdf_output.addPage(page1)

        if index_j == numOne:break
        page2=pdf_input_one.getPage(index_j)
        pdf_output.addPage(page2)

        index_i += 1
        index_j += 1


    pdf_name = output_dir+filename
    
    output_stream = file( pdf_name,'wb')
    pdf_output.write(output_stream) 
    output_stream.close()
    input_one.close()
    print 'Done!'



merge("/Users/yinyilin/Desktop/problem/input/","/Users/yinyilin/Desktop/problem/output/","java1.pdf")
merge("/Users/yinyilin/Desktop/problem/input/","/Users/yinyilin/Desktop/problem/output/","java2.pdf")
merge("/Users/yinyilin/Desktop/problem/input/","/Users/yinyilin/Desktop/problem/output/","jvm1.pdf")
merge("/Users/yinyilin/Desktop/problem/input/","/Users/yinyilin/Desktop/problem/output/","jvm2.pdf")
merge("/Users/yinyilin/Desktop/problem/input/","/Users/yinyilin/Desktop/problem/output/","mysql1.pdf")
merge("/Users/yinyilin/Desktop/problem/input/","/Users/yinyilin/Desktop/problem/output/","mysql2.pdf")
merge("/Users/yinyilin/Desktop/problem/input/","/Users/yinyilin/Desktop/problem/output/","nginx1.pdf")