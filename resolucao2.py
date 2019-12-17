def trocar_vogais(vogal):

    vogal = vogal.replace("a","@")
    vogal = vogal.replace("e", "&")
    vogal = vogal.replace("i","!")
    vogal = vogal.replace("o", "#")
    vogal = vogal.replace("u", "*")

    return vogal

vogal = input("sua frase: ")

print(trocar_vogais(vogal))