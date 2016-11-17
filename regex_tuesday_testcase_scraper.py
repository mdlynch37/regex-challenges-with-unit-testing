from glob import iglob
import os
import re

class RegexTuesdayTestcaseScraper():

    HTML_ENTITIES = [(r'&lt;', r'<'), (r'&gt;', r'>')]

    def __init__(self, filepath_to_html):
        # extract and format title of challenge
        html_title = filepath_to_html.split('/')[-1].split('.')[0]
        self.title = re.sub(r'(?<=\D)(\d)$', r'0\1', html_title)

        with open(filepath_to_html) as f:
            self.challenge_html = f.read()

        # extract number of tests given in html file
        re_n_tests = re.compile(r'id=\'passed-count\'>0</span>/([0-9]+)\)')
        self.n_tests = int(re_n_tests.search(self.challenge_html).group(1))

    def _replace_html_ents(self, test_data):
        for entity, repl in RegexTuesdayTestcaseScraper.HTML_ENTITIES:
            test_data = re.sub(entity, repl, test_data)
        return test_data

    def _extract_test_values(self):
        """
        Yields test input and output pairs as tuples,
        html entities in the data replaced withproper characters.
        """
        for test_data in re.finditer(r'<dt>(.*)</dt><dd>(.*)</dd>',
                                     self.challenge_html):
            yield (self._replace_html_ents(test_data.group(1)),
                   self._replace_html_ents(test_data.group(2)))

    def save_test_data(self, save_dir='./'):
        save_dir = save_dir[:-1] if save_dir[-1] == '/' else save_dir

        # construct destination file path and create directories as needed
        dir_in = '/'.join([save_dir, self.title, 'input'])
        dir_out = '/'.join([save_dir, self.title, 'output'])
        os.makedirs(dir_in, exist_ok=True)
        os.makedirs(dir_out, exist_ok=True)

        test_cnt = 0  # for validation
        for test_in, test_out in self._extract_test_values():
            fp_in = '/'.join([dir_in, 'input{0:03d}.txt'.format(test_cnt)])
            fp_out = '/'.join([dir_out, 'output{0:03d}.txt'.format(test_cnt)])
            with open(fp_in, 'w') as f_in:
                with open(fp_out, 'w') as f_out:
                    f_in.write(test_in)
                    f_out.write(test_out)
            test_cnt += 1
        assert self.n_tests == test_cnt, (
            'for {} expected {} tests, saved {}'
            .format(self.title, self.n_tests, test_cnt))

    def test_data(self):
        """Returns list of tuples of test input and output data."""
        return list(self._extract_test_values())


if __name__ == '__main__':

    PATH_TO_PAGES = './regex-tuesday-gh-pages/'

    log = []
    for fp in iglob(''.join([PATH_TO_PAGES, 'challenge*.html'])):
        scraper = RegexTuesdayTestcaseScraper(fp)
        scraper.save_test_data('./regex-tuesdays-testcases')
        log.append((scraper.title, scraper.n_tests))

    for title, n_tests in sorted(log):
        print('{0}: {1:>3} tests saved'.format(title, n_tests))