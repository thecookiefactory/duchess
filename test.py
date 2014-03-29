from flask.ext.testing import TestCase

from duchess import create_app


class ViewsTest(TestCase):

    def create_app(self):
        duchess = create_app()
        return duchess

    def test_app(self):
        from flask import Flask
        duchess = self.create_app()
        print(duchess.config)
        self.assertIsInstance(duchess, Flask)
        self.assertTrue(duchess.testing)

    def test_index(self):
        r = self.client.get('/')
        self.assert_200(r)

    def test_asdf(self):
        r = self.client.get('/asdf/')
        self.assert_404(r)
