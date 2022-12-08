from system.Models.Category import Category
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class GetCategory(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        ordered = True