import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_arvoa_oikein(self):

        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):

        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        #nyt kortin saldo on 2
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_kortille_voi_ladara_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvo(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

#Tehtävässä 3 itse toteutetut testit alkavat tästä:

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        for i in range(0,3):
            self.kortti.syo_maukkaasti()
            #Kaksi ensimmäistä metodin syo_maukkaasti suoritusta antavat kortin saldoksi 2, sen jälkeen kolmas suoritus ei vähennä saldoa!
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_negatiivisen_summan_lataaminen_ei_muuta_kortin_saldoa(self):
        self.kortti.lataa_rahaa(-1)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_rahat_riittavat_edulliseen(self):
        kortti2 = Maksukortti(2.5)
        kortti2.syo_edullisesti()
        self.assertEqual(str(kortti2), "Kortilla on rahaa 0.0 euroa") #Näyttää siltä, että kortin alkusaldon ollessa 2.5 saldo on tyyppiä double jatkossa?

    def test_rahat_riittavat_maukkaaseen(self):
        kortti3 = Maksukortti(4)
        kortti3.syo_maukkaasti()
        self.assertEqual(str(kortti3), "Kortilla on rahaa 0 euroa") 
