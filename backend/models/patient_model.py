from backend import db

class Patient(db.Model):
    __tablename__ = "patient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    need_respiratory_support = db.Column(db.Boolean, nullable=False)
    need_vasopressor_therapy = db.Column(db.Boolean, nullable=False)
    survival_chance_in_bed = db.Column(db.Float, nullable=False)
    survival_chance_outside_bed = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Patient id={self.id} name={self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "need_respiratory_support": self.need_respiratory_support,
            "need_vasopressor_therapy": self.need_vasopressor_therapy,
            "survival_chance_in_bed": self.survival_chance_in_bed,
            "survival_chance_outside_bed": self.survival_chance_outside_bed
        }