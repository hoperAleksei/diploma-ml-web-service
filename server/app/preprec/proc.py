from external import preprocessing
from pandas import DataFrame
import external

PRE_TYPES = external.preprocessing.PRE_TYPES
preproc = external.preprocessing.preproc

from auth.schemas import User

import globals


def prepr(ds: DataFrame, methods: dict) -> DataFrame:
    d = ds.copy()
    res = preproc(d, methods)
    res[0].insert(0, "label", res[2])
    res = res[0]
    # globals.state[user.username].dataset = res[0].insert(0, "label", res[2])
    return res

# def prepr(user: User, methods: dict) -> DataFrame:
#     d = globals.datasets[globals.state[user.username].dataset_id]
#     res = preproc(d, methods)
#     globals.state[user.username].dataset = res[0].insert(0, "label", res[2])
#     return res
