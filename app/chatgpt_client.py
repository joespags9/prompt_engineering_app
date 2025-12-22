from openai import OpenAI
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ChatGPTClient:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the ChatGPT client.

        Args:
            api_key: OpenAI API key. If not provided, will look for OPENAI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.")

        self.client = OpenAI(api_key=self.api_key)

    def chat_completion(
        self,
        prompt: str,
        model: str = "gpt-4o-mini",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Send a prompt to ChatGPT and get a response.

        Args:
            prompt: The user's prompt/message
            model: The model to use (default: gpt-4o-mini)
            temperature: Controls randomness (0-2, default: 0.7)
            max_tokens: Maximum tokens in response (optional)

        Returns:
            The AI's response as a string
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )

            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"Error calling ChatGPT API: {str(e)}")

    def chat_completion_stream(
        self,
        prompt: str,
        model: str = "gpt-4o-mini",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ):
        """
        Send a prompt to ChatGPT and get a streaming response.

        Args:
            prompt: The user's prompt/message
            model: The model to use (default: gpt-4o-mini)
            temperature: Controls randomness (0-2, default: 0.7)
            max_tokens: Maximum tokens in response (optional)

        Yields:
            Chunks of the AI's response as they arrive
        """
        try:
            stream = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True
            )

            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content

        except Exception as e:
            raise Exception(f"Error calling ChatGPT API: {str(e)}")

    def chat_with_context(
        self,
        messages: list[dict],
        model: str = "gpt-4o-mini",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Send a conversation with context to ChatGPT.

        Args:
            messages: List of message dicts with 'role' and 'content' keys
                     Example: [{"role": "user", "content": "Hello"}]
            model: The model to use (default: gpt-4o-mini)
            temperature: Controls randomness (0-2, default: 0.7)
            max_tokens: Maximum tokens in response (optional)

        Returns:
            The AI's response as a string
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )

            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"Error calling ChatGPT API: {str(e)}")
