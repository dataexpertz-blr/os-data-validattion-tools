from cerberus import Validator

# Define schema
schema = {
    "name": {"type": "string"},
    "age": {"type": "integer", "min": 20, "max": 40}
}

# Sample data
document = {"name": "Alice", "age": 25}

# Validate data
v = Validator(schema)
if v.validate(document):
    print("Valid data!")
else:
    print("Invalid data:", v.errors)
