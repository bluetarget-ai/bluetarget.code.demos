from bluetarget import BlueTarget, Implementation, Framework

bt = BlueTarget(api_key="YOUR_API_KEY")

bt.deploy(
    model_class="Model",
    model_files=["model.py", "model.pkl"],
    requirements_file="requirements.txt",
    model_name="FirstName",
    implementation=Implementation.py38,
    framework=Framework.sklearn
)
