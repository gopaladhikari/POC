from pydantic import BaseModel, computed_field
from typing import Dict


class StudentReportCard(BaseModel):
    student_name: str
    scores: Dict[str, float]

    @computed_field
    @property
    def average_score(self):
        total_score = sum(self.scores.values())
        return total_score / len(self.scores)
