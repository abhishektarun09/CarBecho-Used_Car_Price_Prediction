from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequestSchema(BaseModel):
    km_driven: int = Field(..., gt=0)
    fuel: Literal["Petrol", "Diesel", "CNG", "LPG"]
    seller_type: Literal["Individual", "Dealer", "Trustmark Dealer"]
    transmission: Literal["Manual", "Automatic"]
    owner: Literal["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"]
    mileage: float = Field(..., gt=0)
    engine: float = Field(..., gt=0)
    max_power: float = Field(..., gt=0)
    seats: int = Field(..., ge=2, le=10)
    age: int = Field(..., ge=0)