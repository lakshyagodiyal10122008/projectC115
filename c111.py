import os
import shutil
print (dir(os))
#os.getcwd()
#os.mkdir("Code")
path=os.listdir()
#print(path)
path1=os.path.exists("C:/Users/pc/Contacts/Desktop/ABC")
print (path1)


source="C:/Users/pc/Contacts/Desktop/ABC/A.png"
destination="C:/Users/pc/Contacts/Desktop/CDE"
dest=shutil.move(source,destination)