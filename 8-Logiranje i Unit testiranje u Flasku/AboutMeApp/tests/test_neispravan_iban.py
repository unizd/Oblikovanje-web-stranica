from .. import util

def test_neispravan_iban():
	
	racun = "HR123456789"	
	response = util.provjeri_iban(racun)
	
	assert response == False
