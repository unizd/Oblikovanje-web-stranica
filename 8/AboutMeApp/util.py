import validators

def provjeri_iban(broj_racuna):
	if not validators.iban(broj_racuna):
		return False
	else:
		return True