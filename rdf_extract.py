import pyomexmeta as pyomm
import libcombine
from sys import argv


#To extract rdf from cellml or sbml file
#argv[1] path to file
#argv[2] name of rdf output
#argv[3] output format

rdfstring = pyomm.RDF.from_file(argv[1],"rdfxml")
actual = rdfstring.to_string(argv[3])
print(actual, file=open(argv[2], 'w'))
