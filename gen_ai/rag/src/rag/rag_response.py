from pydantic import BaseModel, Field


class RAGResponse(BaseModel):
    reasoning: str = Field(
        description="Step-by-step logical deduction based strictly on the provided context."
    )
    final_answer: str = Field(
        description="The concise, final answer to the user's query."
    )
