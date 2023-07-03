from utils import *

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)

if __name__ == '__main__':
    download_url = fetch_download_link("select.xml", "DLTINS")
    print(download_url)
