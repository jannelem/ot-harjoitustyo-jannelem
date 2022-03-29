import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		paate = Kassapaate()
    
	def test_luodun_kassapaatteen_saldo_oikein(self):
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
  
	def test_luodun_kassapaatteen_edulliset_oikein(self):
		self.assertEqual(self.paate.edulliset, 0)
    
	def test_luodun_kassapaatteen_edulliset_oikein(self):
		self.assertEqual(self.paate.maukkaat, 0)

	def test_edullinen_kateisella_kasvattaa_saldoa(self):
		self.paate.syo_edullisesti_kateisella(500)
		self.assertEqual(self.paate.kassassa_rahaa(100240)

	def test_edullinen_kateisella_vaihtoraha_oikein(self):
 		assertEqual(self.paate.syo_edullisesti_kateisella(500), 260)

	def test_maukkaasti_kateisella_kasvattaa_saldoa(self):
		self.paate.syo_maukkaasti_kateisella(500)
		self.assertEqual(self.paate.kassassa_rahaa, 100500)
	
	def test_maukkaasti_kateisella_vaihtoraha_oikein(self):
		assertEqual(self.paate.syo_maukkaasti_kateisella(500), 100)
