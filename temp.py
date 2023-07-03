# from urllib import request
# URL = "https://instagram.com/favicon.ico"
# response = request.urlretrieve("https://instagram.com/favicon.ico", "instagram.ico")

# """
# 	# Step - 1: Download the XML file
# 	# URL = https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100

# 	XML_URL = 'https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100'
# 	XML_PATH = 'xml_file.xml'
# 	# Dowmload the file in current directory:
# 	download_file(XML_URL, os.getcwd())
# """

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import pandas as pd

def xml_to_csv():
    mytree = ET.parse('DLTINS_20210117_01of01.xml')
    myroot = mytree.getroot()
    
    for child in myroot.findall('FinInstrmGnlAttrbts')[:2]:
        print(child.tag, child.attrib)
    
    # print(ET.tostring(myroot, encoding='utf8').decode('utf8'))



    id = []
    fullNm = []
    # for x in myroot.findall('FinInstrmGnlAttrbts'):
    #     print(x)
    #     break

    # print(myroot)
    # print([elem.tag for elem in myroot.iter()][:5])

    # for element in myroot:
    #     for sub_element in element:
    #         for sub_sub in sub_element:
    #             print(sub_sub.tag, sub_sub.attrib)
    #             for key, value in sub_sub.attrib:
    #                 print(key, value)
            # print(sub_element.tag, sub_element.attrib)


def try_with_bs4():
    with open('DLTINS_20210117_01of01.xml', 'r', encoding='utf-8') as file:
        xml_data = file.read()
        
    soup = BeautifulSoup(xml_data, 'xml')
	
    # FinInstrmGnlAttrbts = soup.find_all('FinInstrmGnlAttrbts')
    # for values in FinInstrmGnlAttrbts[:2]:
    #     print (values.Id.text)
    #     print (values.FullNm.text)
        
    FinInstrm = soup.find_all('FinInstrm')
    for values in FinInstrm[:2]:
        if values.TermntdRcrd.FinInstrmGnlAttrbts.Id.text:
            print (values.TermntdRcrd.FinInstrmGnlAttrbts.Id.text) 
        if values.TermntdRcrd.FinInstrmGnlAttrbts.FullNm.text:
	        print (values.ermntdRcrd.FinInstrmGnlAttrbts.FullNm.text)


def try_with_pandas():
    xml_data = open('DLTINS_20210117_01of01.xml', 'r', encoding='utf-8').read()
    root = ET.XML(xml_data)
    data = []
    cols = []
    for i, child in enumerate(root):
        data.append([subchild.tag for subchild in child])
        cols.append(child.tag)
        
    df = pd.DataFrame(data).T  # Write in DF and transpose it
    df.columns = cols  # Update column names
    print(df)
    
import pandas_read_xml as pdx
def pandas2():
    df = pdx.read_xml('DLTINS_20210117_01of01.xml')
    print(df)


# pandas2()
# try_with_pandas()
try_with_bs4()
# xml_to_csv()