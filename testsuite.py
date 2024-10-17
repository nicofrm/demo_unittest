import unittest
import HtmlTestRunner

from myproject_unittest.login_testcases import Login_page_verification

class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Login_page_verification))

        runner = HtmlTestRunner.HTMLTestRunner\
                (
            combine_reports=True,
            report_title="Testele Noastre",
            report_name="Regression"
        )
        runner.run(teste_de_rulat)