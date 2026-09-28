"""
Kullanilacak Yapilar:
-fastapi
-get endpoint
-post endpoint
-json body 
-pydantic model 
-response yapisi 
-hata kontrolu
-status code
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class HavaDurumVerisi(BaseModel):
    gun1: float
    gun2: float
    gun3: float

@app.get("/")
def home():
    return{
        "mesaj":"Hava Durumu Tahmin Servisi",
        "aciklama":"son 3 gunun sicaklik degerini gondererk ortalama tahmini yapar."
    }

@app.post("/hava-tahmin", status_code = status.HTTP_201_CREATED)
def hava_tahmini(veri: HavaDurumVerisi):
    for sicaklik in [veri.gun1, veri.gun2, veri.gun3]:
        if sicaklik < -50 or sicaklik > 60:
            raise HTTPException(
                status_code = 400,
                detail = "Sicaklik degeri -50 ile 60 arasinda olmalidir."
            )
    
    ortalama = (veri.gun1 + veri.gun2 + veri.gun3) / 3

    if ortalama < 10:
        tahmin = "hava soguk gibi"
    elif ortalama >= 10 and ortalama < 20:
        tahmin = "hava ilik"
    elif ortalama >= 20 and ortalama < 30:
        tahmin = "hava guzel"
    else:
        tahmin = "hava cok sicak"
    return{
        "durum":"basarili",
        "girilen_veriler":{
            "gun1":veri.gun1,
            "gun2":veri.gun2,
            "gun3":veri.gun3
        },
        "sonuc":{
            "ortalama_sicaklik":round(ortalama,2),
            "tahmin":tahmin,
            "tavsiye":"soguk hava icin kat kat giyin, ilik hava icin rahat giyinebilirsin, guzel hava icin keyfini cikar, cok sicak hava icin hafif giyinebilirsin"
        }
    }
        
    
    