from pydantic import BaseModel, constr

class SectorInput(BaseModel):
    sector: constr(min_length=3, max_length=30)

