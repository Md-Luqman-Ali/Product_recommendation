# Product Recommendation System

A content-based recommendation notebook that represents product review text with TF-IDF and retrieves similar items using cosine similarity.

## Dataset

The notebook expects `product reviews.csv` in the repository root. It uses product identifiers, review summaries, and review text. Preserve the source column names and filename when running the notebook.

## Run the notebook

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# Windows cmd: .venv\\Scripts\\activate.bat
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook
```

Open `product_recommendation.ipynb` and execute the cells in order. The recommendation lookup maps positions from the same training subset used to fit the TF-IDF matrix.

## How it works

1. Prepare and combine the available review text.
2. Convert text into TF-IDF vectors.
3. Compute nearest neighbours using cosine similarity.
4. Return products with similar review content.

## Limitations

This is content-based retrieval, not collaborative filtering. It does not learn user-specific preferences, purchase histories, or product availability. Similar review language does not guarantee equivalent product quality.

## Stack

Python · Pandas · scikit-learn · TF-IDF · Cosine similarity · Jupyter
