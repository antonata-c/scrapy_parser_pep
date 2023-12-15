import csv
from collections import defaultdict
from datetime import datetime

from .settings import (BASE_DIR, ITEM_STATUS_FIELD, RESULTS_DIR,
                       SUMMARY_DATETIME_FORMAT, SUMMARY_FIELDNAMES,
                       SUMMARY_OPEN_FORMAT, SUMMARY_TOTAL_NAME)

FILENAME_FORMAT = 'status_summary_{}.csv'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_amount = defaultdict(int)

    def process_item(self, item, spider):
        self.status_amount[item.get(ITEM_STATUS_FIELD)] += 1
        return item

    def close_spider(self, spider):
        now_formatted = datetime.now().strftime(SUMMARY_DATETIME_FORMAT)
        filepath = self.results_dir / FILENAME_FORMAT.format(now_formatted)
        with open(filepath, SUMMARY_OPEN_FORMAT) as csvfile:
            csv.writer(
                csvfile,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows(
                [
                    SUMMARY_FIELDNAMES,
                    *self.status_amount.items(),
                    (SUMMARY_TOTAL_NAME, sum(self.status_amount.values()))
                ]
            )
