from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class KullaniciBilgisi(BaseModel):
    ad: str
    yas: int
    sehir: str

@app.get("/")
def home():
    return {"mesaj": "fastapi uygulama"}

# @app.get("/urun/{urun_id}")
# def urun_getir(urun_id: int):
#     return {
#         "mesaj": "path parametresi ile urun getirildi",
#         "urun_id": urun_id
#     }

@app.get("/arama")
def arama_yap(kelime:str):
    return {
        "mesaj": "query parametresi ile arama yapildi",
        "aranan_kelime": kelime
    }

@app.post("/kullanici", status_code = status.HTTP_201_CREATED)
def kullanici_ekle(kullanici:KullaniciBilgisi):
    return{
        "durum": "basarili",
        "mesaj": "kullanici basariyla eklendi",
        "veri": {
            "ad": kullanici.ad,
            "yas": kullanici.yas,
            "sehir": kullanici.sehir
        }
    }


@app.get("/urun/{urun_id}")
def urun_getir(urun_id:int):
    if urun_id != 1:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "urun bulunamadi"
        )
    
    return{
        "durum": "basarili",
        "mesaj": "urun bulundu",
        "veri":{
            "urun_id": urun_id
        }
    }

