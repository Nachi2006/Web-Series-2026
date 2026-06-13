from sqlalchemy.orm import Session
import models, schemas

def participantByEmail(db: Session, email: str):
    return db.query(models.Participant).filter(models.Participant.email == email).first()

def participantById(db: Session, id: int):
    return db.query(models.Participant).filter(models.Participant.id == id).first()

def participants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Participant).offset(skip).limit(limit).all()

def createParticipant(db: Session, participant: schemas.participantCreate):
    db_participant = models.Participant(
        name=participant.name,
        email=participant.email,
        role=participant.role
    )
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

def deleteParticipant(db: Session, id: int):
    db_participant = participantById(db, id)
    if db_participant:
        db.delete(db_participant)
        db.commit()
        return True
    return False