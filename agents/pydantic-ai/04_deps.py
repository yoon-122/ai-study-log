from pydantic_ai import Agent, RunContext
from dataclasses import dataclass

@dataclass
class AppDeps:
    user_name: str
    api_key: str

agent = Agent(
    "openai:gpt-4.1-mini",
    deps_type=AppDeps  # deps 타입 명시 필수
)

@agent.tool  # deps 접근할 땐 tool_plain 아니고 tool로
def get_weather(ctx: RunContext[AppDeps], city: str) -> str:
    api_key = ctx.deps.api_key  # deps에서 꺼내기
    # 실제 API 호출 로직
    return f"{city} 날씨 정보"

result = agent.run_sync(
    "오늘 수원 날씨 알려줘",
    deps=AppDeps(user_name="윤훈", api_key="your-key")
)
print(result.output)