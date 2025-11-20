import pandas as pd
import json

def load_browser_history(path):
    with open(path,"r") as file:
        data=json.load(file)
    return pd.DataFrame(data)

def load_app_usage(path):
    return pd.read_csv(path)

def load_step_usage(path):
    return pd.read_csv(path)