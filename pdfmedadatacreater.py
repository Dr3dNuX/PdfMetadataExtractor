# -*- coding: cp1252 -*-
search_one = input("enter some terms>> ")
search = search_one.split()

from pdfminer.high_level import extract_text
 
text = extract_text("learnc.pdf").lower()
 
test = text.split()

for item in search:
    print(item in test, item)



