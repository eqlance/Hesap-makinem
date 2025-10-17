# calculator.py
print("🧮 Basit Hesap Makinesi")
print("----------------------")

# Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı gir: "))
sayi2 = float(input("İkinci sayıyı gir: "))

# İşlem seçimi
print("Yapmak istediğin işlemi seç:")
print("1. Toplama (+)")
print("2. Çıkarma (-)")
print("3. Çarpma (*)")
print("4. Bölme (/)")

secim = input("Seçimin (1/2/3/4): ")

# İşleme göre sonucu hesapla
if secim == "1":
    sonuc = sayi1 + sayi2
    print(f"Sonuç: {sayi1} + {sayi2} = {sonuc}")
elif secim == "2":
    sonuc = sayi1 - sayi2
    print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
elif secim == "3":
    sonuc = sayi1 * sayi2
    print(f"Sonuç: {sayi1} * {sayi2} = {sonuc}")
elif secim == "4":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print(f"Sonuç: {sayi1} / {sayi2} = {sonuc}")
    else:
        print("Hata: Sıfıra bölme yapılamaz!")
else:
    print("Geçersiz seçim yaptın ❌")
    