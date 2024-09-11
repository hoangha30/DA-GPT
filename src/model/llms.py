from langchain_openai import ChatOpenAI
import google.generativeai as genai
import os


def load_llm(model_name):
    """Load LLMs Model

    Args:
        model_name (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if model_name == "gpt-3.5-turbo":
        return ChatOpenAI(
            model=model_name,
            temperature=0.0,
            max_tokens=1000
        )
    elif model_name == "gemini-1.5-flash":
        return genai.GenerativeModel(
            model_name            
        )
    else:
        raise ValueError(
            "Unknown Model.\
                Please choose from ['gpt-3.5-turbo','gemini-1.5-flash']"
        )