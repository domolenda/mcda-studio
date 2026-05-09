from fastapi import APIRouter, HTTPException

from app.schemas.comparison import ComparisonRequest, ComparisonResponse
from app.services.comparison import compare_methods

router = APIRouter(prefix="/comparison")


@router.post("", response_model=ComparisonResponse)
def run_comparison(request: ComparisonRequest) -> ComparisonResponse:
    matrix = request.matrix
    weights = request.weights
    types = request.types
    methods_config = request.methods_config

    try:
        return compare_methods(matrix, weights, types, methods_config)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
