from system import db
from system.Models.ScheduleVacation import schedule_vacation
from sqlalchemy.dialects.postgresql import DATE

class Vacation(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    start = db.Column(DATE(),nullable=False)
    end = db.Column(DATE(),nullable=False)
    reason = db.Column(db.Text,nullable=True)
    # will help to identify which which day the doctor has taken vacation
    active_doctor_id = db.Column(db.Integer,db.ForeignKey("active_doctor.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)

    # we can access the schedules through Vacation object using schedules attribute while we can access the vacations of a schedule by schedule obj using backref vacation
    schedules = db.relationship("Schedule",backref="vacation",secondary=schedule_vacation,lazy="dynamic",cascade='all,delete',passive_deletes=True)