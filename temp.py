from urllib import request
URL = "https://instagram.com/favicon.ico"
response = request.urlretrieve("https://instagram.com/favicon.ico", "instagram.ico")

"""
	# Step - 1: Download the XML file
	# URL = https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100

	XML_URL = 'https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100'
	XML_PATH = 'xml_file.xml'
	# Dowmload the file in current directory:
	download_file(XML_URL, os.getcwd())
"""