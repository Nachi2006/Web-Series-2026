from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List

import models,schemas,crud
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)
app=FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/participants/",response_model=schemas.participantResponse,status_code=201)
def create_participant(participant:schemas.participantCreate,db:Session=Depends(get_db)):
    db_user=crud.participantByEmail(db,email=participant.email)
    if db_user:
        raise HTTPException(status_code=400,detail="Participant is already registered")
    return crud.createParticipant(db=db,participant=participant)

@app.get("/")
def output():
    return "Hello World"
@app.get("/participants/",response_model=List[schemas.participantResponse])
def read_participants(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return crud.participants(db=db,skip=skip,limit=limit)

@app.get("/participants/{participant_id}",response_model=schemas.participantResponse)
def participant_by_id(participant_id:int,db:Session=Depends(get_db)):
    db_user=crud.participantById(db=db,id=participant_id)
    if db_user is None:
       raise HTTPException(status_code=404,detail="Participant does not Exist")
    return db_user

@app.delete("/participants/{participant_id}", status_code=204)
def delete_participant(participant_id: int, db: Session = Depends(get_db)):
    success = crud.deleteParticipant(db, id=participant_id)
    if not success:
        raise HTTPException(status_code=404, detail="Participant not found")
    return None
     
    
    