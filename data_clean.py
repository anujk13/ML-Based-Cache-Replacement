import pandas as pd
import random

# Load dataset
df = pd.read_csv(r"C:\Users\hp\Desktop\Os-PBL\Os-PBL\dataset.csv")
df.columns = df.columns.str.strip()

CACHE_SIZE = 4
lru_cache = []
lru_hits = 0
replace_labels = []
page_age = {}  

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

for _, row in df.iterrows():
    page = row['Page/Frame ID']

    # Increase age for all pages in memory
    for p in list(page_age.keys()):
        page_age[p] += 1

    reference_bit = 1 if page in lru_cache else 0
    dirty_bit = 1 if str(row['Operation Type(R/W)']).strip().upper() == 'W' else 0
    access_count = page_age.get(page, 0)
    age = random.randint(1, 20)

    # LRU Cache simulation
    lru_replace = 0
    if page in lru_cache:
        lru_hits += 1
        lru_cache.remove(page)
        lru_cache.append(page)
    else:
        if len(lru_cache) < CACHE_SIZE:
            lru_cache.append(page)
        else:
            lru_cache.pop(0)
            lru_cache.append(page)
            lru_replace = 1

    # Optional randomness to avoid always replacing
    if lru_replace == 1 and random.random() < 0.3:
        lru_replace = 0

    replace_labels.append(lru_replace)
    page_age[page] = 0

# Create new dataset
df_new = pd.DataFrame({
    'Reference bit': [1 if p in lru_cache else 0 for p in df['Page/Frame ID']],
    'dirty bit': [1 if str(op).strip().upper() == 'W' else 0 for op in df['Operation Type(R/W)']],
    'age': [random.randint(1,20) for _ in range(len(df))],
    'access count': [page_age.get(p, 0) for p in df['Page/Frame ID']],
    'replace': replace_labels,
})

# Save dataset
df_new.to_csv("newdataset.csv", index=False)

# Preview
print("Columns:", df_new.columns.tolist())
print("Total samples:", len(df_new))
print("Class distribution:\n", df_new['replace'].value_counts())
print("\nPreview:\n", df_new.head(20))
