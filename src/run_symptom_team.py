import asyncio
from autogen_agentchat.ui import Console
from teams.med_core_symptom_team import med_core_symptom_team

async def main():
    team_response = asyncio.create_task(Console(med_core_symptom_team.run_stream(task="I'm getting red patches on my face.")))
    await team_response

asyncio.run(main())