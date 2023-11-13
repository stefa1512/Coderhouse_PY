import json
user_disc = {
    "estudiantes": [
        {
            "nombre": "Luis",
            "edad": 34
        },
        {
            "nombre": "Rodrigo",
            "edad": 26
        },
        {
            "nombre": "Maria",
            "edad": 42
        },
    ]
}
user_str = json
with open("estudiante.txt","w") as fil:
    fil.write(user_disc)
