from datasets import load_dataset
import meilisearch


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


dataset = load_dataset("amazon_reviews_multi", "ja", split="train")
index.add_documents_in_batches(list(dataset), primary_key="review_id")
