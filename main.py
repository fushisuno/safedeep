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


pagin = "tools"
tool_lik = list()
tools = list()
lista_tool = list()
usersAll = db.child("users").get()

for i in usersAll.each():
    user = i.val()
    user_valid = user['Email']
    try:
        den = db.child("users").child(i.key()).child("ferramentas_curtidas").get()
        qtd_den = den.val()
        if qtd_den != None:
            for fishy_den in den.each():
                nun = fishy_den.key()
                tool_lik.append(nun)
    except:
        tool_lik = list()
liked_fh = False       
usersAll = db.child("ferramentas").child("antimalware").get()
for ferramenta in usersAll.each():
    tool = ferramenta.val()
    if len(tool_lik) > 0:
        if ferramenta.key() in tool_lik:
                liked_fh = True
        else:
            liked_fh = False 
    dict_tools = {"Nome": tool["Nome"], "Tipo": tool["Tipo"], "Title":  tool["Title"], "Descricao":  tool["Descricao"], "Media_img": "card_media_" + str(tool["Id_media"]), "ID_Tool": "" + ferramenta.key()}
    dict_tools["Tool_liked"] = liked_fh
    lista_tool.append(dict_tools)
dic_tip = {"Tipo_tool": " Anti-Malware", "Valor": lista_tool, "Class_id": "malware"}

tools.append(dic_tip)

lista_tool = list()
liked_fh = False   
usersAll = db.child("ferramentas").child("antivirus").get()
for ferramenta in usersAll.each():
    tool = ferramenta.val()
    if len(tool_lik) > 0:
        if ferramenta.key() in tool_lik:
                liked_fh = True
        else:
            liked_fh = False 
    dict_tools = {"Nome": tool["Nome"], "Tipo": tool["Tipo"], "Title":  tool["Title"], "Descricao":  tool["Descricao"], "Media_img": "card_media_" + str(tool["Id_media"]), "ID_Tool": "" + ferramenta.key()}
    dict_tools["Tool_liked"] = liked_fh
    lista_tool.append(dict_tools)
dic_tip = {"Tipo_tool": " Anti-virus", "Valor": lista_tool, "Class_id": "antivirus"}
tools.append(dic_tip)




'''
users = list()
denun = list()
usersFish = db.child("denuncias").get()
usersAll = db.child("users").get()
for i in usersAll.each():
    user = i.val()
    user_valid = user['Email']
    den = db.child("users").child(i.key()).child("denuncias_curtidas").get()
    qtd_den = den.val()
    if qtd_den != None:
        for fishy_den in den.each():
            nun = {"Id": fishy_den.key()}
            denun.append(nun)
    else:
        denun.append("Null")

for i in usersFish.each():
    user = i.val()
    liked_fh = ""
    for id_fh in denun:
        if id_fh["Id"] == i.key():
                liked_fh = True
    if user['opcao'] == "invasor": 
        dict_user = {"Nome": user['nome'], "Tipo": user['opcao'], "Nome_invasor": user['invasor'], "Descricao": user['descricao'], "ID_Fishy": "" + i.key()}
    else:
        dict_user = {"Nome": user['nome'], "Tipo": user['opcao'], "Url": user['url_site'], "Descricao": user['descricao'], "ID_Fishy": "" + i.key()}
    dict_user["Fishy_liked"] = liked_fh
    users.append(dict_user)
 '''

'''
tools = list()
lista_tool = list()
usersAll = db.child("ferramentas").child("antimalware").get()
for ferramenta in usersAll.each():
    tool = ferramenta.val()
    dict_tools = {"Nome": tool["Nome"], "Tipo": tool["Tipo"], "Title":  tool["Title"], "Descricao":  tool["Descricao"], "Media_img": "card_media_" + str(tool["Id_media"])}
    lista_tool.append(dict_tools)
dic_tip = {"Tipo_tool": "antimalware", "Valor": lista_tool}
tools.append(dic_tip)

lista_tool = list()
usersAll = db.child("ferramentas").child("antivirus").get()
for ferramenta in usersAll.each():
    tool = ferramenta.val()
    dict_tools = {"Nome": tool["Nome"], "Tipo": tool["Tipo"], "Title":  tool["Title"], "Descricao":  tool["Descricao"], "Media_img": "card_media_" + str(tool["Id_media"])}
    lista_tool.append(dict_tools)
dic_tip = {"Tipo_tool": "antivirus", "Valor": lista_tool}
tools.append(dic_tip)
'''

'''
u = int(input())
nome = ["Avira", "Norton", "AVG"]
for i in range(0, len(nome)):
    dados = {"Nome": nome[i], "Tipo": "Anti-Span", "Title": "Ferramentas  Anti-Span", "Descricao": "Ferramenta de anti-virus, usada para proteger, detectar, impedir, previnir e realizar a remoção de softwares maliciosos, vírus e worms.", "Id_media": u}
    u += 1
    db.child("ferramentas").child("antivirus").child(db.generate_key()).set(dados)
'''

'''
u = int(input())
nome = ["Avira", "Norton", "AVG"]
for i in range(0, len(nome)):
    dados = {"Nome": nome[i], "Tipo": "Anti-Vírus", "Title": "Ferramentas  Anti-Vírus", "Descricao": "Ferramenta de anti-virus, usada para proteger, detectar, impedir, previnir e realizar a remoção de softwares maliciosos, vírus e worms.", "Id_media": u}
    u += 1
    db.child("ferramentas").child("antivirus").child(db.generate_key()).set(dados)
'''