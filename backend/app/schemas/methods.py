from pydantic import BaseModel


class MethodParameter(BaseModel):
    name: str
    type: str
    default: float
    min: float
    max: float


class RankingMethod(BaseModel):
    id: str
    name: str
    normalization: bool
    default_normalization: str | None
    parameters: list[MethodParameter]


class RankingMethodsResponse(BaseModel):
    methods: list[RankingMethod]


class NormalizationMethod(BaseModel):
    id: str
    name: str


class NormalizationMethodsResponse(BaseModel):
    normalizations: list[NormalizationMethod]
