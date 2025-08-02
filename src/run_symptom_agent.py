from agents.symptom_analyzer_agent import symptom_analyzer_agent
from autogen_agentchat.ui import Console
import asyncio

async def main():
    agent_response = asyncio.create_task(Console(symptom_analyzer_agent.run_stream(task="I'm getting red patches on my face.")))
    await agent_response

asyncio.run(main())