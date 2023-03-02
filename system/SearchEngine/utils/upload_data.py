from system.SearchEngine.client import connect_to_algolia_client
from system.Config import Config
def upload(doctor_obj,active_id):
    client = connect_to_algolia_client()

    data = [    "name",
                "profile_pic",
                "category"]
    record = {}
    record["id"] = active_id # adding the active id
    for col_name in doctor_obj.__table__.columns.keys():
        if col_name in data:
            record[col_name] = getattr(doctor_obj,col_name)
    

    index = client.init_index(Config.ALGOLIA_INDEX)
    index.save_object(record,{'autoGenerateObjectIDIfNotExist': True})