from system import db
from system.Models.Doctor import Doctor
from datetime import datetime 
from datetime import timedelta
from sqlalchemy.dialects.postgresql import TIME
def default_contact(context):
    # context sensitive default
    id = context.current_parameters.get("active_doctor_id")##since we will be dealing active doctor
    return Doctor.query.filter_by(id=id).first().phone_no

class Schedule(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    active_doctor_id = db.Column(db.Integer,db.ForeignKey("active_doctor.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    phone_no = db.Column(db.String,default=default_contact)
    
    day = db.Column(db.Integer,nullable=False) # accepting weekday means if day is monday then 0, if tuesday then 1
    # using weekday we can get the date of the day from the calendar easily
    specific_week = db.Column(db.Integer) # 1,2,3,4 -> 4 weeks in a month. If null means every week
    
    slot_start = db.Column(TIME(),nullable=False)
    slot_end = db.Column(TIME())
    
    booking_start = db.Column(db.Integer,default=7)# 1,2,3,4,5,6,7,.....before.
    booking_end = db.Column(db.Integer,default=2) # 2hours before before the slot_start
    
    fees = db.Column(db.Integer)
    limit = db.Column(db.Integer)
    
    # we need to provide atleast one of clinic name and medical shop
    clinic_name = db.Column(db.String)
    medical_shop = db.Column(db.String)

    address = db.Column(db.String,nullable=False)

    # appointments
    appointment_data = db.relationship("Appointment",backref="appointment_data")


    def data_exists(self)->bool:
        search_params = {}

        for col_name in self.__table__.columns.keys():
            data = getattr(self,col_name,None)
            if(data):
                search_params[col_name] = data
        
        return bool(Schedule.query.filter_by(**search_params).first())
    

    @classmethod
    def update_schedule(cls,email,schedule_id):
        doctor = Doctor.query.filter_by(email=email).first_or_404()
        doctor_id = doctor.active_id.first().id
        current_schedule_query = Schedule.query.filter_by(id=schedule_id,active_doctor_id=doctor_id)
        current_schedule = current_schedule_query.first_or_404()
        return current_schedule_query
    
    @classmethod
    def check_and_update(cls,id,email,**data):
        schedule = cls.update_schedule(email=email,schedule_id=id)
        schedule.update(data)
        db.session.commit()