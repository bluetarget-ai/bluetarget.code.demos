from bluetarget import BlueTarget

bt = BlueTarget(api_key="YOUR_API_KEY")

bt.set_model_id("YOUR_MODEL_ID")


inputs = [
    [6.9, 3.1, 5.1, 2.3],
    [5.8, 2.7, 5.1, 1.9]
]

response = bt.predict(
    inputs
)

print(response)
