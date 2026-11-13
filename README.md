# Product Recommendation System

Content-based recommendations from product review text using TF-IDF and cosine nearest-neighbour search.

## Dataset
`product reviews.csv` contains product IDs, review summaries, and review text.

The notebook's recommendation lookup now uses row positions from the same training subset used to fit its TF-IDF matrix, preventing the previous full-data/train-matrix index mismatch.

This is content-based recommendation, not collaborative filtering; it does not model user purchase histories or preferences.
