from elasticsearch import Elasticsearch
from src.entity.config_entity import ElasticSearchConfig

class ElasticSearch:

    @staticmethod
    def client_initialization(elasti_config: ElasticSearchConfig):
        return Elasticsearch(
            hosts=elasti_config.hosts,
            basic_auth=(elasti_config.user_id, elasti_config.password)
        )
    