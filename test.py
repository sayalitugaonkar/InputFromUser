import os
import os as walk

f_size=0
def main():
    for root, dirs, files in os.walk("/Users/akshaysulakhe/downloads"):
        for file in files:
            filedir=os.path.join(root,file)
            f_size= os.path.getsize(filedir)
            if file.endswith('.pdf'):
             pdfarray=
                print("file is a pdf ",file)
            print("filenname and size",file,f_size)
        break


if __name__== "__main__":
    main()


