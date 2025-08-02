from autogen_agentchat.teams import RoundRobinGroupChat
from agents.med_core_symptom_som import med_core_symptom_som
from agents.med_core_diagnosis_som import med_core_diagnosis_som
from agents.treatment_planner_agent import treatment_planner_agent
from autogen_agentchat.conditions import TextMentionTermination

termination_condition = TextMentionTermination('TREATMENT_PLAN_APPROVED')

med_core_results_team = RoundRobinGroupChat(
    [med_core_symptom_som, med_core_diagnosis_som, treatment_planner_agent],
    termination_condition=termination_condition,
    max_turns=3
)