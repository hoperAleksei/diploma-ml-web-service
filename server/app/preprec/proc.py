from external import preprocessing
from pandas import DataFrame
import external

PRE_TYPES = external.preprocessing.PRE_TYPES
preproc = external.preprocessing.preproc


from auth.schemas import User



import globals

def prepr(user: User, methods: dict):
    d = globals.datasets[globals.users[user.username]["dataset"]]
    return preproc(d, methods)
