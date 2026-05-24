from kafka import KafkaConsumer
from src.utils import ConfigReaderUtils as conf
from constants import CommonConstants as constants

class OrderEventConsumer:

    def __init__(self):
        pass

    def consume(self, topic, partition, offset):
        consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', consumer_timeout_ms=1000, enable_auto_commit=True)
        consumer.subscribe([topic])

    def readConfig(self) -> dict:
        kafkaConfig = conf.read_config()
        topicConfig = conf.read_config(constants.STREAMING_CONFIG_FILE_PATH)
        combinedConfig = kafkaConfig.update(topicConfig)
        return combinedConfig