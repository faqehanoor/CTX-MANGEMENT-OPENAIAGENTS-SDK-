import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel

class UserInfo(BaseModel):
    user_id: int | str
    name: str

user = UserInfo(user_id=10690, name="❀ꗥ～ꗥ❀ 𝐅𝐀𝐐𝐄𝐇𝐀 𝐍𝐎𝐎𝐑 ❀ꗥ～ꗥ❀ (FN)")

def dynamic_ins(wrapper: RunContextWrapper[UserInfo], agent: Agent[UserInfo]) -> str:
    return "You right to call the tool 'get_user_info' to get user information."

@function_tool
def get_user_info(wrapper: RunContextWrapper[UserInfo]):
    return f"The user info is: Name = {wrapper.context.name}, ID = {wrapper.context.user_id}"

personal_agent = Agent(
    name="PersonalAgent",
    instructions=dynamic_ins,
    tools=[get_user_info],
)

async def main():
    result = await Runner.run(
        personal_agent,
        'What is my name and my user id?',
        run_config=config,
        context=user  
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
