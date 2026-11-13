import json
from pathlib import Path

ROOT = Path(__file__).parents[1]

def test_recommender_notebook_excludes_source_by_index():
    notebook = json.loads((ROOT / "product_recommendation.ipynb").read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    source = "\n".join(
        "".join(cell.get("source", [])) if isinstance(cell.get("source", []), list)
        else cell.get("source", "")
        for cell in notebook["cells"]
    )
    assert "if train_df.index[idx] != source_index" in source
    assert "product_indices = indices[0][1:]" not in source
