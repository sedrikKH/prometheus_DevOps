import base64

# Define an array of strings representing the steps in a software development lifecycle
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

# Loop through each step in the array and perform an operation
for step in steps:
    # Encode the current step as a base64 string
  print(base64.b64encode(step.encode('utf-8')))
