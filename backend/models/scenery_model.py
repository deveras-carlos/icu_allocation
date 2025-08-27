from backend import db

class Scenery(db.Model):
    __tablename__ = "scenery"
    scenary_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    parameter_id = db.Column(db.Integer, db.ForeignKey("parameter.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Scenery scenary_id={self.scenary_id} name={self.name}>"

    def to_dict(self):
        return {
            "scenary_id": self.scenary_id,
            "user_id": self.user_id,
            "parameter_id": self.parameter_id,
            "name": self.name
        }