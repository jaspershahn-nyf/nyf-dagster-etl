import json
import os
import pandas as pd
from dagster import asset
from datetime import datetime

# df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})


@asset
def my_asset():
    os.makedirs("data", exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") 
    with open(f"data/{filename}.json", "w") as f:
        json.dump([9, 1, 2, 3], f)
