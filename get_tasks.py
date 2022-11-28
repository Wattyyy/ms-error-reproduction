import meilisearch

client = meilisearch.Client("http://0.0.0.0:7700", "masterKey")
print(client.get_tasks())
