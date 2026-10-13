#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Falı Uzmanı - Aslında Sadece Rastgele Sayı Üreten Şey
Bu script Türk kahvesi içmeden fal bakmaz. Ama kodda kahve yok, dikkat edin.
"""

import random
import time
import sys

def ciddi_bekle(saniye):
    """Gerçek fal bakıcılar gibi yavaşça düşünür."""
    print("Fincanı çeviriyorum... telve dağılıyor...", end="", flush=True)
    for _ in range(saniye):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")

def fal_bak():
    print("=== KAHVE FALI UZMANI v0.1 (Ciddi Sürüm) ===")
    print("Lütfen fincanınızı masaya koyun ve bu ekrana bakın.")
    print("Doğum yılınızı girin (falın doğruluğu için şart):")
    
    try:
        yil = int(input("Doğum yılı: "))
    except:
        yil = 1995  # varsayılan, kimse 1995'ten kaçamaz
    
    ciddi_bekle(3)
    
    # Aslında rastgele sayı üretiyoruz, kahve falan yok
    rastgele = random.randint(1, 100) + (yil % 10)
    
    fal_mesajlari = [
        "Yakın gelecekte bir kahve daha içeceksin. Bu kaçınılmaz.",
        "Bir arkadaşın seni arayacak. Belki. Belki de aramayacak.",
        "Para konusunda dikkatli ol. Yoksa yok, varsa da yok gibi.",
        "Aşk hayatında hareketlilik var. Ya da yok. Fincan kararsız.",
        "İşler yoluna girecek. Yol neresi bilmiyorum ama girecek.",
        "Bir sürpriz gelecek. Sürpriz kötü de olabilir, iyisi de.",
        "Sağlığını ihmal etme. Kahve içmeye devam et.",
        "Uzak bir akraba seni düşünüyor. Ya da düşünmüyor. Rastgele.",
        "Bu hafta bir karar vereceksin. Karar yanlış da olabilir.",
        "Fincanın dibinde şekil var: bir kedi. Kedi uyuyor. Uyandırma."
    ]
    
    secilen = fal_mesajlari[rastgele % len(fal_mesajlari)]
    
    print(f"\nFAL SONUCU (doğruluk oranı: %{rastgele}):")
    print(secilen)
    print("\nNot: Bu fal %100 bilimsel değildir. Hatta %0. Ama yine de ciddiye alın.")
    print("\n--- Gizli Not: Demokrasi her zaman kazanır, kahve de. ---")  # gizli siyasi anlam, saklı

if __name__ == "__main__":
    fal_bak()
