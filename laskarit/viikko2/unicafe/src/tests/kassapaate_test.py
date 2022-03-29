import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.paate = Kassapaate()
		self.rahakas_kortti = Maksukortti(1000)
		self.koyhan_kortti = Maksukortti(100)
    
	def test_luodun_kassapaatteen_saldo_oikein(self):
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
  
	def test_luodun_kassapaatteen_edulliset_oikein(self):
		self.assertEqual(self.paate.edulliset, 0)
    
	def test_luodun_kassapaatteen_edulliset_oikein(self):
		self.assertEqual(self.paate.maukkaat, 0)

	def test_edullinen_kateisella_kasvattaa_kassaa(self):
		self.paate.syo_edullisesti_kateisella(500)
		self.assertEqual(self.paate.kassassa_rahaa, 100240)

	def test_edullinen_kateisella_vaihtoraha_oikein(self):
 		self.assertEqual(self.paate.syo_edullisesti_kateisella(500), 260)

	def test_maukkaasti_kateisella_kasvattaa_kassaa(self):
		self.paate.syo_maukkaasti_kateisella(500)
		self.assertEqual(self.paate.kassassa_rahaa, 100400)
	
	def test_maukkaasti_kateisella_vaihtoraha_oikein(self):
		self.assertEqual(self.paate.syo_maukkaasti_kateisella(500), 100)
	
	def test_edullisesti_kateisella_palauttaa_kaiken(self):
		self.assertEqual(self.paate.syo_edullisesti_kateisella(200), 200)

	def test_maukkaasti_kateisella_palauttaa_kaiken(self):
		self.assertEqual(self.paate.syo_maukkaasti_kateisella(200), 200)

	def test_edullisesti_kateisella_ei_muuta_saldoa(self):
		self.paate.syo_edullisesti_kateisella(200)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)

	def test_maukkaasti_kateisella_ei_muuta_saldoa(self):
		self.paate.syo_maukkaasti_kateisella(200)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)

	def test_edullisesti_kateisella_ei_muuta_maaraa(self):
		self.paate.syo_edullisesti_kateisella(200)
		self.assertEqual(self.paate.edulliset, 0)

	def test_maukkaasti_kateisella_ei_muuta_maaraa(self):
			self.paate.syo_maukkaasti_kateisella(200)
			self.assertEqual(self.paate.maukkaat, 0)

	def test_syo_edullisesti_kortilla_palauttaa_True(self):
		self.assertEqual(self.paate.syo_edullisesti_kortilla(self.rahakas_kortti), True)

	def test_syo_edullisesti_kortilla_vahentaa_kortin_saldoa(self):
		self.paate.syo_edullisesti_kortilla(self.rahakas_kortti)
		self.assertEqual(str(self.rahakas_kortti), "saldo: 7.6")
	
	def test_syo_edullisesti_kortilla_kasvattaa_maaraa(self):
		self.paate.syo_edullisesti_kortilla(self.rahakas_kortti)
		self.assertEqual(self.paate.edulliset, 1)
	
	def test_syo_edullisesti_kortilla_ei_kasvata_kassaa(self):
		self.paate.syo_edullisesti_kortilla(self.rahakas_kortti)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
	
	def test_syo_edullisesti_kortilla_palauttaa_false_jos_saldo_liian_pieni(self):
		self.assertEqual(self.paate.syo_edullisesti_kortilla(self.koyhan_kortti), False)
	
	def test_syo_edullisesti_kortilla_ei_kasvata_kassaa_jos_saldo_liian_pieni(self):
		self.paate.syo_edullisesti_kortilla(self.koyhan_kortti)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)

	def test_syo_edullisesti_kortilla_ei_kasvata_maaraa_jos_saldo_liian_pieni(self):
		self.paate.syo_edullisesti_kortilla(self.koyhan_kortti)
		self.assertEqual(self.paate.edulliset, 0)
	
	def test_syo_maukkaasti_kortilla_vahentaa_kortin_saldoa(self):
		self.paate.syo_maukkaasti_kortilla(self.rahakas_kortti)
		self.assertEqual(str(self.rahakas_kortti), "saldo: 6.0")
	
	def test_syo_maukkaasti_kortilla_kasvattaa_maaraa(self):
		self.paate.syo_maukkaasti_kortilla(self.rahakas_kortti)
		self.assertEqual(self.paate.maukkaat, 1)
	
	def test_syo_maukkaasti_kortilla_ei_kasvata_kassaa(self):
		self.paate.syo_maukkaasti_kortilla(self.rahakas_kortti)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
	
	def test_syo_maukkaasti_kortilla_palauttaa_false_jos_saldo_liian_pieni(self):
		self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.koyhan_kortti), False)
	
	def test_syo_maukkaasti_kortilla_ei_kasvata_kassaa_jos_saldo_liian_pieni(self):
		self.paate.syo_maukkaasti_kortilla(self.koyhan_kortti)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)

	def test_syo_maukkaasti_kortilla_ei_kasvata_maaraa_jos_saldo_liian_pieni(self):
		self.paate.syo_maukkaasti_kortilla(self.koyhan_kortti)
		self.assertEqual(self.paate.maukkaat, 0)
	
	def test_syo_edullisesti_kortilla_ei_muuta_saldoa_jos_saldo_liian_pieni(self):
		self.paate.syo_edullisesti_kortilla(self.koyhan_kortti)
		self.assertEqual(str(self.koyhan_kortti), "saldo: 1.0")
	
	def test_syo_maukkaasti_kortilla_ei_muuta_saldoa_jos_saldo_liian_pieni(self):
		self.paate.syo_maukkaasti_kortilla(self.koyhan_kortti)
		self.assertEqual(str(self.koyhan_kortti), "saldo: 1.0")

	def test_rahan_lataaminen_kasvattaa_kortin_saldoa(self):
		self.paate.lataa_rahaa_kortille(self.koyhan_kortti, 300)
		self.assertEqual(str(self.koyhan_kortti), "saldo: 4.0")

	def test_rahan_lataaminen_kasvattaa_kassaa(self):
		self.paate.lataa_rahaa_kortille(self.koyhan_kortti, 300)
		self.assertEqual(self.paate.kassassa_rahaa, 100300)
	
	def test_negatiivinen_lataus_ei_muuta_kortin_saldoa(self):
		self.paate.lataa_rahaa_kortille(self.koyhan_kortti, -100)
		self.assertEqual(str(self.koyhan_kortti), "saldo: 1.0")
	
	def test_negatiivinen_lataus_ei_kasvata_kassaa(self):
		self.paate.lataa_rahaa_kortille(self.koyhan_kortti, -100)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)