from backend import db

class NonAllocatedPatients(db.Model):
    __tablename__ = "non_allocated_patients"
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey("answer.id"), primary_key=True)
    survives = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<NonAllocatedPatients patient_id={self.patient_id} answer_id={self.answer_id} survives={self.survives}>"

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "answer_id": self.answer_id,
            "survives": self.survives
        }