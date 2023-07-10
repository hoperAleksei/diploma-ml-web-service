from autoload import load_config
from algorithm import Algorithm
from sklearn.tree import DecisionTreeClassifier


@load_config()
class tree(DecisionTreeClassifier, Algorithm):
    ALGORITHM_NAME = 'Decision Tree'
    DESCRIPTION = "Дерево решений — классификатор, построенный на основе решающих правил вида «если, то»," \
                  " упорядоченных в древовидную иерархическую структуру."

    PRE_REQ = [Algorithm.PreReq.NOT_NULL]

    INPUT_TYPES = [Algorithm.InputTypes.INT,
                   Algorithm.InputTypes.FLOAT,
                   Algorithm.InputTypes.BOOL,
                   Algorithm.InputTypes.STRING]
    PARAMS = [
        {
            'name': 'max_depth',
            'type': 'int',
            'min': '1',
            'max': '100',
            'decs': 'Максимальная глубина дерева'
        },
        {
            'name': 'criterion',
            'type': 'set',
            'values': ['gini', 'entropy', 'log_loss'],
            'decs': 'Функция разделения'
        }
    ]

    def __init__(self, max_depth=3, criterion='gini'):
        DecisionTreeClassifier.__init__(self, max_depth=max_depth,
                                        criterion=criterion,
                                        random_state=0
                                        )
