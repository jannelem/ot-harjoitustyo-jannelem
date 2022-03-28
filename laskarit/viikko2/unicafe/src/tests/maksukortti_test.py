import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")

    def test_rahan_ottaminen_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(900), True)
    
    def test_rahan_ottaminen_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
    
    def test_rahan_ottaminen_palauttaa_false_jos_saldo_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1001), False)
    
    def test_rahan_ottaminen_ei_muuta_saldoa_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(1001)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")