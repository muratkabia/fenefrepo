# File: plugins/sample_plugin.py

def get_options():
    return ["Option", "Test"]

def execute_option(option,session):
    """
    Executes the selected option of the sample plugin.
    """
    print("Sample Plugin: Executing option '{}'".format(option))
    # Add your plugin logic here
