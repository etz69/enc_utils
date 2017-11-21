from st2actions.runners.pythonrunner import Action
from st2client.client import Client

import os

class St2KeyToArray(Action):
    def __init__(self, config=None):
        super(St2KeyToArray, self).__init__(config=config)
        api_url = os.environ.get('ST2_ACTION_API_URL', None)
        token = os.environ.get('ST2_ACTION_AUTH_TOKEN', None)
        self.client = Client(api_url=api_url, token=token)

    def run(self, st2_key):

        _resultObject = list()
        _st2_value = str(self.client.keys.get_by_name(name=st2_key))

        try:
            _resultObject = _st2_value.split(',')
        except Exception as e:
            self.logger.error('Could not convert key')
            return False, e

        return True, _resultObject


