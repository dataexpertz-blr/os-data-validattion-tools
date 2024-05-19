import great_expectations as ge
import pandas as pd

# Sample DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}
df = pd.DataFrame(data)

# Create a Great Expectations DataFrame
ge_df = ge.from_pandas(df)

# Validate columns
ge_df.expect_column_to_exist("name")
ge_df.expect_column_values_to_be_between("age", 20, 40)
ge_df.expect_column_values_to_not_be_null("name")

# Print results
results = ge_df.validate()
print(results)
