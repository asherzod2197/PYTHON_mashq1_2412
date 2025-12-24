sonlar = [3, 5, 3, 7, 8, 5, 10]

for i in range(len(sonlar)):
    if sonlar.count(sonlar[i]) == 1:
        print(sonlar[i])
