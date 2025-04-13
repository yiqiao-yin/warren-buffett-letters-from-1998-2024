from together import Together
from typing import List, Dict, Optional


class ChatBot:
    """
    A simple ChatBot class to interact with a Together LLM model.

    Attributes:
        api_key (str): The API key used to authenticate with the Together API.
        client (Together): A Together client for making requests.
        history (list[dict]): A list of dictionaries representing the conversation history.
    """

    def __init__(self, api_key: str) -> None:
        """
        Initializes the ChatBot with a given API key and an empty conversation history.
        Also creates a Together client instance for making requests.

        Args:
            api_key (str): The API key for Together.
        """
        self.api_key: str = api_key
        self.client: Together = Together(api_key=self.api_key)
        self.history: list[dict] = []

    def append_history(self, role: str, content: str) -> None:
        """
        Appends a new message entry to the conversation history.

        Args:
            role (str): The role of the message sender, e.g., "user" or "assistant".
            content (str): The message content to be appended.
        """
        self.history.append({"role": role, "content": content})

    def invoke_api(
        self,
        model: str = "deepseek-ai/DeepSeek-V3",
        max_tokens: int = 1024,
        temperature: float = 0.7,
        top_p: float = 0.7,
        top_k: int = 50,
        repetition_penalty: float = 1.0,
        stop: list[str] = ["<｜end▁of▁sentence｜>"]
    ) -> str:
        """
        Invokes the Together chat API using the stored conversation history.

        Args:
            model (str, optional): The name of the Together model to use. Defaults to "deepseek-ai/DeepSeek-V3".
            max_tokens (int, optional): The maximum number of tokens in the response. Defaults to 1024.
            temperature (float, optional): The sampling temperature. Defaults to 0.7.
            top_p (float, optional): The top_p sampling parameter. Defaults to 0.7.
            top_k (int, optional): The top_k sampling parameter. Defaults to 50.
            repetition_penalty (float, optional): The repetition penalty parameter. Defaults to 1.0.
            stop (list[str], optional): A list of stop tokens. Defaults to ["<｜end▁of▁sentence｜>"].

        Returns:
            str: The collapsed string response from the API.
        """
        response = self.client.chat.completions.create(
            model=model,
            messages=self.history,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            stop=stop,
            stream=True
        )
        answer: str = self.collapse_response(response)
        return answer

    def collapse_response(self, response) -> str:
        """
        Collapses a streaming response from the Together API into a single string.

        Args:
            response: The streaming response object from the Together API.

        Returns:
            str: A single string containing the concatenated content from each token in the response.
        """
        answer: str = ""
        for token in response:
            if hasattr(token, "choices"):
                try:
                    answer += token.choices[0].delta.content
                except:
                    pass
        return answer

    def show_history(self) -> None:
        """
        Prints the entire conversation history.
        """
        print(self.history)
