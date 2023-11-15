# Vorhersage von Kreditkartentransaktionen

## Überblick

Dieses Repository beinhaltet ein Projekt zur Vorhersage von Kreditkartentransaktionen. Es ist Teil einer Studiumsleistung und zielt darauf ab, mithilfe von maschinellen Lernmethoden die Wahrscheinlichkeit von Kreditkartentransaktionen zu erkennen. Das Projekt umfasst verschiedene Phasen von der explorativen Datenanalyse bis hin zur Modellentwicklung und -evaluation.

## Projektstruktur

- `data/`: Verzeichnis für die Datensätze, die im Projekt verwendet werden.
- `code/`: Enthält Jupyter Notebooks für verschiedene Phasen des Projekts:
  - `1_exploratory_data_analysis.ipynb`: Explorative Datenanalyse
  - `2_feature_engineering.ipynb`: Feature-Engineering
  - `3_build_models.ipynb`: Modellbildung
  - `4_business_prediction.ipynb`: Geschäftsvorhersagen
- `tests/`: Verzeichnis für Unit-Tests.
- `dashboard/`: Dashboard-Anwendungen zur Visualisierung der Ergebnisse.
- `results/`: Ordner zur Speicherung von Ausgabeergebnissen wie Modellen, Grafiken usw.

## Installation

Um das Projekt zu starten, klonen Sie das Repository und installieren Sie die erforderlichen Abhängigkeiten:

```bash
git clone [Repository-URL]
cd model_engineering_creditdata-main
pip install -r requirements.txt
```

## Verwendung

Jedes Notebook im `code/`-Verzeichnis kann individuell ausgeführt werden (sofern das Notebook zuvor mindestens einmal ausgeführt wurde), um die verschiedenen Phasen des Projekts zu durchlaufen. Es wird empfohlen, die Notebooks in der angegebenen Reihenfolge zu durchlaufen.