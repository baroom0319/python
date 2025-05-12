import tkinter

root = tkinter.Tk()

file = open("test.txt", "r", encoding="UTF-8")

strFile = file.readlines()
root.geometry(strFile[:-1])

fileList = file.readlines()
root.title(strFile.rstrip[:-1])

file.close()

root.mainloop()

'''
while True:
    str = file.readline()
    print(str, end ='') 
    if(str == ''):
        break

'''

'''
fileList = file.readlines()
index = 1
for strList in fileList :
    print(str(index) + " : " + strList, end= '')

file.close()
'''
