from backend import db

class ICUBeds(db.Model):
    __tablename__ = "icu_beds"
    parameter_id = db.Column(db.Integer, db.ForeignKey("parameter.id"), primary_key=True)
    intensive_care_unit_id = db.Column(db.Integer, db.ForeignKey("intensive_care_unit.id"), primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<ICUBeds parameter_id={self.parameter_id} intensive_care_unit_id={self.intensive_care_unit_id} amount={self.amount}>"

    def to_dict(self):
        return {
            "parameter_id": self.parameter_id,
            "intensive_care_unit_id": self.intensive_care_unit_id,
            "amount": self.amount
        }