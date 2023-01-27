from system import db
from system.Config import Config
from system.SearchEngine.utils.upload_data import upload


def set_active(model,id,ActiveModel,ActiveModelRelationId,active_field):
    doctor = model.query.filter_by(id=id).first_or_404()
    
    new_active_obj = ActiveModel()
    setattr(new_active_obj,ActiveModelRelationId,id)
    db.session.add(new_active_obj)
    # flushing the object to the database to access it's id before adding to the database
    db.session.flush()

    active_id = new_active_obj.id
    medimyth_active_id = f"{Config.ACTIVE_TAG}-{active_id}"
    # new_active_obj.active_id = medimyth_active_id
    setattr(new_active_obj,active_field,medimyth_active_id)
    db.session.commit()
    
    upload(doctor_obj=doctor, active_id=active_id)
    return medimyth_active_id
