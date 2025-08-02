from autogen_agentchat.agents import AssistantAgent
from utils.model_loader import ModelLoader
from prompts.prompts import SYSTEM_PROMPTS

model_client = ModelLoader().load_llm()

diagnosis_synthesizer_agent = AssistantAgent(
    name="diagnosis_synthesizer_agent",
    description="You are a diagnosis synthesizer agent",
    model_client=model_client,
    system_message=SYSTEM_PROMPTS['dianosis_synthesizer_prompt']
)
