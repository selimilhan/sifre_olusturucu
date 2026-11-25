import random
karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]|;:',.<>?/`~"
sifre_uzunlugu = int(input("Şifre uzunluğunu girin: "))
sifre = ''.join(random.choice(karakterler) for i in range(sifre_uzunlugu))
print("Oluşturulan şifre:", sifre)  
