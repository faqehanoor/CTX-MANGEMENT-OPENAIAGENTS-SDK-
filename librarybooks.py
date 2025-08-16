import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel

class LibraryBook(BaseModel):
    book_id: str
    book_title: str
    author_name: str
    is_available: bool


library_book = LibraryBook(
    book_id="1088",
    book_title="JavaScript Mastery",
    author_name="John Dalton",
    is_available=True
)
def dynamic_ins(wrapper: RunContextWrapper[LibraryBook], agent: Agent[LibraryBook]) -> str:
    return "When prompted, call tool 'get_library_book_details' to get Library Book Details."

@function_tool
def get_library_book_details(wrapper: RunContextWrapper[LibraryBook]):
    return f'Library Book Details: {wrapper.context}'

library_book_agent = Agent[LibraryBook](
    name="Library Book Agent",
    instructions=dynamic_ins,
    tools=[get_library_book_details]
)

async def main():
    result = await Runner.run(
        library_book_agent,
        'Give Library Book Details:', 
        run_config=config,
        context=library_book  
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())