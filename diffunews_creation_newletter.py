#!/usr/bin/python3

import sys
import os
import glob

from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

inputs = glob.glob("./Exemples/*.pdf")
inputs.sort()
print(inputs)


assert inputs
outfn = './Exemples/newletter.pdf'

writer = PdfWriter()
i = 1


for inpfn in inputs:
    inpfn2 = inpfn
    writer.addpages(PdfReader(inpfn2).pages)

writer.trailer.Info = IndirectPdfDict(
    Title='Liste Nouveautés',
    Author='',
    Subject='newletter bibliothèque',
    Creator='',
)
writer.write(outfn)
