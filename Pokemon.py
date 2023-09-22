""" 
Este código é um jogo de Pokemon com 2 pokemon cada treinador, sendo eles Charmander e Squirtle, para o jogador, e Pikachu e Bulbasauro, para a máquina. 
Para jogar, deve-se digitar seu nome e o nome que deseja para seu rival
Em seguida poderá escolher entre seus 2 pokemon e iniciar a batalha contra a máquina. 
Durante a batalha, aparecerá os golpes que poderá utilizar ao lado de suas respectivas quantidades de uso disponíveis, sendo necessário escrever o nome dos golpes para executa-los. 
Aquele quer zerar a vida dos 2 pokemon do adversário primeiro será o vencedor 

Programa feito por Djan
"""

from random import choice,choices
Jogo = True
T = True
Atributos = {
"Fogo":     {
    "Vantagens":["Metal","Grama","Inseto","Gelo","Fada","Fogo"],
    "Desvantagens":["Agua","Pedra","Terra"],
    "Imunidades":[]
            }
,
"Agua":     {
    "Vantagens":["Fogo","Terra","Pedra","Agua","Gelo","Metal"],
    "Desvantagens":["Grama","Eletrico"],
    "Imunidades":[]
            }
,
"Eletrico":     {
    "Vantagens":["Agua","Voador","Eletrico"],
    "Desvantagens":["Terra"],
    "Imunidades":[]
            }
,
"Grama":     {
    "Vantagens":["Agua","Pedra","Terra","Grama","Eletrico"],
    "Desvantagens":["Fogo","Gelo","Inseto","Venenoso","Voador"],
    "Imunidades":[]
            }
,
"Pedra":     {
    "Vantagens":["Fogo","Gelo","Voador","Inseto","Venenoso","Normal"],
    "Desvantagens":["Metal","Agua","Lutador","Grama","Terra"],
    "Imunidades":[]
            }
,
"Terra":     {
    "Vantagens":["Metal","Fogo","Eletrico","Pedra","Venenoso"],
    "Desvantagens":["Agua","Gelo","Grama"],
    "Imunidades":["Eletrico"]
            }
,
"Venenoso":     {
    "Vantagens":["Grama","Fada","Venenoso","Inseto","Lutador"],
    "Desvantagens":["Psiquico","Terra"],
    "Imunidades":[]
            }
,
"Voador":     {
    "Vantagens":["Inseto","Lutador","Grama"],
    "Desvantagens":["Eletrico","Gelo","Pedra"],
    "Imunidades":["Terra"]
            }
,
"Psiquico":     {
    "Vantagens":["Lutador","Venenoso","Psiquico"],
    "Desvantagens":["Fantasma","Sombrio","Inseto"],
    "Imunidades":[]
            }
,
"Sombrio":     {
    "Vantagens":["Fantasma","Psiquico","Sombrio"],
    "Desvantagens":["Fada","Lutador","Inseto"],
    "Imunidades":["Psiquico"]
            }
,
"Lutador":     {
    "Vantagens":["Metal","Pedra","Gelo","Normal","Sombrio"],
    "Desvantagens":["Fada","Psiquico","Voador"],
    "Imunidades":[]
            }
,
"Dragão":     {
    "Vantagens":["Dragão","Eletrico","Fogo","Agua","Inseto"],
    "Desvantagens":["Dragão","Gelo","Fada"],
    "Imunidades":[]
            }
,
"Metal":     {
    "Vantagens":["Fada","Pedra","Gelo","Metal","Dragão","Normal","Grama","Voador","Inseto","Psiquico"],
    "Desvantagens":["Fogo","Terra","Lutador"],
    "Imunidades":["Venenoso"]
            }
,
"Fada":     {
    "Vantagens":["Dragão","Lutador","Sombrio"],
    "Desvantagens":["Metal","Venenoso"],
    "Imunidades":["Dragão"]
            }
,
"Gelo":     {
    "Vantagens":["Dragão","Grama","Terra","Gelo"],
    "Desvantagens":["Fogo","Metal","Lutador","Pedra"],
    "Imunidades":[]
            }
,
"Fantasma":     {
    "Vantagens":["Fantasma","Psiquico","Venenoso","Inseto"],
    "Desvantagens":["Fantasma","Sombrio"],
    "Imunidades":["Normal","Lutador"]
            }
,
"Normal":     {
    "Vantagens":[],
    "Desvantagens":["Lutador"],
    "Imunidades":["Fantasma"]
            }
,
"Inseto":     {
    "Vantagens":["Grama","Terra","Lutador"],
    "Desvantagens":["Fogo","Voador","Terra"],
    "Imunidades":[]
            }
,
"-":       {
    "Vantagens":[],
    "Desvantagens":[],
    "Imunidades":[]
            }
}
while Jogo == True:
    Pokemons_Player = {
    "Charizard":{"Vida":120,"Velocidade":14,"Tipo":["Fogo","Voador"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Flamethrower":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Fogo"
                        }
                }
                }
    ,
    "Jolteon":{"Vida":120,"Velocidade":10,"Tipo":["Eletrico","-"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Thunderbolt":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Eletrico"
                        }
                }
                }
    ,
    "Lapras":{"Vida":120,"Velocidade":14,"Tipo":["Gelo","Agua"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Water Pulse":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Agua"
                        }
                }
                }
    ,
    "Persian":{"Vida":120,"Velocidade":14,"Tipo":["Normal","-"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Slash":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Normal"
                        }
                }
                }
    ,
    "Scyther":{"Vida":120,"Velocidade":14,"Tipo":["Inseto","Voador"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Bug Buzz":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Inseto"
                        }
                }
                }
    ,
    "Dodrio":{"Vida":120,"Velocidade":14,"Tipo":["Voador","Normal"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Aerial Ace":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Voador"
                        }
                }
                }
                                                
                    }
    
    Pokemons_Bot = {
    "Blastoise":{"Vida":120,"Velocidade":10,"Tipo":["Agua","-"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Water Pulse":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Agua"
                        }
                }
                }
    ,
    "Pidgeot":{"Vida":120,"Velocidade":10,"Tipo":["Voador","Normal"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Brave Bird":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Voador"
                        }
                }
                }
    ,
    "Alakazam":{"Vida":120,"Velocidade":10,"Tipo":["Psiquico","-"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Psychic":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Psiquico"
                        }
                }
                }
    ,
    "Rhydon":{"Vida":120,"Velocidade":10,"Tipo":["Terra","Pedra"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Rock Tomb":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Pedra"
                        }
                }
                }
    ,
    "Arcanine":{"Vida":120,"Velocidade":10,"Tipo":["Fogo","-"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Flare Blitz":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Fogo"
                        }
                }
                }
    ,
    "Exeggutor":{"Vida":120,"Velocidade":15,"Tipo":["Psiquico","Grama"],
        "Ataques":{
            "Tackle":{
                "Dano":20 ,
                "Usos":6,
                "Tipo":"Normal"
                    } ,
            "Razor Leaf":{
                "Dano":40 ,
                "Usos":2,
                "Tipo":"Grama"
                        }
                }
                }
                                    }
    
    Nome_Player = input("Qual o seu nome?    ")
    
    while Nome_Player == "":
        print("Nome Inválido")
        Nome_Player = input("Qual o seu nome?    ")
    
    Nome_Bot = input("Qual o nome do seu rival?    ")

    while Nome_Bot == "":
        print("Nome Inválido")
        Nome_Bot = input("Qual o nome do seu rival?    ")

    Derrota_Bot = 0
    Derrota_Player = 0

    Pokemon_Bot = []
    for x in Pokemons_Bot.keys():
        Pokemon_Bot.append(x)

    Pokemon_Player = []
    for x in Pokemons_Player.keys():
        Pokemon_Player.append(x)

    Bot_Pokemon = choice(Pokemon_Bot)
    PokBot1 = Bot_Pokemon

    Battle_Pokemon = input(f"Escolha seu Pokemon: {Pokemon_Player[0]} // {Pokemon_Player[1]} // {Pokemon_Player[2]} // {Pokemon_Player[3]} // {Pokemon_Player[4]} // {Pokemon_Player[5]}    ").title()
    while Battle_Pokemon not in Pokemons_Player.keys():
        print("Você não tem esse pokemon")
        Battle_Pokemon = input(f"Escolha seu Pokemon: {Pokemon_Player[0]} // {Pokemon_Player[1]} // {Pokemon_Player[2]} // {Pokemon_Player[3]} // {Pokemon_Player[4]} // {Pokemon_Player[5]}    ").title()

    Pok1 = Battle_Pokemon
   
    print("---"*35)

    print(f"AQUI COMEÇA A BATALHA ENTRE {Nome_Player.upper()} E {Nome_Bot.upper()} !!!")
    print("---"*35)
    print(f"{Nome_Player.upper()} LANÇA {Battle_Pokemon.upper()} E {Nome_Bot.upper()} LANÇA {Bot_Pokemon.upper()} !!!")

    Player_Wins = 0
    Bot_Wins = 0

    def Batalha():
        
        Tipo_Player = Pokemons_Player[Battle_Pokemon]["Tipo"]
        Tipo_Bot = Pokemons_Bot[Bot_Pokemon]["Tipo"]

        Ataques_Pokemon = []
        for x in Pokemons_Player[Battle_Pokemon]["Ataques"].keys():
            Ataques_Pokemon.append(x)

        Atk1 = Ataques_Pokemon[0]
        Atk2 = Ataques_Pokemon[1]
        Atks = [Atk1,Atk2]

        Usos_Pokemon = []
        for x in Atks:
            Usos_Pokemon.append(Pokemons_Player[Battle_Pokemon]["Ataques"][x]["Usos"])
        UsosAtk1 = Usos_Pokemon[0]
        UsosAtk2 = Usos_Pokemon[1]

        Ataques_Pokemon_Bot = []
        for x in Pokemons_Bot[Bot_Pokemon]["Ataques"].keys():
            Ataques_Pokemon_Bot.append(x)

        Vantagem_Bot1 = False
        Vantagem_Bot2 = False
        Vantagem_Bot3 = False
        Desvantagem_Bot1 = False
        Desvantagem_Bot2 = False
        Desvantagem_Bot3 = False
        Neutro_Player = False
        Nulo_Bot = False
        Vantagem_Player1 = False
        Vantagem_Player2 = False
        Vantagem_Player3 = False
        Desvantagem_Player1 = False
        Desvantagem_Player2 = False
        Desvantagem_Player3 = False
        Neutro_Bot = False
        Nulo_Player = False

        if Pokemons_Player[Battle_Pokemon]["Velocidade"] < Pokemons_Bot[Bot_Pokemon]["Velocidade"]:

            while Pokemons_Player[Battle_Pokemon]["Vida"] >= 1 and Pokemons_Bot[Bot_Pokemon]["Vida"] >= 1:

                Vida_Pok_Bot = Pokemons_Bot[Bot_Pokemon]["Vida"]

                print("---"*35)
                print(f"Turno de {Nome_Bot}")

                Atk_Bot = choices(Ataques_Pokemon_Bot,[0.5,0.5])[0]

                if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[0]]["Desvantagens"]:
                    Vantagem_Bot1 = True
                    
                if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[1]]["Desvantagens"]:
                    Vantagem_Bot2 = True
                
                if Vantagem_Bot1 == True and Vantagem_Bot2 == True:
                    Vantagem_Bot3 = True

                if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[0]]["Vantagens"]:
                    Desvantagem_Bot1 = True
                    
                if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[1]]["Vantagens"]:
                    Desvantagem_Bot2 = True
                
                if Desvantagem_Bot1 == True and Desvantagem_Bot2 == True:
                    Desvantagem_Bot3 = True
                    
                if (Vantagem_Bot1 == True and Desvantagem_Bot1 == True) or (Vantagem_Bot1 == True and Desvantagem_Bot2 == True) or (Vantagem_Bot2 == True and Desvantagem_Bot1 == True) or (Vantagem_Bot2 == True and Desvantagem_Bot2 == True):
                    Neutro_Bot = True
                
                if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[0]]["Imunidades"] or Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[1]]["Imunidades"]:
                    Nulo_Bot = True

                Vida_Pok_Bot = Pokemons_Bot[Bot_Pokemon]["Vida"]
                Vida_Pok = Pokemons_Player[Battle_Pokemon]["Vida"]

                print("---"*35)
                print(f"{Battle_Pokemon}: {Vida_Pok} HP // {Bot_Pokemon}: {Vida_Pok_Bot} HP")

                if Nulo_Bot == True:
                    Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]*0
                
                elif Neutro_Bot == True:
                    Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]
                
                elif Vantagem_Bot3 == True:
                    Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]*4
                
                elif Vantagem_Bot1 == True or Vantagem_Bot2 == True:
                    Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]*2

                elif Desvantagem_Bot3 == True:
                    Pokemons_Player[Battle_Pokemon]["Vida"] -= int(Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]/4)
                
                elif Desvantagem_Bot1 == True or Desvantagem_Bot2 == True:
                    Pokemons_Player[Battle_Pokemon]["Vida"] -= int(Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]/2)

                else:
                    Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]

                Dano = Vida_Pok - Pokemons_Player[Battle_Pokemon]["Vida"]

                print("---"*35)
                if Pokemons_Player[Battle_Pokemon]["Vida"] >= 1:
                    if Neutro_Bot == True:
                        print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon}")
                    elif Nulo_Bot == True:
                        print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon} pois é imune à esse golpe")
                    elif Vantagem_Bot1 == True or Vantagem_Bot2 == True:
                        print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon}, um golpe super efetivo")
                    elif Desvantagem_Bot1 == True or Desvantagem_Bot2 == True:
                        print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon}, um golpe pouco efetivo")
                    else:
                        print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon}")

                if Pokemons_Player[Battle_Pokemon]["Vida"] >= 1:
                    print("---"*35)
                    print("Seu turno")
                    Vida_Pok = Pokemons_Player[Battle_Pokemon]["Vida"]
                    Vida_Pok_Bot = Pokemons_Bot[Bot_Pokemon]["Vida"]

                    print("---"*35)
                    print(f"{Battle_Pokemon}: {Vida_Pok} HP // {Bot_Pokemon}: {Vida_Pok_Bot} HP")
                    print("---"*35)

                    Atk_Player = input(f"Escolha o seu golpe: ( {Atk1} [{UsosAtk1}] // {Atk2} [{UsosAtk2}] )       ").title()

                    while Atk_Player not in Atks:
                        print("Seu pokemon não possui esse golpe")
                        Atk_Player = input(f"Escolha o seu golpe: ( {Atk1} [{UsosAtk1}] // {Atk2} [{UsosAtk2}] )       ").title()

                    if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[0]]["Desvantagens"]:
                        Vantagem_Player1 = True

                    if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[1]]["Desvantagens"]:
                        Vantagem_Player2 = True
                    
                    if Vantagem_Player1 == True and Vantagem_Player2 == True:
                        Vantagem_Player3 = True

                    if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[0]]["Vantagens"]:
                        Desvantagem_Player1 = True

                    if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[1]]["Vantagens"]:
                        Desvantagem_Player2 = True
                    
                    if Desvantagem_Player1 == True and Desvantagem_Player2 == True:
                        Desvantagem_Player3 = True
                    
                    if (Vantagem_Player1 == True and Desvantagem_Player1 == True) or (Vantagem_Player1 == True and Desvantagem_Player2 == True) or (Vantagem_Player2 == True and Desvantagem_Player1 == True) or (Vantagem_Player2 == True and Desvantagem_Player2 == True):
                        Neutro_Player = True
                    
                    if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[0]]["Imunidades"] or Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[1]]["Imunidades"]:
                        Nulo_Player = True

                    if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk1]["Usos"] == 0 and Pokemons_Player[Battle_Pokemon]["Ataques"][Atk2]["Usos"] == 0:
                        Pokemons_Player[Battle_Pokemon]["Vida"] = 0
                        print("---"*35)
                        print(f"{Battle_Pokemon} foi derrotado por não conseguir revidar")
                        print("---"*35)
                        break

                    while Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Usos"] == 0:
                        print("Seu pokemon não consegue mais usar este golpe")
                        Atk_Player = input(f"Escolha o seu golpe: ( {Atk1} [{UsosAtk1}] // {Atk2} [{UsosAtk2}] )       ").title()

                    Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Usos"] -= 1

                    if Atks.index(Atk_Player) == 0:
                        UsosAtk1 = Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Usos"]

                    elif Atks.index(Atk_Player) == 1:
                        UsosAtk2 = Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Usos"]

                    if Nulo_Player == True:
                        Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]*0
                    
                    elif Neutro_Player == True:
                        Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]
                    
                    elif Vantagem_Player3 == True:
                        Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]*4
                    
                    elif Vantagem_Player1 == True or Vantagem_Player2 == True:
                        Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]*2

                    elif Desvantagem_Player3 == True:
                        Pokemons_Bot[Bot_Pokemon]["Vida"] -= int(Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]/4)
                    
                    elif Desvantagem_Player1 == True or Desvantagem_Player2 == True:
                        Pokemons_Bot[Bot_Pokemon]["Vida"] -= int(Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]/2)

                    else:
                        Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]

                    Dano = Vida_Pok_Bot - Pokemons_Bot[Bot_Pokemon]["Vida"]

                    print("---"*35)
                    if Pokemons_Bot[Bot_Pokemon]["Vida"] >= 1:
                        if Neutro_Player == True:
                            print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon}")
                        elif Nulo_Player == True:
                            print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon} pois é imune à esse golpe")
                        elif Vantagem_Player1 == True or Vantagem_Player2 == True:
                            print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon}, um golpe super efetivo") 
                        elif Desvantagem_Player1 == True or Desvantagem_Player2 == True:
                            print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon}, um golpe pouco efetivo")
                        else:
                            print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon}")

                if Pokemons_Player[Battle_Pokemon]["Vida"] <= 0:
                    if Neutro_Bot == True:
                        print(f"{Battle_Pokemon} foi derrotado após receber um {Atk_Bot} de {Bot_Pokemon}")
                    elif Vantagem_Bot1 == True or Vantagem_Bot2 == True:
                        print(f"{Battle_Pokemon} foi derrotado após receber um {Atk_Bot} de {Bot_Pokemon}, um golpe super efetivo") 
                    elif Desvantagem_Bot1 == True or Desvantagem_Bot2 == True:
                        print(f"{Battle_Pokemon} foi derrotado após receber um {Atk_Bot} de {Bot_Pokemon}, um golpe pouco efetivo")
                    else:
                        print(f"{Battle_Pokemon} foi derrotado após receber um {Atk_Bot} de {Bot_Pokemon}")
                    print("---"*35)
                
                if Pokemons_Bot[Bot_Pokemon]["Vida"] <= 0:
                    if Neutro_Player == True:
                        print(f"{Bot_Pokemon} foi derrotado após receber um {Atk_Player} de {Battle_Pokemon}")
                    elif Vantagem_Player1 == True or Vantagem_Player2 == True:
                        print(f"{Bot_Pokemon} foi derrotado após receber um {Atk_Player} de {Battle_Pokemon}, um golpe super efetivo") 
                    elif Desvantagem_Player1 == True or Desvantagem_Player2 == True:
                        print(f"{Bot_Pokemon} foi derrotado após receber um {Atk_Player} de {Battle_Pokemon}, um golpe pouco efetivo")
                    else:
                        print(f"{Bot_Pokemon} foi derrotado após receber um {Atk_Player} de {Battle_Pokemon}")
                    print("---"*35)

                Vantagem_Player1 = False
                Vantagem_Player2 = False
                Vantagem_Player3 = False
                Desvantagem_Player1 = False
                Desvantagem_Player2 = False
                Desvantagem_Player3 = False
                Neutro_Player = False
                Nulo_Player = False

                Vantagem_Bot1 = False
                Vantagem_Bot2 = False
                Vantagem_Bot3 = False
                Desvantagem_Bot1 = False
                Desvantagem_Bot2 = False
                Desvantagem_Bot3 = False
                Neutro_Bot = False
                Nulo_Bot = False

        else:

            while Pokemons_Player[Battle_Pokemon]["Vida"] >= 1 and Pokemons_Bot[Bot_Pokemon]["Vida"] >= 1:

                print("---"*35)
                print("Seu turno")

                Vida_Pok = Pokemons_Player[Battle_Pokemon]["Vida"]
                Vida_Pok_Bot = Pokemons_Bot[Bot_Pokemon]["Vida"]

                print("---"*35)
                print(f"{Battle_Pokemon}: {Vida_Pok} HP // {Bot_Pokemon}: {Vida_Pok_Bot} HP")
                print("---"*35)

                Atk_Player = input(f"Escolha o seu golpe: ( {Atk1} [{UsosAtk1}] // {Atk2} [{UsosAtk2}] )       ").title()

                while Atk_Player not in Atks:
                    print("Seu pokemon não possui esse golpe")
                    Atk_Player = input(f"Escolha o seu golpe: ( {Atk1} [{UsosAtk1}] // {Atk2} [{UsosAtk2}] )       ").title()
                
                if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[0]]["Desvantagens"]:
                    Vantagem_Player1 = True

                if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[1]]["Desvantagens"]:
                    Vantagem_Player2 = True
                    
                if Vantagem_Player1 == True and Vantagem_Player2 == True:
                    Vantagem_Player3 = True

                if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[0]]["Vantagens"]:
                    Desvantagem_Player1 = True

                if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[1]]["Vantagens"]:
                    Desvantagem_Player2 = True
                    
                if Desvantagem_Player1 == True and Desvantagem_Player2 == True:
                    Desvantagem_Player3 == True
                
                if (Vantagem_Player1 == True and Desvantagem_Player1 == True) or (Vantagem_Player1 == True and Desvantagem_Player2 == True) or (Vantagem_Player2 == True and Desvantagem_Player1 == True) or (Vantagem_Player2 == True and Desvantagem_Player2 == True):
                    Neutro_Player = True
            
                if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[0]]["Imunidades"] or Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Tipo"] in Atributos[Tipo_Bot[1]]["Imunidades"]:
                    Nulo_Player = True

                if Pokemons_Player[Battle_Pokemon]["Ataques"][Atk1]["Usos"] == 0 and Pokemons_Player[Battle_Pokemon]["Ataques"][Atk2]["Usos"] == 0:
                    Pokemons_Player[Battle_Pokemon]["Vida"] = 0
                    print("---"*35)
                    print(f"{Battle_Pokemon} foi derrotado por não conseguir revidar")
                    print("---"*35)
                    break

                while Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Usos"] == 0:
                    print("Seu pokemon não consegue mais usar este golpe")
                    Atk_Player = input(f"Escolha o seu golpe: ( {Atk1} [{UsosAtk1}] // {Atk2} [{UsosAtk2}] )       ").title()

                Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Usos"] -= 1

                if Atks.index(Atk_Player) == 0:
                    UsosAtk1 = Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Usos"]

                elif Atks.index(Atk_Player) == 1:
                    UsosAtk2 = Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Usos"]

                if Nulo_Player == True:
                    Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]*0
                    
                elif Neutro_Player == True:
                    Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]

                elif Vantagem_Player3 == True:
                    Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]*4
                    
                elif Vantagem_Player1 == True or Vantagem_Player2 == True:
                    Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]*2

                elif Desvantagem_Player3 == True:
                    Pokemons_Bot[Bot_Pokemon]["Vida"] -= int(Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]/4)
                    
                elif Desvantagem_Player1 == True or Desvantagem_Player2 == True:
                    Pokemons_Bot[Bot_Pokemon]["Vida"] -= int(Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]/2)

                else:
                    Pokemons_Bot[Bot_Pokemon]["Vida"] -= Pokemons_Player[Battle_Pokemon]["Ataques"][Atk_Player]["Dano"]

                Dano = Vida_Pok_Bot - Pokemons_Bot[Bot_Pokemon]["Vida"]

                print("---"*35)
                if Pokemons_Bot[Bot_Pokemon]["Vida"] >= 1:
                    if Neutro_Player == True:
                        print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon}")
                    elif Nulo_Player == True:
                        print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon} pois é imune à esse golpe")
                    elif Vantagem_Player1 == True or Vantagem_Player2 == True:
                        print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon}, um golpe super efetivo") 
                    elif Desvantagem_Player1 == True or Desvantagem_Player2 == True:
                        print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon}, um golpe pouco efetivo")
                    else:
                        print(f"{Bot_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Player} de {Battle_Pokemon}")

                if Pokemons_Bot[Bot_Pokemon]["Vida"] >= 1:
                    print("---"*35)
                    print(f"Turno de {Nome_Bot}")

                    Atk_Bot = choices(Ataques_Pokemon_Bot,[0.5,0.5])[0]

                    if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[0]]["Desvantagens"]:
                        Vantagem_Bot1 = True
                    
                    if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[1]]["Desvantagens"]:
                        Vantagem_Bot2 = True

                    if Vantagem_Bot1 == True and Vantagem_Bot2 == True:
                        Vantagem_Bot3 = True
                    
                    if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[0]]["Vantagens"]:
                        Desvantagem_Bot1 = True
                    
                    if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[1]]["Vantagens"]:
                        Desvantagem_Bot2 = True
                    
                    if Desvantagem_Bot1 == True and Desvantagem_Bot2 == True:
                        Desvantagem_Bot3 = True
                    
                    if (Vantagem_Bot1 == True and Desvantagem_Bot1 == True) or (Vantagem_Bot1 == True and Desvantagem_Bot2 == True) or (Vantagem_Bot2 == True and Desvantagem_Bot1 == True) or (Vantagem_Bot2 == True and Desvantagem_Bot2 == True):
                        Neutro_Bot = True
                    
                    if Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[0]]["Imunidades"] or Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Tipo"] in Atributos[Tipo_Player[1]]["Imunidades"]:
                        Nulo_Bot = True

                    Vida_Pok = Pokemons_Player[Battle_Pokemon]["Vida"]
                    Vida_Pok_Bot = Pokemons_Bot[Bot_Pokemon]["Vida"]

                    print("---"*35)
                    print(f"{Battle_Pokemon}: {Vida_Pok} HP // {Bot_Pokemon}: {Vida_Pok_Bot} HP")

                    if Nulo_Bot == True:
                        Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]*0
                
                    elif Neutro_Bot == True:
                        Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]
                    
                    elif Vantagem_Bot3 == True:
                        Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]*4
                
                    elif Vantagem_Bot1 == True or Vantagem_Bot2 == True:
                        Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]*2

                    elif Desvantagem_Bot3 == True:
                        Pokemons_Player[Battle_Pokemon]["Vida"] -= int(Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]/4)
                
                    elif Desvantagem_Bot1 == True or Desvantagem_Bot2 == True:
                        Pokemons_Player[Battle_Pokemon]["Vida"] -= int(Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]/2)

                    else:
                        Pokemons_Player[Battle_Pokemon]["Vida"] -= Pokemons_Bot[Bot_Pokemon]["Ataques"][Atk_Bot]["Dano"]

                    Dano = Vida_Pok - Pokemons_Player[Battle_Pokemon]["Vida"]

                    print("---"*35)
                    if Pokemons_Player[Battle_Pokemon]["Vida"] >= 1:
                        if Neutro_Bot == True:
                            print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon}")
                        elif Nulo_Bot == True:
                            print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon} pois é imune à esse golpe")
                        elif Vantagem_Bot1 == True or Vantagem_Bot2 == True:
                            print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon}, um golpe super efetivo")
                        elif Desvantagem_Bot1 == True or Desvantagem_Bot2 == True:
                            print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon}, um golpe pouco efetivo")
                        else:
                            print(f"{Battle_Pokemon} perdeu {Dano} de vida ao receber um {Atk_Bot} de {Bot_Pokemon}")

                if Pokemons_Player[Battle_Pokemon]["Vida"] <= 0:
                    if Neutro_Bot == True:
                        print(f"{Battle_Pokemon} foi derrotado após receber um {Atk_Bot} de {Bot_Pokemon}")
                    elif Vantagem_Bot1 == True or Vantagem_Bot2 == True:
                        print(f"{Battle_Pokemon} foi derrotado após receber um {Atk_Bot} de {Bot_Pokemon}, um golpe super efetivo") 
                    elif Desvantagem_Bot1 == True or Desvantagem_Bot2 == True:
                        print(f"{Battle_Pokemon} foi derrotado após receber um {Atk_Bot} de {Bot_Pokemon}, um golpe pouco efetivo")
                    else:
                        print(f"{Battle_Pokemon} foi derrotado após receber um {Atk_Bot} de {Bot_Pokemon}")
                    print("---"*35)
                
                if Pokemons_Bot[Bot_Pokemon]["Vida"] <= 0:
                    if Neutro_Player == True:
                        print(f"{Bot_Pokemon} foi derrotado após receber um {Atk_Player} de {Battle_Pokemon}")
                    elif Vantagem_Player1 == True or Vantagem_Player2 == True:
                        print(f"{Bot_Pokemon} foi derrotado após receber um {Atk_Player} de {Battle_Pokemon}, um golpe super efetivo") 
                    elif Desvantagem_Player1 == True or Desvantagem_Player2 == True:
                        print(f"{Bot_Pokemon} foi derrotado após receber um {Atk_Player} de {Battle_Pokemon}, um golpe pouco efetivo")
                    else:
                        print(f"{Bot_Pokemon} foi derrotado após receber um {Atk_Player} de {Battle_Pokemon}")
                    print("---"*35)

                Vantagem_Player1 = False
                Vantagem_Player2 = False
                Vantagem_Player3 = False
                Desvantagem_Player1 = False
                Desvantagem_Player2 = False
                Desvantagem_Player3 = False
                Neutro_Player = False
                Nulo_Player = False

                Vantagem_Bot1 = False
                Vantagem_Bot2 = False
                Vantagem_Bot3 = False
                Desvantagem_Bot1 = False
                Desvantagem_Bot2 = False
                Desvantagem_Bot3 = False
                Neutro_Bot = False
                Nulo_Bot = False

    
    for x in range(11):

        Batalha()

        if Pokemons_Bot[Bot_Pokemon]["Vida"] <= 0:
            Player_Wins += 1
            Derrota_Bot += 1
            if Derrota_Bot < 6:
                Pokemon_Bot.remove(PokBot1)
                Bot_Pokemon = choice(Pokemon_Bot)
                print(f"{Nome_Bot} recolhe {PokBot1} e lança {Bot_Pokemon}")
                PokBot1 = Bot_Pokemon

        if Pokemons_Player[Battle_Pokemon]["Vida"] <= 0:
            Derrota_Player += 1
            Bot_Wins += 1

            if Derrota_Player < 5:
                if Derrota_Player < 6:
                    Pokemon_Player.remove(Pok1)

                    Battle_Pokemon = input(f"Escolha seu Pokemon: {Pokemon_Player}    ").title()

                    while Battle_Pokemon not in Pokemon_Player:
                        print("Você não tem esse pokemon")
                        Battle_Pokemon = input(f"Escolha seu Pokemon: {Pokemon_Player}    ").title()

                    print("---"*35)
                    print(f"{Nome_Player} recolhe {Pok1} e lança {Battle_Pokemon}")

            Pok1 = Battle_Pokemon

            if Derrota_Player == 5:
                if Derrota_Player < 6:
                      Pokemon_Player.remove(Pok1)
                      Battle_Pokemon = choice(Pokemon_Player)

                print(f"{Nome_Player} recolhe {Pok1} e lança {Battle_Pokemon}")

        if Player_Wins == 6 or Bot_Wins == 6:
            break
     
    if Player_Wins == 6:
        print(f"Parabens {Nome_Player}, você venceu todos os pokemons de {Nome_Bot}!!")
        print("---"*35)

    if Bot_Wins == 6:
        print(f"Não foi dessa vez {Nome_Player}, mais sorte da próxima vez")
        print("---"*35)
    
    Jogo = False
    T = True
    while T == True:
        Resposta = input("Quer jogar de novo?    ").lower()
        if Resposta == "sim" or Resposta == "si" or Resposta == "s":
            Jogo = True
            T = False
        elif Resposta == "nao" or Resposta == "não" or Resposta == "n":
            Jogo = False
            T = False
        else:
            print("---"*35)
            print("Resposta Inválida")
        print("---"*35)