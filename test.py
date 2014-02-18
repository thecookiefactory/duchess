from flask.ext.testing import TestCase, Twill

from duchess import duchess


class ViewsTest(TestCase):

    def create_app(self):
        return duchess

    def test_index(self):
        with Twill(self.app, port=3000) as t:
            t.browser.go(t.url('/'))
            self.assertEqual(t.browser.get_code(), 200)

    def test_asdf(self):
        with Twill(self.app, port=3000) as t:
            t.browser.go(t.url('/asdf/'))
            self.assertEqual(t.browser.get_code(), 404)
