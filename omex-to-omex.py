import libcombine
import pyomexmeta as pyomm
from sys import argv
import os
#To extract rdf file from COMBINE archive
#argv[1] path to omex file
#argv[2] name of rdf output
#argv[3] output format
current_directory = dir_path = os.path.dirname(os.path.realpath("__file__"))
combine_archive_filename = os.path.join(current_directory, f"{argv[2]}.omex")
archive = libcombine.CombineArchive()
archive.initializeFromArchive(argv[1], skipOmex=True)

for i in range(archive.getNumEntries()):
    entry = archive.getEntry(i)
    print(" {0}: location: {1} format: {2}".format(i, entry.getLocation(), entry.getFormat()))
    # the entry could now be extracted and used as string
    if entry.getFormat() == 'http://identifiers.org/combine.specifications/omex-metadata':
        content = archive.extractEntryToString(entry.getLocation())
    if entry.getFormat() == 'http://identifiers.org/combine.specifications/sbml':
        model1 = archive.extractEntryToString(entry.getLocation())

print(content,file=open('rdf_1','w'))
rdf = pyomm.RDF.from_file('rdf_1',"rdfxml")
actual = rdf.to_string(argv[3]) #can use any format here
print(actual, file=open(argv[2], 'w'))
archive.addFileFromString(model1,f"{argv[2]}.sbml","sbml",True)
archive.addFileFromString(actual,f"{argv[2]}.rdf","rdfxml",False)
archive.writeToFile(combine_archive_filename)

