import uvicorn
import matplotlib
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from src.model.load import Models
from src.elsticsearch.elastic import ElasticSearch
from src.config.manager import ConfigurationManager


class InputSchema(BaseModel):
    user_query: str


class OutputSchema(BaseModel):
    status: int
    user_query: str
    response: str


app = FastAPI(
    title="LangGraph Server",
    version="1.0",
    description="Abu Dhabi Legal Document Knowledge base retrieval API Server"
)


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Initialization(metaclass=SingletonMeta):
    def __init__(self):
        self.config = ConfigurationManager()
        self.llm_config = self.config.get_llm_model_config()
        self.embedding_config = self.config.get_embedding_model_config()
        self.elasticsearch_config = self.config.get_elasticsearch_config()

        self.llm = self.initialize_llm_model()
        self.embedding = self.initialize_embedding_model()
    
    def initialize_llm_models(self):
        return Models.llm_model_connection(
            llm_config=self.llm_config
        )
    
    def initialize_embedding_models(self):
        return Models.embedding_model_connection(
            embedding_config=self.embedding_config
        )
    
    def initialize_elasticsearch(self):
        return ElasticSearch.client_initialization(
            elasticsearch_config=self.elasticsearch_config
        )
    
