# About

~~Reproduction of MeiliSearch's error relating to [#2807](https://github.com/meilisearch/meilisearch/issues/2807)~~

**Error is fixed in MeiliSearch >= v0.30.0**

# Flow of Error Reproduction

Note: Used Python 3.10.6

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
   docker run -it --rm -p 7700:7700 -v $(pwd)/meili_data:/meili_data getmeili/meilisearch:v0.30.0
   ```

4. Add documents of the review dataset

   **This step would take a minute.**

   ```
   python reviews_index.py
   ```

5. Add documents of the mc4 dataset

   **This step would take a minute.**

   ```
   python mc4_index.py
   ```

6. Get tasks after several minutes, the error will be reproduced

   ```
   python get_tasks.py
   ```
