import numpy as np
from fastapi import APIRouter, HTTPException

from app.schemas.ranking import RankingRequest, RankingResponse
from app.services.methods.topsis import TOPSIS

router = APIRouter(prefix="/ranking")


@router.post("/topsis", response_model=RankingResponse)
async def rank(request: RankingRequest) -> RankingResponse:
    norm_matrix = request.normalized_matrix
    weights = request.weights
    types = request.types

    topsis = TOPSIS(norm_matrix, weights, types)

    try:
        result = topsis.rank()
        return RankingResponse(ranking=result)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
