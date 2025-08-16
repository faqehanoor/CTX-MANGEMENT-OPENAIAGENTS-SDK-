import asyncio
from pydantic import BaseModel
from agents import (
    Agent,
    Runner,
    trace,
    function_tool,
    RunContextWrapper
)
from connection import config  

# Define the user information model
class User_Info(BaseModel):
    name: str
    age: int
    alive: bool
    roll_num: str

# Instantiate user info
my_info = User_Info(name="Ali", age=23, alive=True, roll_num="q110110")

# Instructions for the agent
def dynamic_ins(wrapper: RunContextWrapper[User_Info], agent: Agent) -> str:
    #wrapper.context.name = 'Muhammad'
    return "Whenever prompted, you should use the 'user_information' tool to get User_Info."

# Tool to extract user info
@function_tool
def user_information(wrapper: RunContextWrapper[User_Info]) -> str:
    return (
        f"The user's roll number is: {wrapper.context.roll_num}, "
        f"and his name is: {wrapper.context.name}. "
        f"His age is: {wrapper.context.age}, and alive status: {wrapper.context.alive}."
    )
# Define the agent
agent = Agent[User_Info](
    name="Triage Agent",
    instructions=dynamic_ins,
    model=config.model, 
    tools=[user_information]
)
# Execution logic
async def main():
    with trace("context-userinfo"):
        prompt = "What is roll number and name of the user and age ,alive status of user?"
        result = await Runner.run(
            agent,
            input=prompt,
            context=my_info
        )
        print(result.final_output)
# Run the logic
if __name__ == "__main__":
    asyncio.run(main())