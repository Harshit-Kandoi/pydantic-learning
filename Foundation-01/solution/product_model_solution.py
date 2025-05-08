from pydantic import BaseModel

# TODO: Create Product model with id, name, price, in_stock
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True
    
input_data = {
    "id": 1,
    "name": "Panner",
    "price": 100.0}

pro = Product(**input_data)
print(pro)