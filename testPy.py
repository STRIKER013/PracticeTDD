from FuncionesPY.isPrimePy import isPrime

#Fase 1: Prueba de Error
# def test_hellow():
 #   assert pruebaError()

#Fase 2 y 3: Prueba obvio y correcta
def test_hellow():
    return "Hello FastApi"

#Fase 1: Prueba error 
#def test_is_prime():
 #   assert isPrime("error") == False

#Fase 2: Prueba Obvia 
def test_isPrime():
    assert isPrime(2) == False