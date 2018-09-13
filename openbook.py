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

    return chapter[5].decode("utf-8")

def read2(book_url):
    book = epub.read_epub(book_url)

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapter.append(item.get_body_content())

    return chapter[6].decode("utf-8")


