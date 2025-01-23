from src.constants import RUNTIME_CONFIG_FILE_PATH
from src.utils.helper_functions import read_yaml_file
from src.entity.config_entity import ElasticSearchConfig, LLMConfig, EmbeddingConfig


class ConfigurationManager:
    def __init__(self, params_file_path=RUNTIME_CONFIG_FILE_PATH) -> None:
        self.config = read_yaml_file(params_file_path)

    def get_elasticsearch_config(self) -> ElasticSearchConfig:
        return ElasticSearchConfig(
            user_id=self.config.ElasticSearch.user_id,
            password=self.self.config.ElasticSearch.password,
            hosts=self.self.config.ElasticSearch.hosts,
            certificate_path=self.self.config.ElasticSearch.certificate_path,
        )

    def get_llm_model_config(self) -> LLMConfig:
        return LLMConfig(
            top_p=self.self.config.LLM.top_p,
            temperature=self.self.config.LLM.temperature,
            base_url=self.self.config.LLM.base_url,
            model_name=self.self.config.LLM.model_name,
        )
    
    def get_embedding_model_config(self) -> EmbeddingConfig:
        return EmbeddingConfig(
            model_id=self.config.Embedding.model_id,
            dimension=self.config.Embedding.dimension,
        )
