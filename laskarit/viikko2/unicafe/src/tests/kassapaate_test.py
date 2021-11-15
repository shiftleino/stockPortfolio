import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase): 
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_alku_raha_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alku_lounaat(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_kateisosto_edulliset_laskuri(self): 
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_edulliset_saldo(self): 
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)

    def test_kateisosto_edulliset_vaihto(self): 
        vaihto = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihto, 250-240)
    
    def test_kateisosto_epaonnistui_edulliset_laskuri(self): 
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_epaonnistui_edulliset_saldo(self): 
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_epaonnistui_edulliset_vaihto(self): 
        vaihto = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihto, 200)

    def test_kateisosto_maukkaat_laskuri(self): 
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_maukkaasti_saldo(self): 
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)

    def test_kateisosto_maukkaasti_vaihto(self): 
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihto, 450-400)
    
    def test_kateisosto_epaonnistui_maukkaat_laskuri(self): 
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_epaonnistui_maukkaasti_saldo(self): 
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_epaonnistui_maukkaasti_vaihto(self): 
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihto, 300)
    
    def test_kortilla_tarpeeksi_rahaa_edullisesti_veloitus(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 600")  

    def test_kortilla_tarpeeksi_rahaa_maukas_palautusarvo(self):
        result = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(result, True)

    def test_kortilla_tarpeeksi_rahaa_myydyt_lounaat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_ei_tarpeeksi_rahaa_veloitus(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 200")

    def test_kortilla_ei_tarpeeksi_rahaa_palautusarvo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        result = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(result, False)

    def test_kortilla_ei_tarpeeksi_rahaa_myydyt_lounaat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 4)

    def test_kortilla_ostettaessa_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_saldon_lataus_kassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortin_saldo_lataus_nega_kassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)