from system.SearchEngine.client import connect_to_algolia_client

def upload(doctor_obj):
    client = connect_to_algolia_client()

    data = ["id",
                "name",
                "profile_pic",
                "category"]
    record = {}
    for col_name in doctor_obj.__table__.columns.keys():
        if col_name in data:
            record[col_name] = getattr(doctor_obj,col_name)
    

    index = client.init_index("medimyth")
    index.save_object(record,{'autoGenerateObjectIDIfNotExist': True})