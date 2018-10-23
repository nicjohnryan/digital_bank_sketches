# -*- coding: utf-8 -*-

#=========================
# Jaro winkler in Python
#=========================

from pyjarowinkler import distance
from matplotlib import pyplot as plt

ref = 'Wages ABC Pty Ltd SEP'
words = ['Wages ABC Pty Ltd JUN', 'Wages ABC Pty Ltd JUL', 'Wages ABC Pty Ltd AUG',
           'UBER Some Random Town 56437', 'Ice Cream Shop random digits 23456', 'Ice Cream Shop random digits 23456']

ref = ref.lower()

scores = []

for w in words:
    w = w.lower()
    score = distance.get_jaro_distance(ref, w)
    scores.append(score)

plt.hist(scores)    


#=========================
# Scrape PDFs in Python
#=========================

import PyPDF2
import re

pdfFileObj = open('tempPublicReport_sthkgzi7ad.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(1)

page = pageObj.extractText()

legalName = re.search(r'Legal name(.*?)ABN', page).group(1)
ANZSIC = re.search(r'ANZSIC(.*?)\/', page).group(1)

print("Legal Name: {} , ANZSIC Code: {}".format(legalName, ANZSIC))