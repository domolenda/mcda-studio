from fastapi import APIRouter

from app.schemas.methods import (
    NormalizationMethod,
    NormalizationMethodsResponse,
    RankingMethod,
    RankingMethodsResponse,
)
from app.services.methods.registry import get_ranking_methods
from app.services.normalization.registry import get_normalization_methods

router = APIRouter(prefix="/methods")


@router.get("/ranking", response_model=RankingMethodsResponse)
def list_ranking_methods() -> RankingMethodsResponse:
    methods = get_ranking_methods()
    return RankingMethodsResponse(
        methods=[RankingMethod.model_validate(m) for m in methods]
    )


@router.get("/normalization", response_model=NormalizationMethodsResponse)
def list_normalization_methods() -> NormalizationMethodsResponse:
    methods = get_normalization_methods()
    return NormalizationMethodsResponse(
        normalizations=[NormalizationMethod.model_validate(m) for m in methods]
    )
