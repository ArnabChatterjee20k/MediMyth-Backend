from system import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
class Appointment(db.Model):
    # this is for patients who will book to a schedule
    id = db.Column(db.Integer,primary_key = True)
    appointment_id = db.Column(db.String)
    schedule_id = db.Column(db.Integer,db.ForeignKey("schedule.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    name = db.Column(db.String(30),nullable=False)
    contact_number = db.Column(db.String(10),nullable=False)##contact number of the patient
    age = db.Column(db.Integer,nullable=False)
    date = db.Column(db.DateTime,default = datetime.utcnow)

    @hybrid_property
    def appointment_id(self):
        return f"MMA-{self.id}"

