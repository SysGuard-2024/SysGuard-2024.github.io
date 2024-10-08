from elasticsearch import Elasticsearch
import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
    logger = logging.getLogger('SysGuardLog')
    logger.setLevel(logging.INFO)
    # Need to modify es configuration by yourself
    es_host = 'localhost'
    es_port = 9200
    es_index = 'logs'
    es_handler = ElasticsearchHandler(
        es_hosts=[{'host': es_host, 'port': es_port}],
        index=es_index
    )
    logger.addHandler(es_handler)

    # Optional: create a file handler for local log file recording
    file_handler = RotatingFileHandler('application.log', maxBytes=5 * 1024 * 1024, backupCount=2)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


class ElasticsearchHandler(logging.Handler):
    def __init__(self, es_hosts, index_name):
        self.es = Elasticsearch(es_hosts)
        self.index_name = index_name

    def log(self, logLevel, errorInfo, device_location, device_name, device_type, device_value):
        timestamp = datetime.now().isoformat()

        log_entry = {
            "timestamp": timestamp,
            "logLevel": logLevel,
            "errorInfo": errorInfo,
            "device_location": device_location,
            "device_name": device_name,
            "device_type": device_type,
            "device_value": device_value,
            "message": f"{device_location}.{device_name}.state: {device_value}",
            "source": source
        }

        log_json = json.dumps(log_entry)

        self.es.index(index=self.index_name, body=log_json)


logger = setup_logging()