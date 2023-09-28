import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_0(self):
        input = "123"
        expected = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 100))
    def test_1(self):
        input = "\"123\k Hi\""
        expected = "Illegal Escape In String: 123\k"
        self.assertTrue(TestLexer.test(input, expected, 101))
    def test_2(self):
        input = "\"123 Hi\""
        expected = "123 Hi,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 102))
    
    def test_3(self):
        input = """ "print \\"Hello, World!\\"" """
        expected = "print \"Hello, World!\",<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 103))

    def test_4(self):
        input = """ "Hello \q World!" """
        expected = "Illegal Escape In String: Hello \q"
        self.assertTrue(TestLexer.test(input, expected, 104))
    
    def test_5(self):
        input = """ "He asked me: \\"Where is John?\\"" """
        expected = "He asked me: \"Where is John?\",<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 105))

    def test_6(self):
        input = "He asked me: \"Where is John?\""
        expected = "He,asked,me,:,Where is John?,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 106))

    def test_7(self):
        input = """ He asked me: \"Where is John? """
        expected = "He asked me: \"Where is John?\",<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 107))

    def test_8(self):
        input = "\"dkjoiue\\s\""
        expected = "Illegal Escape In String: dkjoiue\s"
        self.assertTrue(TestLexer.test(input, expected, 108))