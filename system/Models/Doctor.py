from system import db
from werkzeug.security import check_password_hash , generate_password_hash
from system.Models.ActiveDoctor import ActiveDoctor
from system.utils.set_active import set_active
from system.SearchEngine.utils.upload_data import upload
class Doctor(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),nullable=False)
    phone_no = db.Column(db.String(10),nullable=False)
    email = db.Column(db.String(30),nullable=False,unique=True)
    reff_code = db.Column(db.String(10),default=None)
    address = db.Column(db.String,nullable=False)
    reg_no = db.Column(db.String(20),nullable=False,unique=True)
    category = db.Column(db.String(20),nullable=False)
    description = db.Column(db.String)
    profile_pic = db.Column(db.String,default=None)
    _password = db.Column(db.String)
    active = db.Column(db.Boolean,default=False)

    email_visibility = db.Column(db.Boolean,default=True)
    reg_no_visibility = db.Column(db.Boolean,default=True)
    phone_no_visibility = db.Column(db.Boolean,default=True)

    active_id = db.relationship("ActiveDoctor",backref="active_id",lazy="dynamic",cascade='all,delete',passive_deletes=True)
    
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,value):
        self._password = generate_password_hash(value)

    @classmethod
    def set_active(cls,id):
        doctor , medimyth_active_id, active_id = set_active(
            model=Doctor,
            id=id,
            ActiveModel=ActiveDoctor,
            ActiveModelRelationId="doctor_id",
            active_field="active_doctor_id"
        )
        upload(doctor_obj=doctor, active_id=active_id)
        return medimyth_active_id
    
    @classmethod
    def check_password(cls,password,email):
        doctor = Doctor.query.filter_by(email=email).first_or_404()
        return check_password_hash(doctor.password,password)