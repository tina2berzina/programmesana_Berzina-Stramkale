sastavdalas = ["Piens", "Milti", "Cukurs", "Pūdercukurs", "Eļļa", "Ūdens", "Krējums", "Sviests", "Brūnais cukurs", "Kakao", "Saldais krējums", "Sāls", "Sīrups", "Auzu pārslas", "Jogurts", "Kanēlis", "Cepamais pulveris", "Sausais raugs", "Medus"]

cups = {
    "piens": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "milti": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "cukurs": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "pūdercukurs": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "eļļa": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "ūdens": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "krējums": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "sviests": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "brūnais cukurs": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "kakao": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "saldais krējums": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "sāls": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "sīrups": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "auzu pārslas": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "jogurts": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "kanēlis": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"],
    "medus": ["1/4", "1/3", "2/3", "1/2", "3/4", "1", "1 1/4", "1 1/3", "1 2/3", "1 1/2", "1 3/4", "2"]
}


grami = {
    "piens": [62, 79, 158, 125, 187, 249, 311, 328, 407, 374, 436, 498],
    "milti": [30, 40, 80, 60, 90, 120, 150, 160, 200, 180, 210, 240],
    "cukurs": [50, 67, 134, 100, 150, 200, 250, 267, 334, 300, 350, 400],
    "pūdercukurs": [29, 38, 76, 58, 86, 115, 144, 152, 191, 173, 201, 230],
    "eļļa": [60, 80, 160, 118, 178, 237, 297, 317, 397, 355, 474],
    "ūdens": [32, 64, 128, 96, 160, 192, 224, 256, 320, 288, 352, 384],
    "krējums": [59, 79, 158, 119, 178, 237, 296, 316, 395, 356, 415, 474],
    "sviests": [58, 76, 152, 116, 174, 232, 290, 308, 384, 348, 406, 464],
    "brūnais cukurs": [55, 73, 146, 110, 165, 220, 275, 293, 366, 330, 385, 440],
    "kakao": [21, 28, 56, 43, 63, 85, 106, 113, 141, 128, 148, 170],
    "saldais krējums": [60, 80, 160, 120, 180, 240, 300, 320, 400, 360, 440, 480],
    "sāls": [71, 96, 192, 142, 213, 284, 355, 380, 476, 426, 497, 568],
    "sīrups": [85, 113, 226, 170, 255, 340, 425, 453, 566, 510, 595, 680],
    "auzu pārslas": [25, 33, 66, 50, 75, 100, 125, 133, 166, 150, 175, 200],
    "jogurts": [65, 86, 172, 130, 195, 260, 325, 346, 432, 390, 455, 520],
    "kanēlis": [33, 44, 88, 66, 99, 132, 165, 176, 220, 198, 231, 264],
    "medus": [85, 113, 226, 170, 255, 340, 425, 453, 566, 510, 595, 680]
    
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
