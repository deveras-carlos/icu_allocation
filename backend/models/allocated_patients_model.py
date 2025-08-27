from backend import db

class AllocatedPatients(db.Model):
    __tablename__ = "allocated_patients"
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey("answer.id"), primary_key=True)
    intensive_care_unit_id = db.Column(db.Integer, db.ForeignKey("intensive_care_unit.id"), nullable=False)
    survives = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<AllocatedPatients patient_id={self.patient_id} answer_id={self.answer_id} survives={self.survives}>"

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "answer_id": self.answer_id,
            "intensive_care_unit_id": self.intensive_care_unit_id,
            "survives": self.survives
        }