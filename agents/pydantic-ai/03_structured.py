from pydantic import BaseModel
from pydantic_ai import Agent

class SongRecommendation(BaseModel):
    title: str
    artist: str
    reason: str

agent = Agent(
    "openai:gpt-4.1-mini",
    output_type=SongRecommendation
)

result = agent.run_sync("잔잔한 밤 산책용 노래 추천해줘")
print(result.output.title)
print(result.output.artist)
print(result.output.reason)