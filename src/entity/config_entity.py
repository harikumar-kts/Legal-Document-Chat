from dataclasses import dataclass


@dataclass(frozen=True)
class ElasticSearchConfig:
    """Elasticsearch related configurations"""
    user_id: str
    password: str
    hosts: list[str]
    certificate_path: str


@dataclass(frozen=True)
class LLMConfig:
    """LLM model server configurations"""
    top_p: float
    temperature: float
    api_key: str
    base_url: str
    model_name: str


@dataclass(frozen=True)
class EmbeddingConfig:
    """Embedding model configurations"""
    model_id: str
    dimension: int
