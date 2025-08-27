from backend import db

class IntensiveCareUnit(db.Model):
    __tablename__ = "intensive_care_unit"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<IntensiveCareUnit id={self.id} name={self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }