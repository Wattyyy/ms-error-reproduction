import meilisearch

client = meilisearch.Client("http://127.0.0.1:7700", "masterKey")
print(client.get_tasks())
