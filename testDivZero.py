from urllib.parse import _NetlocResultMixinStr
import functions as functions


res = functions.division(5,0)

if res == "Erro. Divisão impossível":
    print("Passed!")
else:
    print("Something is wrong...")