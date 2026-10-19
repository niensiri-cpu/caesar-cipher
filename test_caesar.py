
import unittest

from caesar import (
    encrypt,
    decrypt,
    brute_force,
    auto_crack,
    english_word_score
)


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt("HELLO", 3), "KHOOR")

    def test_decrypt(self):
        self.assertEqual(decrypt("KHOOR", 3), "HELLO")

    def test_wraparound(self):
        self.assertEqual(encrypt("XYZ", 3), "ABC")

    def test_lowercase(self):
        self.assertEqual(encrypt("hello", 3), "KHOOR")
        self.assertEqual(decrypt("khoor", 3), "HELLO")

    def test_punctuation(self):
        self.assertEqual(
            encrypt("HELLO WORLD!", 3),
            "KHOOR ZRUOG!"
        )

    def test_brute_force(self):
        results = brute_force("KHOOR")

        self.assertEqual(len(results), 26)
        self.assertEqual(results[3]["message"], "HELLO")
    
    def test_english_word_score(self):
        hello_score = english_word_score("HELLO")
        fake_score = english_word_score("WTAAD")

        self.assertGreater(hello_score, fake_score)

    def test_auto_crack(self):
        result = auto_crack("KHOOR")

        self.assertEqual(result["key"], 3)
        self.assertEqual(result["message"], "HELLO")



if __name__ == "__main__":
    unittest.main()
