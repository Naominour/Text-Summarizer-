import urllib.request as request
import zipfile
from textsummarizer.loggin import logger
from textsummarizer.utils.common import get_size
from textsummarizer.entity import DataIngestionConfig
from pathlib import Path
import os


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config



    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url, 
                filename = self.config.local_data_file
            )
            logger.info(f" {filename} download! with following info:\n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file)  )}")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts zip file to the data directory
        Function returns None

        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

try:
    config = Configurationmanager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()

except Exception as e:
    raise e