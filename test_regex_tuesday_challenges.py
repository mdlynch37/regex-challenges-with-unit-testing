import regex_tuesday_challenges as rt
import re
import unittest
from glob import iglob

class TestRegexTuesdayFunctions(unittest.TestCase):

    TESTCASE_FOLDER = './regex-tuesdays-testcases'

    def generate_tc_filepathes(self, testcase_folder):
        """
        Yields tuple of filepathes for txt files with test input
        and expected output data
        """

        testcase_folder = (testcase_folder[:-1] if testcase_folder[-1] == '/'
                           else testcase_folder)
        fp_pattern_in = '/'.join([testcase_folder, 'input/input*.txt'])
        fp_pattern_out = '/'.join([testcase_folder, 'output/output*.txt'])

        for fp_in, fp_out in zip(iglob(fp_pattern_in),
                                 iglob(fp_pattern_out)):
            yield fp_in, fp_out

    def read_testcases(self, testcase_folder):
        """
        Yields tuple of test input data and expected output data
        read from files with validated format like 'input00.txt' and
        'output00.txt' with suffix values being a variable number of digits
        that match input file to output file.
        """

        for fp_in, fp_out in self.generate_tc_filepathes(testcase_folder):
            # check that test filenames are in correct format
            assert re.search(r'input[0-9]+\.txt$', fp_in), (
                   'Incorrect input file name format: {}'.format(fp_in))
            assert re.search(r'output[0-9]+\.txt$', fp_out), (
                   'Incorrect output file name format: {}'.format(fp_out))
            # check input and output file suffixes match
            assert fp_in.split('input')[-1] == fp_out.split('output')[-1], (
                'Input and output file suffixes do not match...'
                '\nin: {} \nout: {}'.format(fp_in, fp_out))

            with open(fp_in) as fi_in:
                with open(fp_out) as fi_out:
                    yield (fp_in, fi_in.read(), fp_out, fi_out.read())

    def truncate_test_data(self, test_data):
        """Truncates test input or expected output data for failure message"""
        return (test_data if len(str(test_data)) < 200
                else ''.join([test_data[:73], ' ... ']))

    def format_failure_msg(self, test_input, output, output_expected):
        return ('\noutput:\n{}\nexpected:\n{}\nfor input:\n{}'
                .format(self.truncate_test_data(output),
                        self.truncate_test_data(output_expected),
                        self.truncate_test_data(test_input)))

    def test_highlight_repeat_words(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge01'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = rt.highlight_repeat_words(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_match_css_grayscale(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge02'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_css_grayscale(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_match_valid_date(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge03'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_valid_date(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_md_italics_to_html(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge04'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = rt.md_italics_to_html(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_match_valid_nums(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge05'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_valid_nums(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_match_valid_ipv4(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge06'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_valid_ipv4(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_match_valid_domain(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge07'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_valid_domain(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))


    def test_highlight_repeat_list_items(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge08'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = rt.highlight_repeat_list_items(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_md_links_to_html(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge09'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = rt.md_links_to_html(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_tokenize_text(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge10'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = rt.tokenize_text(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))


    def test_match_alpha_ascending(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge11'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_alpha_ascending(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_fix_whitespace(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge12'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = rt.fix_whitespace(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_match_chem_elements(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge14'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_chem_elements(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_match_valid_js_regex(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge17'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_valid_js_regex(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_match_irc_message(self):
        testcase_folder = '/'.join([TestRegexTuesdayFunctions.TESTCASE_FOLDER,
                                    'challenge18'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(bool(rt.match_irc_message(test_in)))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

if __name__ == '__main__':
    unittest.main()
