from pydantic import BaseModel
from pydantic_ai import Agent

# 에이전트 1: 음악 검색 전담
search_agent = Agent(
    "anthropic:claude-haiku-4-5-20251001",
    system_prompt="너는 음악 검색 전문가야. 키워드로 어울리는 음악 장르와 아티스트를 찾아줘."
)

# 에이전트 2: 추천 전담
class Recommendation(BaseModel):
    title: str
    artist: str
    reason: str

recommend_agent = Agent(
    "anthropic:claude-haiku-4-5-20251001",
    output_type=Recommendation,
    system_prompt="너는 음악 추천 전문가야. 검색 결과를 바탕으로 최적의 곡을 추천해줘."
)

# 메인 에이전트: 두 에이전트 조율
main_agent = Agent(
    "anthropic:claude-haiku-4-5-20251001",
    system_prompt="너는 음악 추천 서비스 매니저야."
)

@main_agent.tool_plain
def search_music(keyword: str) -> str:
    # 검색 에이전트 호출
    result = search_agent.run_sync(keyword)
    return result.output

@main_agent.tool_plain
def recommend_music(search_result: str) -> str:
    # 추천 에이전트 호출
    result = recommend_agent.run_sync(search_result)
    return f"{result.output.title} - {result.output.artist}: {result.output.reason}"

result = main_agent.run_sync("잔잔한 밤 산책용 노래 추천해줘")
print(result.output)