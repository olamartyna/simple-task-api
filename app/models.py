from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(50), default='pending')

    def __repr__(self):
        return f'<Task {self.id} - {self.title}>'