from pydantic import BaseModel


class HoroscopeMatchRequest(BaseModel):

    groom_name: str
    groom_dob: str
    groom_time: str
    #groom_country: str
    groom_location: str

    bride_name: str
    bride_dob: str
    bride_time: str
    #bride_country: str
    bride_location: str