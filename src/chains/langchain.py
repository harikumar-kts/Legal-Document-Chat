from typing import Union, Dict, List

from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt
from src.config.pydantic_base_class import MultiQuerySchema


class LangChainFunctions:

    @staticmethod
    def multi_query_generation(
            model: ChatGroq,
            user_question: str
    ) -> Union[MultiQuerySchema, Dict]:
        """
        Agent will generate the multiple query from the user's query

        :param model: ChatGroq LLM Model
        :param user_question: user's input question
        :return: Multi Query object
        """
        multi_query_prompt_template = load_prompt("prompt/multi_query_prompt.yaml")
        structured_llm = model.with_structured_output(
            MultiQuerySchema,
            method="json_mode"
        )
        multi_query_generation = multi_query_prompt_template | structured_llm
        return multi_query_generation.invoke(
            {
                "user_query": user_question
            }
        )

    @staticmethod
    def elasticsearch_keyword_generation(model: ChatGroq, questions: List[str]):
        """
        Generate the keywords for Elastic search Lexical search
        :param model: ChatGroq LLM Model
        :param questions: Multi queries generated from users query
        :return: Search keywords
        """
        search_key_prompt_template = load_prompt("prompt/search_key_prompt.yaml")
        elastic_search_key_generation = search_key_prompt_template | model
        return elastic_search_key_generation.invoke(
            {
                "questions": questions
            }
        )



