from backend import db

class Parameter(db.Model):
    __tablename__ = "parameter"
    id = db.Column(db.Integer, primary_key=True)
    min_respiration = db.Column(db.Integer, default=0, nullable=False)
    max_respiration = db.Column(db.Integer, default=4, nullable=False)
    min_coagulation = db.Column(db.Integer, default=0, nullable=False)
    max_coagulation = db.Column(db.Integer, default=4, nullable=False)
    min_liver = db.Column(db.Integer, default=0, nullable=False)
    max_liver = db.Column(db.Integer, default=4, nullable=False)
    min_cardiovascular = db.Column(db.Integer, default=0, nullable=False)
    max_cardiovascular = db.Column(db.Integer, default=4, nullable=False)
    min_nervous = db.Column(db.Integer, default=0, nullable=False)
    max_nervous = db.Column(db.Integer, default=4, nullable=False)
    min_kidney = db.Column(db.Integer, default=0, nullable=False)
    max_kidney = db.Column(db.Integer, default=4, nullable=False)
    min_neonatal_age = db.Column(db.Integer, default=0, nullable=False)
    max_neonatal_age = db.Column(db.Integer, default=28, nullable=False)
    min_pediatric_age = db.Column(db.Integer, default=29, nullable=False)
    max_pediatric_age = db.Column(db.Integer, default=15 * 365 + 3, nullable=False)
    min_adult_age = db.Column(db.Integer, default=15 * 365 + 4, nullable=False)
    max_adult_age = db.Column(db.Integer, default=120 * 365, nullable=False)

    def __repr__(self):
        return f"<Parameter id={self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "min_respiration": self.min_respiration,
            "max_respiration": self.max_respiration,
            "min_coagulation": self.min_coagulation,
            "max_coagulation": self.max_coagulation,
            "min_liver": self.min_liver,
            "max_liver": self.max_liver,
            "min_cardiovascular": self.min_cardiovascular,
            "max_cardiovascular": self.max_cardiovascular,
            "min_nervous": self.min_nervous,
            "max_nervous": self.max_nervous,
            "min_kidney": self.min_kidney,
            "max_kidney": self.max_kidney,
            "min_neonatal_age": self.min_neonatal_age,
            "max_neonatal_age": self.max_neonatal_age,
            "min_pediatric_age": self.min_pediatric_age,
            "max_pediatric_age": self.max_pediatric_age,
            "min_adult_age": self.min_adult_age,
            "max_adult_age": self.max_adult_age
        }