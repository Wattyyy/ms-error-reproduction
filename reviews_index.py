from typing import Any
from datasets import load_dataset
import meilisearch

# https://huggingface.co/datasets/amazon_reviews_multi
dataset = load_dataset("amazon_reviews_multi", "ja", split="train")
documents: list[dict[str, Any]] = list(dataset)

client = meilisearch.Client("http://127.0.0.1:7700", "masterKey")
index = client.index("reviews")
index.update_settings(
    {
        "filterableAttributes": [
            "review_id",
            "product_id",
            "reviewer_id",
            "stars",
            "review_body",
            "review_title",
            "language",
            "product_category",
        ],
        "pagination": {"maxTotalHits": 200000},
    }
)
index.add_documents_in_batches(documents, primary_key="review_id")
