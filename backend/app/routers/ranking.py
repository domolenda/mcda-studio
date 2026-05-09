from fastapi import APIRouter, HTTPException

from app.schemas.ranking import RankingRequest, RankingResponse, WASPASRequest
from app.services.methods.topsis import TOPSIS
from app.services.methods.waspas import WASPAS

router = APIRouter(prefix="/ranking")


@router.post("/topsis", response_model=RankingResponse)
def rank_topsis(request: RankingRequest) -> RankingResponse:
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


@router.post("/waspas", response_model=RankingResponse)
def rank_waspas(request: WASPASRequest) -> RankingResponse:
    matrix = request.matrix
    weights = request.weights
    types = request.types
    normalization_method = request.normalization_method
    lambda_ = request.lambda_

    waspas = WASPAS()

    try:
        result = waspas.rank(matrix, weights, types, normalization_method, lambda_)
        return RankingResponse(ranking=result)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
