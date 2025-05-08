from pydantic import BaseModel
from typing import List

#TODO: Create Course Model
#Each Course Has Modules
#Each Module Has Lessons

class Lesson(BaseModel):
    lesson_id: int
    lesson_name: str
    
class Module(BaseModel):
    module_id: int
    module_name: str
    lessons: List[Lesson]
    
class Course(BaseModel):
    course_id: int
    course_name: str
    modules: List[Module]