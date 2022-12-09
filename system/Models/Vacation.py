from system import db 
from system.Models.ScheduleVacation import schedule_vacation
from system.Models.Schedule import Schedule
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

    @classmethod
    def create_vacation(cls,active_doctor_id,**kwargs):
        start = kwargs.get("start")
        end = kwargs.get("end")
        reason = kwargs.get("reason")
        schedules_ids= kwargs.get("schedules_ids")
        
        vacation = Vacation(active_doctor_id=active_doctor_id,start=start,end=end,reason=reason)
        schedules = vacation.schedules

        # adding schedules in the the vacation
        schedule_objects = Schedule.get_schedules_by_ids(schedules_ids)
        for schedule in schedule_objects:
            schedules.append(schedule)

        db.session.add(vacation)
        db.session.commit()
    
    @classmethod
    def vacation_exist(cls,active_doctor_id=active_doctor_id,**kwargs):
        start = kwargs.get("start")
        end = kwargs.get("end")
        return Vacation.query.filter(Vacation.active_doctor_id==active_doctor_id,Vacation.start==start,Vacation.end==end).first()