import googlefinance
import unittest
from urllib2 import URLError

class TestQuotes(unittest.TestCase):

    def test_one_symbol(self):
        appl = googlefinance.getQuotes('GOOG')[0]
        self.assertEqual(appl["Index"], "NASDAQ")
        self.assertEqual(appl["StockSymbol"], "GOOG")

    def test_symbols(self):
        quotes = googlefinance.getQuotes(['GOOG', 'VIE:BKS'])
        self.assertEqual(quotes[0]["Index"], "NASDAQ")
        self.assertEqual(quotes[0]["StockSymbol"], "GOOG")
        self.assertEqual(quotes[1]["Index"], "VIE")
        self.assertEqual(quotes[1]["StockSymbol"], "BKS")

    def test_timeout(self):
        # ensure timeout will always happen
        googlefinance.setTimeout(0.0001)
        with self.assertRaisesRegexp(URLError, 'timed out'):
            googlefinance.getQuotes(['GOOG'])

        # reset timeout (for other tests)
        googlefinance.setTimeout(googlefinance.DEFAULT_TIMEOUT)

if __name__ == '__main__':
    unittest.main()
