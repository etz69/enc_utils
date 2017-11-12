from st2actions.runners.pythonrunner import Action

from pythonwhois.net import get_whois_raw
from pythonwhois.parse import parse_raw_whois


class AbuseFinder(Action):
    def __init__(self, config=None):
        super(AbuseFinder, self).__init__(config=config)

    def run(self, tld):
        self.logger.info('Abuse Finder called')
        _abuse_contact = ""
        names = list()
        emails = list()

        try:
            data = get_whois_raw(tld)
            parsed_whois = parse_raw_whois(data, ['Domain', 'contacts'])

            _abuse_contact = parsed_whois['emails'][0]

        except Exception as e:
            self.logger.error('Abuse finder ended with error %s', e)
            return False, _abuse_contact

        return True, _abuse_contact


if __name__ == '__main__':
    AbuseFinder().run('cnn.com')
