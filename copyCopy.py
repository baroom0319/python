#text.txt를 읽어와서
#outTest.text파일에 작성한다.
inFile = open("test.txt", "r", encoding="UTF-8")
outfile = open("outTest.txt", "w", encoding="UTF-8")

while True:
    strFile = inFile.readline()
    #strFile
    strFilechange = ""
    for ch in strFile:
        #암호화
        chNum = ord(ch)
        chNum = chNum + 100
        chChange = chr(chNum)
        #기록
        strFilechange += chChange   
    if(strFile == ""):  
        break
    outfile.writelines(strFilechange) 

inFile.close()
outfile.close()

inFile = open("test.txt", "r", encoding="UTF-8")
#복호화
while True:
    strFile = inFile.readline()
    #strFile
    strFilechange = ""
    for ch in strFile:
        #암호화
        chNum = ord(ch)
        chNum = chNum - 100
        chChange = chr(chNum)
        #기록
        strFilechange += chChange   
    if(strFile == ""):  
        break
    print(strFilechange, end="")

inFile.close()
outfile.close()

