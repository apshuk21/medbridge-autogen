from autogen_agentchat.agents import AssistantAgent
from utils.model_loader import ModelLoader
from prompts.prompts import SYSTEM_PROMPTS

model_client = ModelLoader().load_llm()

symptom_analyzer_agent = AssistantAgent(
    name="symptom_analyzer_agent",
    description="You are a symptom analyzer agent",
    model_client=model_client,
    system_message=SYSTEM_PROMPTS['symptom_analyzer_prompt']
)
