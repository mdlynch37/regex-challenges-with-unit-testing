import hackerrank_regex_challenges as hr
import re
import unittest
from glob import iglob


class TestRegexMethods(unittest.TestCase):

    TESTCASE_FOLDER = './hackerrank-testcases'

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
        return (test_data if len(str(test_data)) < 80
                else ''.join([test_data[:73], ' ... ']))

    def format_failure_msg(self, test_input, output, output_expected):
        return ('\noutput: {}\nexpected: {}\nfor input: {}'
                .format(self.truncate_test_data(output),
                        self.truncate_test_data(output_expected),
                        self.truncate_test_data(test_input)))

    def test_is_valid_postal_re_module(self):
        testcase_folder = '/'.join([TestRegexMethods.TESTCASE_FOLDER,
                                    'validating-postalcode-testcases'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(hr.is_valid_postal_re_module(test_in))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_is_valid_postal_regex_module(self):
        testcase_folder = '/'.join([TestRegexMethods.TESTCASE_FOLDER,
                                    'validating-postalcode-testcases'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = str(hr.is_valid_postal_regex_module(test_in))
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_detect_html_tags(self):
        testcase_folder = '/'.join([TestRegexMethods.TESTCASE_FOLDER,
                                    'detect-html-tags-testcases'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = hr.detect_html_tags(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_is_valid_credit_card_num(self):
        testcase_folder = '/'.join([TestRegexMethods.TESTCASE_FOLDER,
                                    'validating-credit-card-number-testcases'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = hr.is_valid_credit_card_num(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

    def test_decode_matrix(self):
        testcase_folder = '/'.join([TestRegexMethods.TESTCASE_FOLDER,
                                    'matrix-script-testcases'])

        for fp_in, test_in, fp_out, test_out in self.read_testcases(
                testcase_folder):
            with self.subTest(filepath_in=fp_in, filepath_out=fp_out):
                output = hr.decode_matrix(test_in)
                self.assertEqual(output, test_out,
                                 msg=self.format_failure_msg(
                                     test_in, output, test_out))

if __name__ == '__main__':
    unittest.main()
