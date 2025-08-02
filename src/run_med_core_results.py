import asyncio
from autogen_agentchat.ui import Console
from teams.med_core_results_team import med_core_results_team

async def main():
    results = asyncio.create_task(Console(med_core_results_team.run_stream(task="I'm having mild pain in the right part of my stomach.")))
    await results

if (__name__ == '__main__'):
    asyncio.run(main())