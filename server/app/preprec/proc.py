from external import preprocessing
from pandas import DataFrame
import external

PRE_TYPES = external.preprocessing.PRE_TYPES
preproc = external.preprocessing.preproc


from auth.schemas import User



import globals

def prepr(user: User, methods: dict) -> DataFrame:
    d = globals.datasets[globals.state[user.username].dataset_id]
    res = preproc(d.head(10), methods)
    globals.state[user.username].dataset = res[0].insert(0, "label", res[2])
    return res
