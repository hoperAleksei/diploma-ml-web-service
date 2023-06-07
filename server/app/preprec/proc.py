from external import preprocessing

import external

PRE_TYPES = external.preprocessing.PRE_TYPES
preproc = external.preprocessing.preproc


from auth.schemas import User



import globals

async def prepr(user: User, methods: dict):
    return preproc(globals.datasets[globals.users[user.username]["dataset"]], methods)
