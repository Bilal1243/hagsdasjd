from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd
import numpy as np

# Generate synthetic dataset with 5000 rows
np.random.seed(42)  # For reproducibility
data = {
    'Milk': np.random.randint(2, size=5000),
    'Bread': np.random.randint(2, size=5000),
    'Butter': np.random.randint(2, size=5000),
    'Cheese': np.random.randint(2, size=5000)
}


# gghjkdfhkgndf

# Convert dataset to DataFrame
df = pd.DataFrame(data)
pandas>=1.0.0
numpy>=1.18.0
mlxtend>=0.22.0
