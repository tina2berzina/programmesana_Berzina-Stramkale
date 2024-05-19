sastavdalas = ["Piens", "Milti", "Cukurs", "Pūdercukurs", "Eļļa", "Ūdens", "Krējums", "Sviests", "Brūnais cukurs", "Kakao", "Saldais krējums", "Sāls", "Sīrups", "Auzu pārslas", "Jogurts", "Kanēlis", "Cepamais pulveris", "Sausais raugs", "Medus"]

cups = {
    "piens": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "milti": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "cukurs": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "pūdercukurs": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "eļļa": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "ūdens": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "krējums": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "sviests": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "brūnais cukurs": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "kakao": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "saldais krējums": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "sāls": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "sīrups": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "auzu pārslas": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "jogurts": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "kanēlis": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "cepamais pulveris": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "sausais raugs": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"],
    "medus": ["tsp", "tbsp", "1/4", "1/3", "2/3", "1/2", "3/4", "1"]
}

grami = {
    "piens": [5, 15, 62, 79, 158, 125, 187, 249],
    "milti": [3, 8, 30, 40, 80, 60, 90, 120],
    "cukurs": [4, 13, 50, 67, 134, 100, 150, 200],
    "pūdercukurs": [3, 8, 29, 38, 76, 58, 86, 115],
    "eļļa": [5, 15, 60, 80, 160, 118, 178, 237],
    "ūdens": [5, 15, 32, 64, 128, 96, 160, 192],
    "krējums": [5, 15, 59, 79, 158, 119, 178, 237],
    "sviests": [5, 14, 58, 76, 152, 116, 174, 232],
    "brūnais cukurs": [5, 13, 55, 73, 146, 110, 165, 220],
    "kakao": [3, 9, 21, 28, 56, 43, 63, 85,],
    "saldais krējums": [5, 15, 60, 80, 160, 120, 180, 240],
    "sāls": [6, 18, 71, 96, 192, 142, 213, 284],
    "sīrups": [7, 21, 85, 113, 226, 170, 255, 340],
    "auzu pārslas": [3, 10, 25, 33, 66, 50, 75, 100],
    "jogurts": [5, 15, 65, 86, 172, 130, 195, 260],
    "kanēlis": [4, 8, 33, 44, 88, 66, 99, 132],
    "cepamais pulveris": [4, 14, 56, 75, 150, 112, 168, 224],
    "sausais raugs": [3, 9, 36, 48, 96, 72, 108, 144],
    "medus": [7, 21, 85, 113, 226, 170, 255, 340]
    
}

print("Programma pārveido receptes sastāvdaļas no ASV mērvienībām uz gramiem")
print("Sastāvdaļas: ")
for sastavdala in sastavdalas:
    print(sastavdala)
    
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
    
    b = cups[s].index(sm)
    print(grami[s][b], "grami")
