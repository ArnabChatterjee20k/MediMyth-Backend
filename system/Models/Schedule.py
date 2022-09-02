from system import db
from system.Models.Doctor import Doctor
from datetime import datetime 
from datetime import timedelta
from sqlalchemy.dialects.mysql import TIME
def default_contact(context):
    # context sensitive default
    id = context.current_parameters.get("doctor_id")
    return Doctor.query.filter_by(id).first().phone_no

def default_slot_end(context):
    slot_start = context.current_parameters.get("slot_start")
    default_hours = 2
    slot_end = slot_start-default_hours
    return slot_end

class Schedule(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    doctor_id = db.Column(db.Integer,db.ForeignKey("doctor.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    phone_no = db.Column(db.String,default=default_contact)
    
    day = db.Column(db.Integer,nullable=False) # accepting weekday means if day is monday then 0, if tuesday then 1
    # using weekday we can get the date of the day from the calendar easily
    specific_week = db.Column(db.Integer) # 1,2,3,4 -> 4 weeks in a month. If null means every week
    
    slot_start = db.Column(TIME(),nullable=False)
    slot_end = db.Column(TIME())
    
    booking_start = db.Column(db.Integer,default=7)# 1,2,3,4,5,6,7,.....before.
    booking_end = db.Column(db.DateTime,default=default_slot_end)
    
    fees = db.Column(db.Integer)
    limit = db.Column(db.Integer)
    
    # we need to provide atleast one of clinic name and medical shop
    clinic_name = db.Column(db.String)
    medical_shop = db.Column(db.String)

    address = db.Column(db.String,nullable=False)