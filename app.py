from system import create_api , db
app = create_api()
with app.app_context(): db.create_all()
if __name__ == "__main__":
    app.run(host="0.0.0.0")