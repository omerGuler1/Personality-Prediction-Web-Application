from sqlalchemy.orm import Session
from . import models, schemas 

def get_feedback(db: Session, feedback_id: int):
    return db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Feedback).offset(skip).limit(limit).all()

def create_feedback(db: Session, feedback: schemas.FeedbackCreate):
    db_feedback = models.Feedback(feedback=feedback.feedback, prediction=feedback.prediction)
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def delete_feedback(db: Session, feedback_id: int):
    db_feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    if db_feedback:
        db.delete(db_feedback)
        db.commit()
        return db_feedback
    return None

def update_feedback(db: Session, feedback_id: int, feedback_update: schemas.FeedbackBase):
    db_feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    if db_feedback:
        for key, value in feedback_update.dict().items():
            setattr(db_feedback, key, value)
        db.commit()
        db.refresh(db_feedback)
        return db_feedback
    return None
