from importlib.resources import path
import os,os.path 
from posixpath import split
import string
from time import time
import PyPDF2
import time
import glob

def count():
    return sum(len(files) for _, _, files in os.walk(r"C:\Users\Nattapong\OneDrive - KMITL\Office Lens"))

filecount = count()
while True:
    time.sleep(1)
    if count() > filecount:   
        list_of_files = glob.glob(r'C:\Users\Nattapong\OneDrive - KMITL\Office Lens\*')
        latest_file_path = max(list_of_files, key=os.path.getctime)
        file_name = os.path.basename(latest_file_path)
        split_file_extension = os.path.splitext(file_name)
        print(split_file_extension[0],split_file_extension[1])
        if(split_file_extension[1] == '.pdf'): 
            splitName = file_name.split(' ')       
            if (len(splitName)  == 5):
                try:
                    with open(latest_file_path, 'rb') as pdfFile:

                        pdfReader = PyPDF2.PdfFileReader(pdfFile)

                        for pageNum in range(pdfReader.numPages):
                            pdfWriter = PyPDF2.PdfFileWriter()
                            if(pageNum < 10):
                                splitName.insert(2, "p0" + str(pageNum + 1))
                            else:
                                splitName.insert(2, "p" + str(pageNum + 1))
                            finalName = ' '.join(splitName)
                            final_path = os.path.join(r"C:\Users\Nattapong\OneDrive - KMITL\การบ้านสยาม", finalName)
                            pdfWriter.addPage(pdfReader.getPage(pageNum))
                            with open(final_path + ".pdf", 'wb') as newFile:
                                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                                pdfWriter.write(newFile)
                            newFile.close()
                            print("file " + finalName + " created")
                            splitName.pop(2)
                        print("PDF file splited successfully")

                except FileNotFoundError as e:
                    print("File not found")
            else:
                print("name format not match")
        else:
            continue


            
    filecount = count()
    
    
    