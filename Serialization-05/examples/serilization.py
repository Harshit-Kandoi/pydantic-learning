from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    addresses: List[Address]
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

    
# create a user instance
user = User(
    id=1,
    name="John Doe",
    email="kandoiharshitsdlp@gmail.com",
    created_at=datetime.now(),
    addresses=[
        Address(street="123 Main St", city="New York", zip_code="10001"),
    ],
    tags=["admin", "user"]
)

# Using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict)

# Using model_dump_json() -> str
json_str = user.model_dump_json()
print(json_str)