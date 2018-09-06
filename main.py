import ebooklib
from ebooklib import epub
import webbrowser
import os

ebookname = "Crazy Rich Asians.epub"
book = epub.read_epub(ebookname)

x=[]
old_spine=[]

### De-coding the book spine ###
xyz = book.spine
book_spine = []

for i in range (len(xyz)):
    book_spine.append(xyz[i][0])

### Retrieving all the HTML files of the book in correct order ###
for j in range(len(book_spine)):
    banana = book.get_item_with_id(book_spine[j])
    x.append(banana.get_body_content())

### Creating the directory for the HTML files to be stored in ###
newpath = "C:/Users/Florian Parzhuber/Desktop/epubreader" + "/" + ebookname[:-5]
if not os.path.exists(newpath):
    os.makedirs(newpath)

### Decoding and saving the HTML files in the newly created directory ###
for z in range(len(x)):
    decoded = x[z].decode('utf8')
    f = open(newpath +'/Chapter ' + str(z+1)+'.html','w',encoding='utf-8')
    f.write(decoded)
    f.close()

### Creating the directory for the image files to be stored in ###
image_folder_path = "C:/Users/Florian Parzhuber/Desktop/epubreader" + "/" + ebookname[:-5] + "/"
if not os.path.exists(image_folder_path):
    os.makedirs(image_folder_path)

### Retrieving all the image files and storing it in the correct directory ###


for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_IMAGE:
        print('==================================')
        print('NAME : ', item.get_name())
        
        filename = str(item.get_name())
        directoryname = filename.rsplit("/",1)
        filename2 = filename.rsplit("/",0)
        print(directoryname)

        if not os.path.exists(image_folder_path + directoryname[0]):
            os.makedirs(image_folder_path + directoryname[0])

        f = open(image_folder_path + directoryname[0] + filename2[0],'wb')
        f.write(item.get_content())
        f.close()
        #print('----------------------------------')
        #print(item.get_content())
        #print('==================================')

#print(images.get_content())


### Opening a chapter ###
#webbrowser.open_new_tab("helloworld.html")


