from fastapi import APIRouter, HTTPException

from app.schemas.weights import WeightsRequest, WeightsResponse
from app.services.weights import entropy_weights, equal_weights

router = APIRouter(prefix="/weights")


@router.post("/entropy", response_model=WeightsResponse)
def run_entropy_weights(request: WeightsRequest) -> WeightsResponse:
    matrix = request.matrix

    try:
        weights = entropy_weights(matrix).tolist()
        return WeightsResponse(weights=weights)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.post("/equal", response_model=WeightsResponse)
def run_equal_weights(request: WeightsRequest) -> WeightsResponse:
    matrix = request.matrix

    try:
        weights = equal_weights(matrix).tolist()
        return WeightsResponse(weights=weights)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
