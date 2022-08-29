anapara = 1000 # Dolar
k_pay = 7 # yüzde kar payı
g_kar_yüz = 1+(k_pay/100)

toplam = anapara + anapara*g_kar_yüz   # 1. günün bakiyesi
toplam = toplam + anapara*g_kar_yüz   # 2. günün bakiyesi
toplam = toplam + anapara*g_kar_yüz   # 3. günün bakiyesi
toplam = toplam + anapara*g_kar_yüz   # 4. günün bakiyesi
toplam = toplam + anapara*g_kar_yüz   # 5. günün bakiyesi
toplam = toplam + anapara*g_kar_yüz   # 6. günün bakiyesi
toplam = toplam + anapara*g_kar_yüz   # 7. günün bakiyesi

print(toplam)