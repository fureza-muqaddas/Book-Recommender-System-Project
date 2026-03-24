import os
from pathlib import Path
import logging 


logging.basicConfig(level=logging.INFO)
project_name= "ds_project"

list_of_files=[

    #".github/workflows/.gitkeep",  
    f"src/{project_name}/__init__.py",  
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",  
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeliness/__init__.py",
    f"src/{project_name}/pipeliness/training_pipeline.py",
    f"src/{project_name}/pipeliness/predictions_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "config/config.yaml",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "main.py"
]


for file in list_of_files:
    file_path=Path(file)
    file_dir,file_name=os.path.split(file_path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")
    
    if (not os.path.exists(file_path) or os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
