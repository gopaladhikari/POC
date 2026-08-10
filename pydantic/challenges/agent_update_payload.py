from pydantic import BaseModel, Field, ConfigDict
from typing import Literal


class AgentUpdatePayload(BaseModel):

    agent_name: str = Field(..., min_length=3, max_length=30)

    llm_model: Literal["gpt-3.5-turbo", "gpt-4", "claude-3"]

    temperature: float = Field(..., ge=0.0, le=2.0)

    tags: set[str] = Field(..., max_length=5)

    model_config = ConfigDict(extra="forbid")


payload = {
    "agent_name": "John Doe",
    "llm_model": "gpt-3.5-turbo",
    "temperature": 0.5,
    "tags": ["tag1", "tag2"],
}


validated_payload = AgentUpdatePayload.model_validate(payload)
