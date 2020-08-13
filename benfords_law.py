"""Test provided CSV of values against Benford's Law"""

import benfordslaw as bl

# Load elections example
df = bl.import_example()

# Extract election information.
X = df['votes'].loc[df['candidate']=='Donald Trump'].values

# Print
print(X)
# array([ 5387, 23618,  1710, ...,    16,    21,     0], dtype=int64)

# Make fit
out = bl.fit(X)

# Plot
bl.plot(out, title='Donald Trump')

