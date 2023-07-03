from utils import *

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)

if __name__ == '__main__':
    # Step - 1: Fetch the download link from XML:
    download_url = fetch_download_link("select.xml", "DLTINS")
    
	# Step - 2: Download from the link fetchedn from above
    zip_file = download_file(download_url, os.getcwd())
    if len(zip_file):
        logging.info(zip_file + " downloaded!")
    else:
        logging.error("Couldn't download the ZIP file")
        exit(-1)
        

    # Step - 3: Extract XML file from the above ZIP file:
    xml_downloaded = extract_from_zip(zip_file, '.xml')	

    if len(xml_downloaded):
        logging.info("XML Extracted to location: " + str(xml_downloaded))
    else:
        logging.error("Couldn't extract XML file. Aborting...")
        exit(-1)

    
    # Step - 4: Convert the XML to CSV
    csv_path = xml_to_csv(xml_downloaded, os.getcwd())
    if len(csv_path):
        logging.info("CSV File created: " + str(csv_path))
    else:
        logging.error("Coudln't convert XML to CSV!!")
        exit(-1)

    
    # Step - 5: Upload to AWS S3 Bucket
    if upload_to_s3(csv_path, constants.AWS_BUCKET, constants.AWS_KEY):
        logging.info("File Uploaded to S3 successfully!!")
    else:
        logging.error("Couldn't upload to S3!!")
