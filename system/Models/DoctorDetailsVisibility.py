from system import db

default_value = True
class DoctorDetailsVisibility(db.Model):
    """
        True means everyone can see it
        False means only me

        But all details will be visible to admin
    """
    id = db.Column(db.Integer,primary_key = True)
    doctor_id = db.Column(db.Integer,db.ForeignKey("doctor.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    email_visibility = db.Column(db.Boolean,default=default_value)
    reg_no_visibility = db.Column(db.Boolean,default=default_value)
    phone_no_visibility = db.Column(db.Boolean,default=True)