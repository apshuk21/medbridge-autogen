from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.agents import UserProxyAgent
from agents.symptom_analyzer_agent import symptom_analyzer_agent
from autogen_agentchat.conditions import TextMentionTermination

termination_condition = TextMentionTermination('APPROVE')

user_proxy_agent = UserProxyAgent(
    'symptom_analyzer_user_proxy_agent',
    input_func=input
)

med_core_symptom_team = RoundRobinGroupChat(
    [symptom_analyzer_agent, user_proxy_agent],
    termination_condition=termination_condition,
    max_turns=5
)