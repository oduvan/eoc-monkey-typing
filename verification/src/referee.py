from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "count_words"
    FUNCTION_NAMES = {
        "python_3": "count_words",
        "js_node": "countWords"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''def cover(func, data):
    return func(data[0], set(data[1]))
''',
            ENV_NAME.JS_NODE: '''

function cover(func, in_data) {
    return func.apply(this, in_data)
}

    '''
    }