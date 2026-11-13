# Product Recommendation System

A content-based recommendation project that uses product review text, TF-IDF vectorization and cosine similarity to retrieve products with similar review content.

<p align="center">
  <img src="https://img.shields.io/badge/Project-Recommendation%20Systems-6C63FF?style=for-the-badge" alt="Recommendation system">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Notebook-Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
</p>

## Project overview

This notebook demonstrates a text-based recommendation pipeline. It represents review content as TF-IDF vectors and finds nearby items using cosine similarity.

**Interface:** Jupyter Notebook  
**Notebook:** `product_recommendation.ipynb`  
**Live web demo:** Not currently published.

## Dataset

The notebook expects `product reviews.csv` in the repository root. It uses product identifiers, review summaries and review text. Preserve the original filename and column names unless the notebook's data-loading cells are changed.

## How it works

1. Load and inspect product review records.
2. Prepare the available review text.
3. Convert text into TF-IDF feature vectors.
4. Calculate nearest neighbours using cosine similarity.
5. Retrieve products with similar review content.

## Technology

Python · Pandas · scikit-learn · TF-IDF · Cosine similarity · Jupyter Notebook

## Run locally

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook
```

Open `product_recommendation.ipynb` and execute the cells in order.

## Recommendation design

The notebook maps recommendation positions back to the same training subset used to fit the TF-IDF matrix. The source item is excluded by its original row identity so it is not recommended as its own nearest neighbour.

## Limitations

- This is **content-based retrieval**, not collaborative filtering.
- It does not learn user-specific preferences, purchase histories or real-time product availability.
- Similar review language does not guarantee equivalent product quality.
- Recommendation quality depends on text coverage, data quality and preprocessing.

## Future improvements

- Add a Streamlit interface for product lookup.
- Compare TF-IDF with sentence embeddings.
- Add recommendation explanations and offline ranking metrics.
- Evaluate coverage and diversity in addition to similarity.

## Author

**Md Luqman Ali** · [GitHub](https://github.com/Md-Luqman-Ali) · [LinkedIn](https://www.linkedin.com/in/mdluqmanali/)
