from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage
from autogen_agentchat.messages import TextMessage
import os
import asyncio

class ModelLoader:
    """
        A class to load llm model.
    """
    def __init__(self):
        load_dotenv()
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def load_llm(self):
        """
        Load and return the LLM model.
        """
        model_client = OpenAIChatCompletionClient(model="gpt-4.1-mini", api_key=self.openai_api_key)

        return model_client
    

if (__name__ == '__main__'):
    async def main():
        model_loader = ModelLoader()
        model_client = model_loader.load_llm()

        response = await model_client.create([UserMessage(content="What is the capital of France?", source="user")])
        print(response)

        output = await model_client.create([UserMessage(content="Who won the first IPL?", source="user")])
        print(output)
        
        await model_client.close()

    asyncio.run(main())
