#notes about __init__.py
    #It tells Python that the directory is a package.
    #It’s automatically executed when you import that package.
    #You can use it to initialize global variables, imports, or configurations (like logging).

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")

#Logs are just records of what your program does while it’s running.
#logs make debugging easier , it's a good practice <3