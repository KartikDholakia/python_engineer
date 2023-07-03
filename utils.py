import os
import wget
import logging
from urllib import request
import xml.etree.ElementTree as ET


def download_file(file_url: str, path: str):
    """
    Function to download file from the given url. 
    The downloaded file is placed in "path". If the file
    is already present at that path, it will not download 
    it again.
    :param file_url: Web URL of the file to be downloaded
    :param path: Location where you want to download the file
    :return:
		(bool): Success. If the function was able to download the
        file then true otherwise false.
    """

	# Extract filename from the given Web URL: 
    file_name = os.path.basename(file_url)[:5]
    logging.info('Filename: ' + file_name)
    
    # Check if the file is already present in 'path':
    if os.path.exists(os.path.join(path, file_name)):
        logging.debug(file_name + ' is already downloaded!')
        return True
    else:
        try:
            response = request.urlretrieve(file_url, os.path.join(path, file_name))
            # response = wget.download(file_url, path)
            logging.info("File downloaded in path" + path)
        except Exception as error:
            logging.error("Error in downloading" + str(error))



def fetch_download_link(xml_file, file_type):
    """
    Given the XML file and file_type, fecth the first 
    download link from XML file with file type as
    "file_type".
    :param xml_file: Path to XML file
    :param file_type: File Type of the resource to be downloaded
    :return:
		(string): Download Link
    """
    logging.info("Parsing XML File: " + xml_file)
    mytree = ET.parse('select.xml')
    myroot = mytree.getroot()
    
    # Traverse through child elements of root:
    logging.info("Traversing through child elements of XML")
    for element in myroot[1]:
        for sub_element in element:
            # print(sub_element.tag, sub_element.attrib, sub_element.text)
            if sub_element.attrib['name'] == 'file_type' and sub_element.text == file_type:
                found = True
                break
        if found:
            download_url = element[1].text
            break
    if found:
        logging.info("Found the download URL: " + download_url)
        return download_url
    else:
        logging.error("Unable to parse XML and find the download URL")
        exit(-1)



