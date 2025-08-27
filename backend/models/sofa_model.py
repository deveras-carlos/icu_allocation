from backend import db

class SOFA(db.Model):
    __tablename__ = "sofa"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    respiration = db.Column(db.Integer, nullable=False)
    coagulation = db.Column(db.Integer, nullable=False)
    liver = db.Column(db.Integer, nullable=False)
    cardiovascular = db.Column(db.Integer, nullable=False)
    nervous = db.Column(db.Integer, nullable=False)
    kidney = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<SOFA id={self.id} patient_id={self.patient_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "respiration": self.respiration,
            "coagulation": self.coagulation,
            "liver": self.liver,
            "cardiovascular": self.cardiovascular,
            "nervous": self.nervous,
            "kidney": self.kidney
        }