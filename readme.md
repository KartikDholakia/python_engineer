# SteelEye Python Engineer Assessment

- Have downloaded the XML file and parsed thorugh it to find the download link
- Created function to download any file from web
- Created function to extracted the .xml file(only) from zip
- Converted the contents of XML to CSV
- Created a function to upload file over AWS S3

---
## Installation

Clone the repository:

	git clone https://github.com/KartikDholakia/python_engineer

Move inside the directory:

	cd python_engineer

Install required libraries:

	pip install requirements.txt

Create an Account in AWS and update access keys in `constants.py`:

	AWS_BUCKET = 'name_of_S3_bucket'
	AWS_KEY = 'key_goes_here'

Run the main program:

	python main.py

---

## Project Files

`main.py` - Starting point of the project \
`utils.py` - All useful functions are defined here \
`constants.py` - All constants (like csv_headers, AWS Bucket Name, AWS Key) are defined here 

`DLTINS_20210117_01of01.csv` - File csv created after following all the mentioned steps \
`select.xml` - XML from where the download link was fetched (Step - 1). Was provided in the assignment iteself