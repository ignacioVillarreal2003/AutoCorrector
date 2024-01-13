from autocorrect import Speller

corrector = Speller(lang='es')

def corregir_Frase(frase):
    if not corrector(frase) == frase:
        return corrector(frase)
    else:
        return  frase

print(corregir_Frase(input('Frase a corregir: ')))