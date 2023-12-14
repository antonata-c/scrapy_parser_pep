import csv
from collections import defaultdict
from datetime import datetime

from .constants import (BASE_DIR, ITEM_STATUS_FIELD, RESULTS_DIR,
                        STATUS_INCREMENT, SUMMARY_DATETIME_FORMAT,
                        SUMMARY_FIELDNAMES, SUMMARY_OPEN_FORMAT,
                        SUMMARY_TOTAL_NAME)

FILENAME_FORMAT = 'status_summary_{}.csv'


class PepParsePipeline:
    def open_spider(self, spider):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)
        self.status_amount = defaultdict(int)

    def process_item(self, item, spider):
        self.status_amount[item.get(ITEM_STATUS_FIELD)] += STATUS_INCREMENT
        return item

    def close_spider(self, spider):
        now_formatted = datetime.now().strftime(SUMMARY_DATETIME_FORMAT)
        filepath = self.results_dir / FILENAME_FORMAT.format(now_formatted)
        self.status_amount[SUMMARY_TOTAL_NAME] = sum(
            self.status_amount.values()
        )
        with open(filepath, SUMMARY_OPEN_FORMAT) as csvfile:
            csv.writer(
                csvfile, dialect=csv.unix_dialect
            ).writerows(
                [SUMMARY_FIELDNAMES, *self.status_amount.items()]
            )
