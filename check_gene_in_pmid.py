import requests
import re
import traceback
import sys
import logging

PUBTATOR_ENDPOINT_URL = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/Gene/"


final_api_string = PUBTATOR_ENDPOINT_URL + pmid + "/BioC"

#call the pubtator api endpoint
pubtator_response = requests.get(final_api_string)

#print url for sanity
print(pubtator_response.url)

#print raw response and json
try:
	print(pubtator_response, pubtator_response.json())
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

#remove this, after test, beore commit
print(pubtator_response.encoding)

#print response content
print(pubtator_response.content)
