from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.agents import UserProxyAgent
from agents.diagnosis_synthesizer_agent import diagnosis_synthesizer_agent
from autogen_agentchat.conditions import TextMentionTermination

termination_condition = TextMentionTermination('APPROVE')

user_proxy_agent = UserProxyAgent(
    'diagnosis_synthesizer_user_proxy_agent',
    input_func=input
)

med_core_diagnosis_team = RoundRobinGroupChat(
    [diagnosis_synthesizer_agent, user_proxy_agent],
    termination_condition=termination_condition,
    max_turns=5
)