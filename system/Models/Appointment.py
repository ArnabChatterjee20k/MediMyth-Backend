from enum import unique
from system import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime , date, timedelta
from sqlalchemy.dialects.postgresql import DATE
import calendar
from system.Models.Schedule import Schedule
from system.utils.get_next_date import get_next_date
from system.utils.convert_str_to_date import convert_str_to_date
class Appointment(db.Model):
    # this is for patients who will book to a schedule
    id = db.Column(db.Integer,primary_key = True)
    appointment_id = db.Column(db.String)
    schedule_id = db.Column(db.Integer,db.ForeignKey("schedule.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    appointment_id = db.Column(db.String,unique=True)
    person_id = db.Column(db.Integer)
    name = db.Column(db.String(30),nullable=False)
    contact_number = db.Column(db.String(10),nullable=False)##contact number of the patient
    age = db.Column(db.Integer,nullable=False)
    appointment_date = db.Column(DATE(),nullable=False)
    date = db.Column(db.DateTime,default = datetime.utcnow)

    # @hybrid_property
    # def appointment_id(self):
    #     return f"MMA-{self.id}"


    @classmethod
    def check_booking(cls,id,appointment_date):
        schedule = Schedule.query.filter_by(id=id).first()
        print(schedule)
        if not schedule:
            print(schedule)
            return False
        specific_week = schedule.specific_week
        if specific_week:
            return cls.check_booking_start_specific_week(schedule,specific_week) and cls.check_booking_end_specific_week(schedule,specific_week) and cls.check_limit(schedule,appointment_date)
        return cls.check_booking_start(schedule) and cls.check_booking_end(schedule) and cls.check_limit(schedule,appointment_date)
    
    @classmethod
    def check_booking_start_specific_week(cls,schedule,specific_week):
        weekday = schedule.day
        today = date.today()
        all_weeks = calendar.monthcalendar(today.year,today.month)
        required_week = all_weeks[specific_week]
        required_date = required_week[weekday]

        parsed_required_date = datetime(today.year,today.month,required_date) # proper datetime parsed object

        booking_start_day = schedule.booking_start
        today = datetime.strptime(date.today().strftime(r"%y-%m-%d"),r"%y-%m-%d")

        delta = parsed_required_date - today
        return delta.days <= booking_start_day

    @classmethod
    def check_booking_end_specific_week(cls,schedule,specific_week):
        slot_start = schedule.slot_end
        weekday = schedule.day
        today = date.today()
        all_weeks = calendar.monthcalendar(today.year,today.month)
        required_week = all_weeks[specific_week]
        required_date = required_week[weekday]
        parsed_required_date = datetime(today.year,today.month,required_date) # proper datetime parsed object
        # parsed_required_date = datetime.strftime(parsed_required_date,r"%y-%m-%d")
        # parsed_required_date = datetime

        # combining with time
        parsed_required_date_time = datetime.combine(parsed_required_date,slot_start)

        booking_end = schedule.booking_end

        endtime = parsed_required_date_time - timedelta(hours=booking_end)

        return datetime.now()<endtime


    @classmethod
    def check_booking_start(cls,schedule):
        booking_start_day = schedule.booking_start

        scheduled_day = schedule.day
        today = datetime.strptime(date.today().strftime(r"%y-%m-%d"),r"%y-%m-%d")
        next_scheduled_day_date = datetime.strptime(get_next_date(scheduled_day),r"%y-%m-%d")

        delta = next_scheduled_day_date - today
        return delta.days <= booking_start_day
    
    @classmethod
    def check_booking_end(cls,schedule):
        booking_end_time = schedule.booking_end
        slot_start = schedule.slot_start
        scheduled_day = schedule.day
        next_scheduled_day_date = datetime.strptime(get_next_date(scheduled_day),r"%y-%m-%d")
        required_datetime = datetime.combine(next_scheduled_day_date,slot_start)
        endtime = required_datetime - timedelta(hours=booking_end_time)

        return datetime.now()<endtime

    @classmethod 
    def check_limit(cls,schedule,appointment_date):
        schedule_id = schedule.id
        appointment_date_obj = convert_str_to_date(appointment_date)
        appointments = cls.query.filter(schedule_id==schedule_id,appointment_date==appointment_date_obj).count()
        limit = schedule.patient_limit
        print(appointments,limit)
        if limit and appointments>=limit:
            return False
        return True
    
    
