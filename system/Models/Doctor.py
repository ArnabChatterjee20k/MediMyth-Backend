from system import db
from werkzeug.security import check_password_hash , generate_password_hash
class Doctor(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),nullable=False)
    phone_no = db.Column(db.String(10),nullable=False)
    email = db.Column(db.String(30),nullable=False,unique=True)
    reff_code = db.Column(db.String(10),default=None)
    address = db.Column(db.String,nullable=False)
    reg_no = db.Column(db.String(20),nullable=False,unique=True)
    category = db.Column(db.String(20),nullable=False)
    profile_pic = db.Column(db.String,default=None)
    _password = db.Column(db.String)
    active = db.Column(db.Boolean,default=False)

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,value):
        self._password = generate_password_hash(value)

    @classmethod
    def set_active(cls,id):
        doctor = Doctor.query.filter_by(id=id).first()
        doctor.active = True
        db.session.commit()
    
    @classmethod
    def check_password(cls,password,email):
        try:
            doctor = Doctor.query.filter_by(email=email).first()
            return check_password_hash(doctor.password,password)
        except:
            raise ValueError