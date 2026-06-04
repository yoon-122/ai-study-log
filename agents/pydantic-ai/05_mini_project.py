from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from dataclasses import dataclass

@dataclass
class AppDeps:
    spotify_api_key: str

class SongRecommendation(BaseModel):
    title: str
    artist: str
    genre: str
    reason: str

agent = Agent(
    "openai:gpt-4.1-mini",
    deps_type=AppDeps,
    output_type=SongRecommendation,
    system_prompt="너는 음악 추천 전문가야."
)

@agent.tool
def search_spotify(ctx: RunContext[AppDeps], keyword: str) -> str:
    api_key = ctx.deps.spotify_api_key
    # Spotify API 호출 로직
    return f"{keyword} 관련 음악 검색 결과"

result = agent.run_sync(
    "잔잔한 밤 산책용 노래 추천해줘",
    deps=AppDeps(spotify_api_key="your-key")
)
print(result.output.title)
print(result.output.artist)
print(result.output.reason)