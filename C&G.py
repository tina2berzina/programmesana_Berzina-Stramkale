sastavdalas = ["Piens,", "Milti,", "Cukurs,", "Pūdercukurs,", "Eļļa,", "Ūdens,", "Krējums,", "Sviests,", "Brūnais cukurs,", "Kakao,", "Saldais krējums,", "Sāls,", "Sīrups,", "Auzu pārslas,", "Jogurts,", "Kanēlis,", "Cepamais pulveris,", "Sausais raugs,", "Medus"]

cups = {
    "piens": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "milti": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "cukurs": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "pūdercukurs": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "eļļa": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "ūdens": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "krējums": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "sviests": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "brūnais cukurs": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "kakao": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "saldais krējums": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "sāls": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "sīrups": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "auzu pārslas": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "jogurts": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "kanēlis": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "medus": ["1/4", "1/3", "2/3", "1/2", "3/4", "1"]
}

grami = {
    "piens": [62, 79, 158, 125, 187, 249],
    "milti": [30, 40, 80, 60, 90, 120],
    "cukurs": [50, 67, 134, 100, 150, 200],
    "pūdercukurs": [29, 38, 76, 58, 86, 115],
    "eļļa": [60, 80, 160, 118, 178, 237],
    "ūdens": [32, 64, 128, 96, 160, 192],
    "krējums": [59, 79, 158, 119, 178, 237],
    "sviests": [58, 76, 152, 116, 174, 232],
    "brūnais cukurs": [55, 73, 146, 110, 165, 220],
    "kakao": [21, 28, 56, 43, 63, 85,],
    "saldais krējums": [60, 80, 160, 120, 180, 240],
    "sāls": [71, 96, 192, 142, 213, 284],
    "sīrups": [85, 113, 226, 170, 255, 340],
    "auzu pārslas": [25, 33, 66, 50, 75, 100],
    "jogurts": [65, 86, 172, 130, 195, 260],
    "kanēlis": [33, 44, 88, 66, 99, 132],
    "medus": [85, 113, 226, 170, 255, 340]
    
}

mililitri = {
    "piens": [],
    "eļļa": [],
    "ūdens": [],
    "krējums": [],
    "saldais krējums": [],
    "sīrups": [],
    "jogurts": [],
    "medus": []
    
}
print("                       C&G")
print("Programma pārveido receptes sastāvdaļas no ASV mērvienībām uz gramiem vai mililitriem.")
print("Sastāvdaļas: ")
midpoint = len(sastavdalas) // 2
first_half = sastavdalas[:midpoint]
second_half = sastavdalas[midpoint:]
print(" ".join(first_half))
print(" ".join(second_half))
print()

n = int(input("Cik Jums ir sastāvdaļas? - "))
for i in range(n):
    s = input("Sastāvdaļa: ")
    if s not in cups:
        print("Nederīga sastāvdaļa")
        continue
    
    sm = input("Sākotnējā mērvienība (cups): ")
    if sm not in cups[s]:
        print("Nederīga mērvienība")
        continue
    
    vm = input("Vēlamā mērvienība (g vai ml): ")
    
    b = cups[s].index(sm)
    if vm == "g":
        print(grami[s][b], "grami")
    elif vm == "ml":
        if s in mililitri:
            print(mililitri[s][b], "mililitri")
        else:
            print("Šī sastāvdaļa nevar tikt pārveidota uz mililitriem")
    else:
        print("Nederīga mērvienība")
