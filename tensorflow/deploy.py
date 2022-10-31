from bluetarget import BlueTarget, Server, Implementation, Framework

bt = BlueTarget(api_key="YOUR_API_KEY")

bt.deploy(
    model_class="Model",
    model_files=["model.py", "my_model/saved_model.pb",
                 "my_model/keras_metadata.pb",
                 "my_model/variables/variables.index",
                 "my_model/variables/variables.data-00000-of-00001"],
    requirements_file="requirements.txt",
    serverId=Server.standard_small,
    implementation=Implementation.py38,
    framework=Framework.tensorflow
)
