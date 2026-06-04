from pydantic import BaseModel
from pydantic_ai import Agent

# 1. BaseModel 기본
class User(BaseModel):
    name: str
    age: int

user = User(name="영수", age=27)
print(user)

# 2. Agent 기본
agent = Agent("openai:gpt-4.1-mini")
result = agent.run_sync("안녕")
print(result.output)

# 3. system_prompt
agent = Agent(
    "openai:gpt-4.1-mini",
    system_prompt="너는 친절한 파이썬 튜터다."
)
# 테스트: 파이썬이 뭐야? / 리액트가 뭐야? 답변 차이 확인하기