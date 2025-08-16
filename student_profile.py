import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel

class StudentProfile(BaseModel):
    student_id: int | str
    student_name: str
    current_quater: str
    total_courses: int


student = StudentProfile(
    student_id="10690", 
    student_name="Faqeha Noor (FN)",
    current_quater="Q4", 
    total_courses=7
)

def dynamic_ins(wrapper: RunContextWrapper[StudentProfile], agent: Agent[StudentProfile]) -> str:
    return "When prompted, call tool 'get_student_profile' to get student profile."

@function_tool
def get_student_profile(wrapper: RunContextWrapper[StudentProfile]):
    return f'The Student Profile: {wrapper.context}'

personal_agent = Agent[StudentProfile](
    name="Agent",
    instructions=dynamic_ins,
    tools=[get_student_profile]
)

async def main():
    result = await Runner.run(
        personal_agent,
        'Provide student profile containing student name, student id, current semester, and total courses', 
        run_config=config,
        context=student  
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())