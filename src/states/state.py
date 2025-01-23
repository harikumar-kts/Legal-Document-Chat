from typing import List, Dict
from typing_extensions import TypedDict


class GraphResponseState(TypedDict):
    user_query: str
    embedding_vector: List[float]
    elasticsearch_keys: List[str]
    relevent_docs: Dict
