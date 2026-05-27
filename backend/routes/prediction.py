from fastapi import APIRouter
from agents.prediction_agent import birthstar_analysis

router=APIRouter()

@router.post("/birthstar")

async def birthstar(data:dict):

    result=await birthstar_analysis(
        data["birthstar"]
    )

    return result