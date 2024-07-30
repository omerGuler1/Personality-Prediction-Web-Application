from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Dict


class UserInput(BaseModel):
    name: str
    surname: str

class PredictionInput(BaseModel):
    q1: int
    q2: int
    q3: int
    q4: int
    q5: int
    q6: int
    q7: int
    q8: int
    q9: int
    q10: int
    q11: int
    q12: int
    q13: int
    q14: int
    q15: int
    q16: int
    q17: int
    q18: int
    q19: int
    q20: int
    q21: int = None
    q22: int = None
    q23: int = None
    q24: int = None
    q25: int = None
    q26: int = None
    q27: int = None
    q28: int = None
    q29: int = None
    q30: int = None
    q31: int = None
    q32: int = None
    q33: int = None
    q34: int = None
    q35: int = None
    q36: int = None
    q37: int = None
    q38: int = None
    q39: int = None
    q40: int = None
    q41: int = None
    q42: int = None
    q43: int = None
    q44: int = None
    q45: int = None
    q46: int = None
    q47: int = None
    q48: int = None
    q49: int = None
    q50: int = None
    q51: int = None
    q52: int = None
    q53: int = None
    q54: int = None
    q55: int = None
    q56: int = None
    q57: int = None
    q58: int = None
    q59: int = None
    q60: int = None


class PredictRequest(BaseModel):
    input_data: Dict[str, int]
    user_input: UserInput



class PredictionDetailsBase(PredictionInput):
    id: int
    personality_type: str
    answers: Dict[str, int]

    class Config:
        orm_mode = True

class PredictionDetailsCreate(PredictionInput):
    personality_type: str

class PredictionDetailsResponse(BaseModel):
    predictions: List[PredictionDetailsBase]
    total: int



class FeedbackBase(BaseModel):
    feedback: str
    prediction: int

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class FeedbackResponse(BaseModel):
    feedbacks: List[Feedback]
    total: int

