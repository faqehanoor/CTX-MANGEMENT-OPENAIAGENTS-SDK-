import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel

class BankAccount(BaseModel):
    account_number: str
    customer_name: str
    account_balance: float
    account_type: str


bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Fatima Khan",
    account_balance=75500.50,
    account_type="savings"
)

def dynamic_ins(wrapper: RunContextWrapper[BankAccount], agent: Agent[BankAccount]) -> str:
    return "When prompted, call tool 'customer_bank_account_details' to get customer bank account details."

@function_tool
def customer_bank_account_details(wrapper: RunContextWrapper[BankAccount]):
    return f'Customer Bank Account Details is : {wrapper.context}'

customer_bankaccount_agent = Agent[BankAccount](
    name="Customer Bank Account Agent",
    instructions=dynamic_ins,
    tools=[customer_bank_account_details]
)

async def main():
    result = await Runner.run(
        customer_bankaccount_agent,
        'Give Customer Bank Account Details:', 
        run_config=config,
        context=bank_account  
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())