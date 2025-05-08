from pydantic import BaseModel

#TODO: Create Booking Model
#Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >= 1)
# - rate_per_night: float
# Also, add computed field: total_amount = rate_per_night * nights