import os
import sys
import logging

logging_string = "[%(asctime)s - %(levelname)s - %(module)s - %(lineno)s - %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format = logging_string,
    handlers=[
    logging.FileHandler(log_filepath , mode='w'),
    logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("EnergyPredLogger")