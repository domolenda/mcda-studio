# mcda-studio

## PL

MCDA-studio to aplikacja webowa do analizy wielokryterialnej (MCDA/MCDM).  
Do głównych funkcjonalności należą:

- Import danych
- Konfiguracja metod (TOPSIS, VIKOR, WASPAS)
- Generowanie rankingów
- Wizualizacja i porównanie wyników

## EN

MCDA-studio is a web application for multi-criteria decision analysis (MCDA/MCDM).  
Its main features include:

- Data import
- Method configuration (TOPSIS, VIKOR, WASPAS)
- Ranking generation
- Visualization and comparison of results

## Demo

### General usage
![General usage](./media/use_example.gif)

### State snapshot usage
![State snapshot](./media/save_load_example.gif)

## Repository Structure

The repository is structured as follows:
```
mcda-studio/
├── backend/    # FastAPI/python - backend
├── frontend/   # Vue3/typescript - frontend
└── examples/   # Example datasets
```

## Setup Instructions

### Frontend
[front-end](./frontend/README.md)

### Backend
[back-end](./backend/README.md)


## Example Datasets

If you want to try the application with example datasets, you can find them in the [examples](./examples/) directory. When using own datasets, make sure they are in the same format as the example datasets.
