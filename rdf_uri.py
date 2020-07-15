import pyomexmeta as pyomm
import libcombine
from sys import argv


#To extract rdf from a uri
#argv[1] uri as string
#argv[2] name of rdf output
#argv[3] output format

rdfstring = pyomm.RDF.from_uri(argv[1],"rdfxml")
actual = rdfstring.to_string(argv[3])
print(actual, file=open(argv[2], 'w'))
