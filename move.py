import os
import shutil

source="C:/Users/Admin/Desktop/Newfolder"
destination="C:/Users/Admin/Python Programming/Class 102 Project"
listofItems=os.listdir(source)
print(listofItems)

for fname in listofItems:
    name,ext=os.path.splitext(fname)
    print(name,ext)

    if ext == '':
        continue
    if ext in [".txt", ".doc", ".docx",".pdf"]:

        path1 = source + '/' + fname                      
        path2 = destination + '/' + "Document_Files"                     
        path3 = destination + '/' + "Document_Files" + '/' + fname   
        
        if os.path.exists(path2):
          print("Moving " + fname + ".....")

          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + fname + ".....")
          shutil.move(path1, path3)

