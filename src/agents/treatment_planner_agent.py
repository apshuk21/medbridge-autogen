from autogen_agentchat.agents import AssistantAgent
from utils.model_loader import ModelLoader
from prompts.prompts import SYSTEM_PROMPTS

model_client = ModelLoader().load_llm()

treatment_planner_agent = AssistantAgent(
    name="treatment_planner_agent",
    description="You are a treatment planner agent",
    model_client=model_client,
    system_message=SYSTEM_PROMPTS['treatment_planner_prompt']
)
