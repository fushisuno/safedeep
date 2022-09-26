import pyrebase
import re
config = {
  "apiKey": "AIzaSyAfJZyTi1WtVKy62SytAGbQyd2TaPCWn6A",
  "authDomain": "safedeep-9c030.firebaseapp.com",
  "databaseURL": "https://safedeep-9c030-default-rtdb.firebaseio.com",
  "projectId": "safedeep-9c030",
  "storageBucket": "safedeep-9c030.appspot.com",
  "messagingSenderId": "325692084824",
  "appId": "1:325692084824:web:3ce03fcce1a9fd2286f02d"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
u = int(input())
nome = ["Avira", "Norton", "AVG"]
for i in range(0, len(nome)):
    dados = {"Nome": nome[i], "Tipo": "Anti-Span", "Title": "Ferramentas  Anti-Span", "Descricao": "Ferramenta de anti-virus, usada para proteger, detectar, impedir, previnir e realizar a remoção de softwares maliciosos, vírus e worms.", "Id_media": u}
    u += 1
    db.child("ferramentas").child("antivirus").child(db.generate_key()).set(dados)
