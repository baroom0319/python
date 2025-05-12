#text.txt를 읽어와서
#outTest.text파일에 작성한다.
inFile = open("test.txt", "r", encoding="UTF-8")
outfile = open("outTest.txt", "w", encoding="UTF-8")

while True:
    strFile = inFile.readline()
    if(strFile == ""):  
        break
    outfile.writelines(strFile) 

inFile.close()
outfile.close()