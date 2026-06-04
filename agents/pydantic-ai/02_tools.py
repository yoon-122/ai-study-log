from pydantic_ai import Agent, RunContext
from dataclasses import dataclass

agent = Agent("openai:gpt-4.1-mini")

# tool_plain: 단순 계산, deps 불필요
@agent.tool_plain
def add(a: int, b: int) -> int:
    return a + b

@agent.tool_plain
def multiply(a: int, b: int) -> int:
    return a * b

@agent.tool_plain
def divide(a: float, b: float) -> float:
    return a / b

# 테스트: LLM이 적절한 tool 선택하는지 확인
# result = agent.run_sync("15 + 30 계산해줘")
# result = agent.run_sync("20 곱하기 30은?")
# result = agent.run_sync("100 나누기 4는?")