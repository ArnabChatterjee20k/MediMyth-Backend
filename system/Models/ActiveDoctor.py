from system import db
from sqlalchemy.ext.hybrid import hybrid_property
class ActiveDoctor(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    doctor_id = db.Column(db.Integer,db.ForeignKey("doctor.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False,unique=True)
    active_doctor_id = db.Column(db.String,unique=True)
    scheduled_data = db.relationship("Schedule",backref="scheduled_data",lazy="dynamic",cascade='all,delete',passive_deletes=True)
    vacation_data = db.relationship("Vacation",backref="active_doctor",lazy="dynamic",cascade='all,delete',passive_deletes=True)
    # @hybrid_property
    # def active_doctor_id(self):
    #     return f"MMD-{self.id}"