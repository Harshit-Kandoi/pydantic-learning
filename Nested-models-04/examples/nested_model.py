from typing import Optional, List
from pydantic import BaseModel

class Address(BaseModel):
    street : str
    city : str
    postal_code : str
    
class User(BaseModel):
    id: int
    name: str
    address: Address
    
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None  # Recursive type reference
    
Comment.model_rebuild()  # Rebuild the model to resolve the recursive type reference

address = Address(street="123 Main St", city="Anytown", postal_code="12345")
user = User(id=1, name="John Doe", address=address)
comment = Comment(id=1, content="This is a comment", replies=[
    Comment(id=2, content="This is a reply", replies=[
        Comment(id=3, content="This is a nested reply")
    ])
])

    
    