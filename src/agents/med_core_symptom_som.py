from autogen_agentchat.agents import SocietyOfMindAgent
from teams.med_core_symptom_team import med_core_symptom_team
from utils.model_loader import ModelLoader

model_client = ModelLoader().load_llm()

med_core_symptom_som = SocietyOfMindAgent(
    'med_core_symptom_som',
    team=med_core_symptom_team,
    model_client=model_client
)