from fastapi import APIRouter, HTTPException

from app.schemas.ranking import RankingRequest, RankingResponse
from app.services.methods.topsis import TOPSIS

router = APIRouter(prefix="/ranking")


@router.post("/topsis", response_model=RankingResponse)
def rank(request: RankingRequest) -> RankingResponse:
    matrix = request.matrix
    weights = request.weights
    types = request.types
    normalization_method = request.normalization_method

    topsis = TOPSIS()

    try:
        result = topsis.rank(matrix, weights, types, normalization_method)
        return RankingResponse(ranking=result)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
