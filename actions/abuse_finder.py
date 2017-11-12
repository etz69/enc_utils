from abuse_finder import domain_abuse

from st2actions.runners.pythonrunner import Action


class AbuseFinder(Action):
    def __init__(self, config=None):
        super(AbuseFinder, self).__init__(config=config)

    def run(self, tld):
        self.logger.info('Abuse Finder called')
        _abuse_contact = ""


        try:
            result = domain_abuse(tld)
            _abuse_contact = str(result['abuse'][0])
        except Exception as e:
            self.logger.error('Abuse finder ended with error')
            return False, _abuse_contact

        return True, _abuse_contact
