import logging
import os
from datetime import datetime

LOG_PATH = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
file_path = os.path.join(os.getcwd(), "logs", LOG_PATH)
os.makedirs(file_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(file_path, LOG_PATH)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info('Logging has started here!')