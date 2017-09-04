import os
import requests
import re
import traceback
import sys
import logging
import argparse

#adding custom imput command line arguments
parser = argparse.ArgumentParser(description='check for existence of gene1 and gene2 \
	in a pubmed paper, with id=pmid')
parser.add_argument('-g1', '--gene1', dest="gene1", default="ALDH2" , type=str, nargs='+',
                   help='gene1 as a string', metavar='g1')
parser.add_argument('-g2', '--gene2', dest="gene2", default="PPARD", type=str, nargs='+',
                   help='gene2 as a string', metavar='g2')
parser.add_argument('-p','--pmid', dest="pmid", default=11811951, type=int, nargs='+',
                   help='PMID, pubmed id as an integer') #todo , will this fit in an int, eg 11811951 ?

args = parser.parse_args()

#constructing the pubtator api endpoint to be called
PUBTATOR_ENDPOINT_URL = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/Gene/"
final_api_string = PUBTATOR_ENDPOINT_URL + str(args.pmid) + "/BioC"

#call the pubtator api endpoint
pubtator_response = requests.get(final_api_string)

#print url for sanity
print(pubtator_response.url)

#print raw response and json
try:
	print("The response from pubtator gene api is :", pubtator_response, pubtator_response.json())
except ValueError as ve:
	logging.exception("Something awful happened!")
	logger.error('json decoding failed, ValueError', exc_info=True)
	print(traceback.format_exception(None, # <- type(e) by docs, but ignored 
                                     ve, ve.__traceback__),
          file=sys.stderr, flush=True)
	print("json decoding failed : ", ve.p)
	traceback.print_exc()
	desired_trace = traceback.format_exc(sys.exc_info())
    #log(desired_trace)

#print response text
print(pubtator_response.text)

#remove this, after test, beore commit #todo
print(pubtator_response.encoding)

#print response content
print(pubtator_response.content)

#save requests's response(xml/json) to a file

#before saving pubtator api call response to file, print pwd
print("\n pwd = " + os.getcwd())

#filename = "path/to/desired/location/for/saving/response"
api_response_file_path = os.getcwd() + "/" + str(args.pmid) + "_bioc.xml"

with open(api_response_file_path, mode='wb') as localfile:     
	localfile.write(pubtator_response.content)

#search for gene2, gene2 in the api response(which is requests's response)

#can we use simple string method find()
prsc =  str(pubtator_response.content)

#g1e = gene1 existence in (paper with) given pmid
g1e = prsc.find(gene1)
g2e = prsc.find(gene2)

if g1e != -1:
	print("gene1: " + args.gene1 + " EXISTS in paper with pubmedid: " + str(args.pmid))
	#consider having 2 output parameters ? #todo
	#return(True) 
else:
	print("gene1: " + args.gene1 + " DOES NOT EXIST in paper with pubmedid: " + str(args.pmid))


if g2e != -1:
	print("gene2: " + args.gene2 + " EXISTS in paper with pubmedid: " + str(args.pmid))
	#consider having 2 output parameters ? #todo
	#return(True) 
else:
	print("gene2: " + args.gene2 + " DOES NOT EXIST in paper with pubmedid: " + str(args.pmid))

"""
g1_present = re.search(args.gene1, pubtator_response.text)
g2_present = re.search(args.gene2, pubtator_response.text)

print(g1_present.group(0))
print(g2_present.group(0))
#find all occurences of gene1 and gene2
re.findall(args.gene1, pubtator_response.text)
re.findall(args.gene2, pubtator_response.text)
"""


