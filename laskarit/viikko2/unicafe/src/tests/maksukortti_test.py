import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_tiedot_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10")
    
    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 30")
    
    def test_rahan_ottaminen_kun_saldoa(self):
        self.maksukortti.ota_rahaa(6)
        self.assertEqual(str(self.maksukortti), "saldo: 4")

    def test_rahan_ottaminen_kun_ei_saldoa(self):
        self.maksukortti.ota_rahaa(30)
        self.assertEqual(str(self.maksukortti), "saldo: 10")

    def test_ottaminen_toimii_palautusarvo(self):
        result = self.maksukortti.ota_rahaa(6)
        self.assertEqual(result, True)

    def test_ottaminen_ei_toimi_palautusarvo(self):
        result = self.maksukortti.ota_rahaa(30)
        self.assertEqual(result, False)    