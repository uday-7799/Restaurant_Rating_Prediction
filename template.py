import os 
import sys
from pathlib import Path
import logging

project_name = "RestaurantRatingPrediction"

lis_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    "notebooks/EDA.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "Dockerfile",
    "templates/index.html",
    "app.py",
    "setup.py"
]


for filepath in lis_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating the {filedir} directory for file name: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            logging.info(f"creating empty file: {filepath}")
            pass

    else:
        logging.info(f"{filename} already exists")