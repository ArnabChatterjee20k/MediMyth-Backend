from system import db
from sqlalchemy.orm import column_property
from datetime import datetime
class Appointment(db.Model):
    # this is for patients who will book to a schedule
    id = db.Column(db.Integer,primary_key = True)
    appointment_id = column_property(f"MM{id}")
    schedule_id = db.Column(db.Integer,db.ForeignKey("schedule.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    name = db.Column(db.String(30),nullable=False)
    contact_number = db.Column(db.String(10),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    date = db.Column(db.DateTime,default = datetime.utcnow)

