from bluetarget import BlueTarget

bt = BlueTarget(api_key="YOUR_API_KEY")

bt.set_model_id("YOUR_MODEL_API")

inputs = [
    "http://c.files.bbci.co.uk/48DD/production/_107435681_perro1.jpg",
]

response = bt.predict(
    inputs
)

print(response)
