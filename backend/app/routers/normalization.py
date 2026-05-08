import numpy as np
from fastapi import APIRouter, HTTPException

from app.schemas.normalization import NormalizationRequest, NormalizationResponse
from app.services.normalization.min_max import MinMaxNormalization

router = APIRouter(prefix="/normalization")


@router.post("/min-max", response_model=NormalizationResponse)
def min_max_normalization(request: NormalizationRequest):
    matrix = request.matrix
    types = request.types

    norm = MinMaxNormalization(matrix, types)
    try:
        result = norm.normalize()
        rounded = np.round(result, 4).tolist()
        return NormalizationResponse(normalized_matrix=rounded)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
