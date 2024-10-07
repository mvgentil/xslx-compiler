import pandas as pd
from app.pipeline.transform import concat_dataframes

df_1 = pd.DataFrame({'col1': [1,2], 'col2':[3,4]})
df_2 = pd.DataFrame({'col1': [5,6], 'col2':[7,8]})

def test_transform():

    data = [df_1, df_2]
    arrange = pd.concat(data, ignore_index=True)

    act = concat_dataframes([df_1, df_2])

    assert len(arrange) == len(act)