from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from utils.model_loader import ModelLoader
from prompts.prompts import SYSTEM_PROMPTS
# import asyncio

model_client = ModelLoader().load_llm()

symptom_analyzer_agent = AssistantAgent(
    name="symptom_analyzer_agent",
    description="You are a symptom analyzer agent",
    model_client=model_client,
    system_message=SYSTEM_PROMPTS['symptom_analyzer_prompt']
)

# if (__name__ == '__main__'):
#     async def main():
#         agent_response = asyncio.create_task(Console(symptom_analyzer_agent.run_stream(task="I'm getting red patches on my face.")))
#         await agent_response

#     asyncio.run(main())
