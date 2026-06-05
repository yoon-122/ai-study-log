import httpx
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from dataclasses import dataclass

@dataclass
class AppDeps:
    lastfm_api_key: str

class SongRecommendation(BaseModel):
    title: str
    artist: str
    reason: str

agent = Agent(
    "anthropic:claude-haiku-4-5-20251001",  # 클로드 나중에 결재해서 실행해보기
    deps_type=AppDeps,
    output_type=SongRecommendation,
    system_prompt="너는 음악 추천 전문가야. 검색 결과를 바탕으로 최적의 곡을 추천해줘."
)

@agent.tool
def search_music(ctx: RunContext[AppDeps], keyword: str) -> str:
    response = httpx.get(
        "https://ws.audioscrobbler.com/2.0/",
        params={
            "method": "track.search",
            "track": keyword,
            "api_key": ctx.deps.lastfm_api_key,
            "format": "json",
            "limit": 5
        }
    )
    tracks = response.json()["results"]["trackmatches"]["track"]
    return str([f"{t['name']} - {t['artist']}" for t in tracks])

result = agent.run_sync(
    "잔잔한 밤 산책용 노래 추천해줘",
    deps=AppDeps(lastfm_api_key="49244027847b93596c0f07fa1cfb5692")
)

print(f"제목: {result.output.title}")
print(f"아티스트: {result.output.artist}")
print(f"추천 이유: {result.output.reason}")