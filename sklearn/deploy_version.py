from bluetarget import BlueTarget

bt = BlueTarget(api_key="YOUR_API_KEY")

bt.deploy_new_version(
    model_id="YOUR_MODEL_ID",
    model_class="Model",
    model_files=["model.py", "model.pkl"],
    requirements_file="requirements.txt",
)
