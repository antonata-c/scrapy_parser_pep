from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

ITEM_STATUS_FIELD = 'status'
SUMMARY_TOTAL_NAME = 'Total'
SUMMARY_FIELDNAMES = ('Статус', 'Количество')

SUMMARY_DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
SUMMARY_OPEN_FORMAT = 'w'
OUT_FILE_FORMAT = 'csv'

STATUS_INCREMENT = 1
