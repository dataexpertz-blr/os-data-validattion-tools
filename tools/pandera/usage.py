import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema

# Sample DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}
df = pd.DataFrame(data)

# Define schema
schema = DataFrameSchema({
    "name": Column(pa.String),
    "age": Column(pa.Int, checks=pa.Check.in_range(20, 40))
})

# Validate DataFrame
validated_df = schema.validate(df)
print(validated_df)
