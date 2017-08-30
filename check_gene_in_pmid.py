import requests
import re


PUBTATOR_ENDPOINT = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/Gene/"


final_api_string = PUBTATOR_ENDPOINT + pmid + "/BioC"

#call the pubtator api endpoint
pubtator_response = requests.get(final_api_string)

#print url for sanity
print(pubtator_response.url)

#print raw response and json
print(pubtator_response, pubtator_response.json())

#print response text
print(pubtator_response.text)

#remove this, after test, beore commit
print(pubtator_response.encoding)

#print response content
print(pubtator_response.content)
