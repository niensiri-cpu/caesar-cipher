
import unittest

from caesar import encrypt, decrypt, brute_force


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


if __name__ == "__main__":
    unittest.main()
