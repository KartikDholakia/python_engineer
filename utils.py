import os
import wget
import logging
from urllib import request
import xml.etree.ElementTree as ET
import zipfile


def download_file(file_url: str, path: str):
    """
    Function to download file from the given url. 
    The downloaded file is placed in "path". If the file
    is already present at that path, it will not download 
    it again.
    :param file_url: Web URL of the file to be downloaded
    :param path: Location where you want to download the file
    :return:
		(string): Name of the file downloaded
    """

	# Extract filename from the given Web URL: 
    file_name = os.path.basename(file_url)
    logging.info('Filename extracted from URL: ' + file_name)
    
    # Check if the file is already present in 'path':
    if os.path.exists(os.path.join(path, file_name)):
        logging.debug(file_name + ' is already downloaded!')
        return file_name
    else:
        # Try downloading the file:
        try:
            response = request.urlretrieve(file_url, os.path.join(path, file_name))
            logging.info("File downloaded in path" + path)
            return file_name
        except Exception as error:
            logging.error("Error in downloading" + str(error))
            return ""



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



def extract_from_zip(zip_path, file_type):
    """
    Extracts the file of 'file_type' from the given zip file. 
    Extracting file conditionally.
    :param zip_path: Path of ZIP file
    :param file_type: Extension of file which we want to extract
    :return:
       (string): Path of extracted file 
    """
    try:
        # Try opening the given ZIP file:
        with zipfile.ZipFile(zip_path, 'r') as zip:

            # Fetch the list of items in the archive:
            files = zip.namelist()

            # Traverse through each of them to find the required file:
            for file in files:
                # Extract file name and extension:
                file_name, file_extension = os.path.splitext(file)

                # If this file meets our condition:
                if file_extension == file_type:

                    # Check if this file is already present in root directory:
                    if os.path.exists(os.path.join(os.getcwd(), file)):
                        logging.debug("File was already extracted!")
                        return os.path.join(os.getcwd(), file)
                    
                    else:
                        logging.info("Found the file in ZIP archive. Now extracting it...")
                        return zip.extract(file)
                
    except zipfile.BadZipfile as error:
        logging.error("Failed to extract from ZIP file. Error: " + str(error))

    except zipfile.LargeZipFile as error:
        logging.error("Error - Large ZIP file. " + str(error))

    except Exception as error:
        logging.error("Failed to extract from ZIP file. Error: " + str(error))

    # If unable to extract file, return empty string:
    return "" 
