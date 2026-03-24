from constant import CONFIG_FILE_PATH
from src.ds_project.components.data_ingestion import DataIngestion
from src.ds_project.config.configuration import AppConfiguration



class TrainingPipeline:

    def __init__(self):
        self.app_config = AppConfiguration(config_file_path=CONFIG_FILE_PATH)
        self.data_ingestion = DataIngestion(app_config=self.app_config)

    def start_data_ingestion(self):
        """
        Starts the training pipeline
        :return: none
        """
        self.data_ingestion.initiate_data_ingestion()