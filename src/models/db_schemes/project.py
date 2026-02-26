from pydantic import BaseModel, Field,validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    _id: Optional[ObjectId] 
    project_id: str = field(...,min_length=1)

    @validator('project_id')
    def validate_project_id(cls, value):
        if not value.isalnum() or value.isspace():
            raise ValueError('project_id must not be empty or whitespace')
        return value

    def config:
        arbitrary_types_allowed = True
 