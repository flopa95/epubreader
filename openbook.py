from ebooklib import epub
import ebooklib
import os
import html2text as htmltext

chapter_list = []
book_spine = []


def trunc_at(s, d, n=5):
    "Returns s truncated at the n'th (5th by default) occurrence of the delimiter, d."
    return d.join(s.split(d, n)[:n])


def read(book_url):
    book = epub.read_epub(book_url)

    for i in range (len(book.spine)):
        book_spine.append(book.spine[i][0])

    for j in range(len(book_spine)):
        chapter = book.get_item_with_id(book_spine[j])
        chapter_list.append(chapter.get_body_content())

    return trunc_at(chapter_list[10].decode("utf-8"),"</p")

def read2(book_url):
    book = epub.read_epub(book_url)

    for i in range (len(book.spine)):
        book_spine.append(book.spine[i][0])

    for j in range(len(book_spine)):
        chapter = book.get_item_with_id(book_spine[j])
        chapter_list.append(chapter.get_body_content())

    return trunc_at(chapter_list[11].decode("utf-8"),"</p",5)





### Retrieving all the HTML files of the book in correct order ###

