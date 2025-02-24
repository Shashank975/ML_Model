import os 
import sys 
import logging
from pathlib import Path


SOURCE_DIR = "src"


file_list = [
    f"{SOURCE_DIR}/__init__.py",
    f"{SOURCE_DIR}/components/__init__.py",
    f"{SOURCE_DIR}/config/__init__.py",
    f"{SOURCE_DIR}/constant/__init__.py",
    f"{SOURCE_DIR}/entity/__init__.py",
    f"{SOURCE_DIR}/exception/__init__.py",
    f"{SOURCE_DIR}/logger/__init__.py",
    f"{SOURCE_DIR}/pipeline/__init__.py",
    f"{SOURCE_DIR}/utils/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py",
    "requirements.txt"
]


for filepth in file_list:
    filepath = Path(filepth)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

        logging.info(f"Created directory {filedir}")
   
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath , "w") as f :
            pass
    else:
        logging.warning(f"File {filepath} already exists.")


        #$ conda activate C:\Users\LENOVO\Desktop\Modular_Programming\ML_Model\modular