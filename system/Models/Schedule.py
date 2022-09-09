from system import db
from system.Models.Doctor import Doctor
from system.Models.ActiveDoctor import ActiveDoctor
from sqlalchemy.dialects.postgresql import TIME
from sqlalchemy import or_ , and_ 
class Schedule(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    active_doctor_id = db.Column(db.Integer,db.ForeignKey("active_doctor.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    phone_no = db.Column(db.String,nullable=False)
    
    day = db.Column(db.Integer,nullable=False) # accepting weekday means if day is monday then 0, if tuesday then 1
    # using weekday we can get the date of the day from the calendar easily
    specific_week = db.Column(db.Integer) # 1,2,3,4 -> 4 weeks in a month. If null means every week
    
    slot_start = db.Column(TIME(),nullable=False)
    slot_end = db.Column(TIME())
    
    booking_start = db.Column(db.Integer,default=7)# 1,2,3,4,5,6,7,.....before.
    booking_end = db.Column(db.Integer,default=2) # 2hours before before the slot_start
    
    fees = db.Column(db.Integer)
    patient_limit = db.Column(db.Integer)
    
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
    
    def get_slot_start(self):
        # Although slot start will be definitely present in the attributes but still validating
        return getattr(self,"slot_start",None)
    
    def get_slot_end(self):
        # slot end may not be present in the attributes so it will give error. So that default None will be returned in that case
        return getattr(self,"slot_end",None)

    def get_active_doctor_id(self):
        return getattr(self,"active_doctor_id",None)
    
    def get_specific_week(self):
        return getattr(self,"specific_week",None)

    def check_slot_specific_week(self,doctor_id=None):
        """
            checking if slot_start and slot_end lying between other schedule times or not of a specific active doctor
        """
        if self.get_active_doctor_id():
            active_doctor_schedules = Schedule.query.filter(Schedule.active_doctor_id==self.get_active_doctor_id(),Schedule.specific_week==self.get_specific_week())
            print(Schedule.query.filter(Schedule.active_doctor_id==self.get_active_doctor_id(),Schedule.specific_week==self.get_specific_week()).all())
        elif doctor_id:
            active_doctor_schedules = Schedule.query.filter(Schedule.active_doctor_id==doctor_id,Schedule.specific_week==self.get_specific_week())
        else:
            raise Exception("Not active doctor id ")

        print(active_doctor_schedules.all())
        if not active_doctor_schedules.first():
            return False

        schedule_cant_be_created = False

        slot_start = self.get_slot_start()
        slot_end = self.get_slot_end()

        if slot_start and slot_end:
            if active_doctor_schedules.filter(or_(
                Schedule.slot_start.between(slot_start,slot_end) , 
                Schedule.slot_end.between(slot_start,slot_end)
                )).first():
                return True
        
        if slot_start and not slot_end:
            print("Yes")
            if active_doctor_schedules.filter(
                and_((Schedule.slot_start<=slot_start),
                and_(Schedule.slot_end>slot_start,Schedule.slot_end.isnot(None)))
                ).first():
                return True
            
        if not slot_start and slot_end:
            if active_doctor_schedules.filter(and_((Schedule.slot_start<slot_end),
                and_(Schedule.slot_end>=slot_end,Schedule.slot_end.isnot(None)))).first():
                return True 
        
        return schedule_cant_be_created

    def check_slot_no_specific_week(self,doctor_id=None):
        """
            checking if slot_start and slot_end lying between other schedule times or not of a specific active doctor
        """
        if self.get_active_doctor_id():
            active_doctor_schedules = Schedule.query.filter(Schedule.active_doctor_id==self.get_active_doctor_id())
        elif doctor_id:
            active_doctor_schedules = Schedule.query.filter(Schedule.active_doctor_id==doctor_id)
        else:
            raise Exception("Not active doctor id ")

        print(active_doctor_schedules.all())
        if not active_doctor_schedules.first():
            return False

        schedule_cant_be_created = False

        slot_start = self.get_slot_start()
        slot_end = self.get_slot_end()

        if slot_start and slot_end:
            if active_doctor_schedules.filter(or_(
                Schedule.slot_start.between(slot_start,slot_end) , 
                Schedule.slot_end.between(slot_start,slot_end)
                )).first():
                return True
        
        if slot_start and not slot_end:
            print("Yes")
            if active_doctor_schedules.filter(
                and_((Schedule.slot_start<=slot_start),
                and_(Schedule.slot_end>slot_start,Schedule.slot_end.isnot(None)))
                ).first():
                return True
            
        if not slot_start and slot_end:
            if active_doctor_schedules.filter(and_((Schedule.slot_start<slot_end),
                and_(Schedule.slot_end>=slot_end,Schedule.slot_end.isnot(None)))).first():
                return True 
        
        return schedule_cant_be_created

    def check_slot(self,doctor_id=None):
        if not self.get_specific_week():
            print("yes")
            return self.check_slot_no_specific_week(doctor_id=doctor_id)
        return self.check_slot_specific_week(doctor_id=doctor_id)

    @classmethod
    def active_doctor_by_email(cls,email):
        doctor = Doctor.query.filter_by(email=email).first_or_404()
        return doctor.active_id.first().id
    @classmethod
    def check_schedule(cls,active_doctor_id,schedule_id):
        current_schedule_query = Schedule.query.filter_by(id=schedule_id,active_doctor_id=active_doctor_id)
        current_schedule = current_schedule_query.first_or_404()
        return current_schedule_query
    
    @classmethod
    def check_and_update(cls,id,active_doctor_id,**data):
        schedule = cls.check_schedule(active_doctor_id=active_doctor_id,schedule_id=id)
        schedule.update(data)
        db.session.commit()

    @classmethod
    def check_and_delete(cls,active_doctor_id,id):
        schedule = cls.check_schedule(active_doctor_id=active_doctor_id,schedule_id=id).first()
        patients = schedule.appointment_data
        print(patients)
        db.session.delete(schedule)
        db.session.commit()
        return patients # so that they can be notified