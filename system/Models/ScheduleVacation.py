from system import db

schedule_vacation = db.Table(
    "schedule_vacation",
    db.Column("schedule_id",db.Integer, db.ForeignKey("schedule.id",
              onupdate="CASCADE", ondelete="CASCADE"), nullable=False,primary_key=True),
    db.Column("vacation_id",db.Integer, db.ForeignKey("vacation.id",
              onupdate="CASCADE", ondelete="CASCADE"), nullable=False,primary_key=True)
)
