from backend import db

class Solver(db.Model):
    __tablename__ = "solver"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Solver id={self.id} name={self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }