from typing import Any
from datetime import datetime
from datasets import load_dataset
import meilisearch

# https://huggingface.co/datasets/mc4
dataset = load_dataset("mc4", "ja", split="train", streaming=True)
documents: list[dict[str, Any]] = list(dataset.take(30000))
# add primary key and convert datetime string into int type
for i, document in enumerate(documents):
    document["id"] = i
    document["timestamp"] = int(
        datetime.strptime(document["timestamp"], "%Y-%m-%dT%H:%M:%SZ").timestamp()
    )

client = meilisearch.Client("http://127.0.0.1:7700", "masterKey")
index = client.index("mc4")
index.update_settings(
    {
        "filterableAttributes": ["id", "text", "timestamp", "url"],
        "pagination": {"maxTotalHits": 200000},
    }
)
index.add_documents_in_batches(documents, primary_key="id")
