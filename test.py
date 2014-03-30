import os
import time

from flask.ext.testing import TestCase as FlaskTestCase
from unittest import TestCase

from duchess import create_app
from utils import autocompiler


class ViewsTest(FlaskTestCase):

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


class AutocompilerTest(TestCase):
    @classmethod
    def setup_class(cls):
        with open('duchess/assets/css/test.sass', 'w') as sass_file:
            sass_file.write('$c = black\na\n  color: $c\n')
        autocompiler.watch_assets('duchess/assets')
        time.sleep(1)

    @classmethod
    def teardown_class(cls):
        os.remove('duchess/assets/css/test.sass')
        os.remove('duchess/assets/css/test.min.css')

    def test_autocompiler(self):
        with open('duchess/assets/css/test.sass', 'w') as sass_file:
            sass_file.write('$c = white\na\n  color: $c\n')
        time.sleep(1)

        with open('duchess/assets/css/test.min.css', 'r') as css_file:
            self.assertEqual(css_file.read(), 'a{color:white}')

        self.assertRaises(IOError, open, 'duchess/assets/css/test.sass.css')
