from ebooklib import epub
import ebooklib
import os
import html2text as htmltext

chapter = []

def read(book_url):
    book = epub.read_epub(book_url)

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapter.append(item.get_body_content())

    #banana = chapter[7].decode("utf-8")
    #print (chapter)
    return htmltext.html2text(chapter[1].decode("utf-8"))




    '''
for z in range(len(x)):
    decoded = x[z].decode('utf8')
    f = open(newpath +'/Chapter ' + str(z+1)+'.html','w',encoding='utf-8')
    f.write(decoded)
    f.close()

    '''