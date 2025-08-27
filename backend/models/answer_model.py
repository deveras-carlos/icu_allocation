from backend import db

class Answer(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True)
    simulation_id = db.Column(db.Integer, db.ForeignKey("simulation.id"), nullable=False)
    solver_id = db.Column(db.Integer, db.ForeignKey("solver.id"), nullable=False)

    def __repr__(self):
        return f"<Answer id={self.id} simulation_id={self.simulation_id} solver_id={self.solver_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "simulation_id": self.simulation_id,
            "solver_id": self.solver_id
        }