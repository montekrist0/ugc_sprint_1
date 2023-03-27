from pydantic import BaseModel


class ViewProgress(BaseModel):
    film_id: str
    user_id: str
    value: int
