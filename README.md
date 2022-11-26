# About

Reproduction of MeiliSearch's error relating to [#2807](https://github.com/meilisearch/meilisearch/issues/2807)

# Flow of Error Reproduction

Note: Used Python 3.11

1. Clone this repository

   ```
   git clone git@github.com:Wattyyy/ms-error-reproduction.git && cd ms-error-reproduction
   ```

2. Install libraries

   ```
   pip install -r requirements.txt
   ```

3. Run MeiliSearch

   ```
   curl -L https://install.meilisearch.com | sh && ./meilisearch --master-key=masterKey
   ```

4. Add documents of the review dataset

   ```
   python reviews_index.py
   ```

5. Add documents of the mc4 dataset

   This step would take a minute.

   ```
   python mc4_index.py
   ```

6. Get tasks and the error will be reproduced

   ```
   python get_tasks.py
   ```
