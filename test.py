from flask.ext.testing import TestCase
import urllib2

from duchess import duchess


class ViewsTest(TestCase):

    def create_app(self):
        return duchess

    def test_index(self):
        r = urllib2.urlopen('http://localhost:5000/')
        self.assert_200(r)
        r = urllib2.urlopen('http://localhost:5000')
        self.assert_200(r)

    def test_asdf(self):
        r = urllib2.urlopen('http://localhost:5000/asdf/')
        self.assert_404(r)
