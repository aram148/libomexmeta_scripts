import os
import site
import typing
import unittest
import libcombine
import requests
import zipfile
import pyomexmeta as pyomm
from sys import argv

#To extract rdf file from COMBINE archive
#argv[1] path to omex file
#argv[2] name of rdf output
#argv[3] output format

archive = libcombine.CombineArchive()
archive.initializeFromArchive(argv[1], skipOmex=True)
annotation_entries = [i.c_str() for i in archive.getAllLocations() if i[-4:] == ".rdf"]
rdf_extract = [archive.extractEntryToString(i) for i in annotation_entries]
rdf = pyomm.RDF.from_string(rdf_extract[0])
actual = rdf.to_string(argv[3]) #can use any format here
print(actual, file=open(argv[2], 'w'))