from system import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import DATE
from system.Models.Schedule import Schedule
from system.Models.Vacation import Vacation
from system.utils.convert_str_to_date import convert_str_to_date
from system.utils.datetime_fns import isInAppointmentRange


class Appointment(db.Model):
    # this is for patients who will book to a schedule
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.String)
    schedule_id = db.Column(db.Integer, db.ForeignKey(
        "schedule.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    appointment_id = db.Column(db.String, unique=True)
    person_id = db.Column(db.Integer)
    name = db.Column(db.String(30), nullable=False)
    # contact number of the patient
    contact_number = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    # this is only for the date in which we will meet the doctor. The booking start time and booking end time will be based on current date and time
    appointment_date = db.Column(DATE(), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    # @hybrid_property
    # def appointment_id(self):
    #     return f"MMA-{self.id}"

    @classmethod
    def check_booking(cls, id, appointment_date):
        schedule = Schedule.query.filter_by(id=id).first_or_404()
        params = {
            "provided_date": appointment_date,
            "scheduled_day": schedule.day,
            "starting_day": schedule.booking_start,
            "end_hour": schedule.booking_end,
            "slot_start": schedule.slot_start,
            "req_specfic_week": schedule.specific_week
        }
        print(isInAppointmentRange(**params))
        return cls.check_limit(schedule, appointment_date) and isInAppointmentRange(**params) , schedule

    @classmethod
    def check_vacation(cls, id, appointment_date):
        print("vacation",Schedule.query.join(Schedule.vacation).filter(Schedule.id == id, Vacation.start <= appointment_date, Vacation.end >= appointment_date).first())
        return Schedule.query.join(Schedule.vacation).filter(Schedule.id == id, Vacation.start <= appointment_date, Vacation.end >= appointment_date).first()

    @classmethod
    def check_limit(cls, schedule, appointment_date):
        schedule_id = schedule.id
        appointment_date_obj = convert_str_to_date(appointment_date)
        appointments = cls.query.filter(
            cls.schedule_id == schedule_id, cls.appointment_date == appointment_date_obj).count()
        limit = schedule.patient_limit
        if limit and appointments >= limit:
            return False
        return True
