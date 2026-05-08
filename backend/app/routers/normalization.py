import numpy as np
from fastapi import APIRouter, HTTPException

from app.schemas.normalization import NormalizationRequest, NormalizationResponse
from app.services.normalization.min_max import MinMaxNormalization

router = APIRouter(prefix="/normalization")


@router.post("/min-max", response_model=NormalizationResponse)
def min_max_normalization(request: NormalizationRequest):
    matrix = np.array(request.matrix)
    types = request.types

    norm = MinMaxNormalization(matrix, types)
    try:
        result = norm.normalize()
        return NormalizationResponse(normalized_matrix=result.tolist())
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
