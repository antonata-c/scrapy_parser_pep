from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

ITEM_STATUS_FIELD = 'status'
SUMMARY_TOTAL_NAME = 'Total'
SUMMARY_FIELDNAMES = ('Status', 'Quantity')

SUMMARY_DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
SUMMARY_OPEN_FORMAT = 'w'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE, ]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status']
    },
}
