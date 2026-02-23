
---

# **Day 8 – Read Excel**

```markdown
# Day 8 – Read Excel

## Objective
Learn to read Excel files using Python and pandas.

## What I Learned
- How to use `pandas` and `openpyxl` to load Excel
- How to inspect data using `df.head()` and `df.columns`
- Basic filtering using string matching

## Practice Example
```python
import pandas as pd

df = pd.read_excel("eco.xlsx")
print(df.head())
filtered = df[df["Subject"].str.contains("ECO")]
print(filtered)
