from backend import db

class Simulation(db.Model):
    __tablename__ = "simulation"
    id = db.Column(db.Integer, primary_key=True)
    scenery_id = db.Column(db.Integer, db.ForeignKey("scenery.scenary_id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, nullable=False)
    modification_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Simulation id={self.id} title={self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "scenery_id": self.scenery_id,
            "title": self.title,
            "description": self.description,
            "creation_date": self.creation_date,
            "modification_date": self.modification_date
        }