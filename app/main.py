from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
from .database import SessionLocal, engine
from .schemas import Feedback, PredictionInput, FeedbackCreate, FeedbackResponse, PredictRequest
import joblib
import pandas as pd

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


personality_types = {
    0: "ESTJ",
    1: "ENTJ",
    2: "ESFJ",
    3: "ENFJ",
    4: "ISTJ",
    5: "ISFJ",
    6: "INTJ",
    7: "INFJ",
    8: "ESTP",
    9: "ESFP",
    10: "ENTP",
    11: "ENFP",
    12: "ISTP",
    13: "ISFP",
    14: "INTP",
    15: "INFP"
}


# Load the trained models and scalers
model_60 = joblib.load('data/knn_model.pkl')
scaler_60 = joblib.load('data/scaler.pkl')
feature_names_60 = joblib.load('data/feature_names.pkl')

# Load for 20 questions
model_20 = joblib.load('data/knn_model2.pkl')
scaler_20 = joblib.load('data/scaler2.pkl')
feature_names_20 = joblib.load('data/feature_names2.pkl')




# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/predict")
async def predict(request: PredictRequest, db: Session = Depends(get_db)):
    try:

        input_data = request.input_data
        user_input = request.user_input

        num_questions = len(input_data)
        if num_questions == 60:
            model = model_60
            scaler = scaler_60
            feature_names = feature_names_60
        elif num_questions == 20:
            model = model_20
            scaler = scaler_20
            feature_names = feature_names_20


        # input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Ensure the DataFrame has the correct column names
        input_df = input_df.reindex(columns=feature_names, fill_value=0)
        
        # Normalize the data
        input_data_normalized = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_data_normalized)
        
        # prediction to personality type
        personality_type = int(prediction[0])



        personality_type_str = personality_types.get(personality_type, "Unknown Personality Type (default)")
        new_prediction = models.Prediction(name=user_input.name, 
                                           surname=user_input.surname, 
                                           personality_type=personality_type_str
        )

        db.add(new_prediction)
        db.commit()
        db.refresh(new_prediction)
        response_id = new_prediction.id


        new_prediction_details = models.PredictionDetails(
            id=new_prediction.id,
            personality_type=personality_type_str,
            **input_data
        )
        db.add(new_prediction_details)
        db.commit()
        db.refresh(new_prediction_details)

        return {"name": user_input.name, "surname": user_input.surname, "response_id": response_id, "predicted_personality": personality_type}
    
    except Exception as e:
        return {"error": str(e), "predicted_personality": None}





@app.post("/feedback", response_model=schemas.Feedback)
async def submit_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = crud.create_feedback(db=db, feedback=feedback)
    return db_feedback

@app.get("/feedbacks", response_model=FeedbackResponse)
async def read_feedbacks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    feedbacks = crud.get_feedbacks(db, skip=skip, limit=limit)
    total = db.query(models.Feedback).count()
    return FeedbackResponse(feedbacks=feedbacks, total=total)

@app.get("/feedback/{feedback_id}", response_model=schemas.Feedback)
async def read_feedback(feedback_id: int, db: Session = Depends(get_db)):
    db_feedback = crud.get_feedback(db, feedback_id=feedback_id)
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return db_feedback

@app.put("/feedback/{feedback_id}", response_model=schemas.Feedback)
async def update_feedback(feedback_id: int, feedback: FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = crud.update_feedback(db, feedback_id=feedback_id, feedback_update=feedback)
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return db_feedback

@app.delete("/feedback/{feedback_id}", response_model=schemas.Feedback)
async def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    db_feedback = crud.delete_feedback(db, feedback_id=feedback_id)
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return db_feedback