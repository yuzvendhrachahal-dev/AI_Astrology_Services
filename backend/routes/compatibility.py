from fastapi import APIRouter

from models.schemas import (
    HoroscopeMatchRequest
)

from agents.compatibility_agent import (
    horoscope_matching_agent
)

router = APIRouter()


@router.post("/horoscope-match")
def horoscope_match(
    request: HoroscopeMatchRequest
):

    result = horoscope_matching_agent(
        request
    )

    return {
        "success": True,
        "report": result
    }