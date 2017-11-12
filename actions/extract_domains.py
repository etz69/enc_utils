from tld import get_tld

from st2actions.runners.pythonrunner import Action


class ExtractDomains(Action):
    def __init__(self, config=None):
        super(ExtractDomains, self).__init__(config=config)

    def run(self, input_text):
        self.logger.info('TLD extractor called')
        _tlds = []

        domain = input_text.split("//")[-1].split("/")[0]
        try:
            res = get_tld(domain, as_object=True, fix_protocol=True)
            tld = res.tld
            _tlds.append(tld)
        except Exception as e:
            self.logger.error('TLD extractor ended with error')
            return False, _tlds

        return True, _tlds
