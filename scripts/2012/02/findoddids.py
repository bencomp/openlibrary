import json
import fileinput
import csv
import sys


if sys.argv[len(sys.argv)-1] != sys.argv[0]:
	writer = csv.writer(open(sys.argv[len(sys.argv)-1], 'wb'))
	writer.writerow(["record","identifier","value"])
else:
	sys.exit("No filename supplied!")

oddids = ["1sbn", 
	"ISBN13",  
	"isbn13", 
	"isbn",
	"epub_isbn",
	"ean",
	"library_of_congress_catalogue_number",
	"library_of_congress_catalog_no.", 
	"library_of_congress_catalog_card_no.", 
	"library_of_congress_catalog_card_number", 
	"library_of_congress_classification_(lcc)",
	"lccn_permalink:",
	"amazon.co.jp", 
	"amazon_asin#",
	"asin:", 
	"amazon.ca_asin", 
	"amazon.de_asin",
	"amazon.co.uk_asin",
	"web_link/_internet_url", 
	"call_number", 
	"dewey_decimal_classification", 
	"dewey_number",
	"universal_decimal_classification",
	"deutsche_nationalbibliothek_(urn:nbn)",
	"bibliothèque_nationale_de_france_(bnf)",
	"open_library",
	"uri",
	"oclc",
	"test123",
	"sold_by",
	"publisher",
	"id",
	"pdf_version"]

# Open standard input
f = fileinput.input('-')
for line in f:
	decoded = json.loads(line)
	if "identifiers" in decoded:
		for k in decoded["identifiers"].keys():
			if k.encode('utf-8') in oddids:
				for v in decoded["identifiers"][k]:
					writer.writerow([decoded["key"].encode('utf-8'), k.encode('utf-8'), v.encode('utf-8')])

