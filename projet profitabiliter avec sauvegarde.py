from pathlib import Path
import json
nom_de_svg = ""
etat_de_la_sauveguarde="desactive"
choix_tipe_sauveguarde=1
nombre_année=1
sauvegarde="a"
while True:
    print(f"""se petit programe es la pour vous aider a determiner 
votre rentabiliter annuele a partire de votre moyenne journaliere.
faite votre choix:
1 calcule de la progretion sur une année j par j sans impots '253jour ouvré'.
2 calcule de la progretion sur une année j par j avec impots '253jour ouvré'.
3 sauvegarde automatique({etat_de_la_sauveguarde}).
4 calcule de la progretion complette sur une durée de votre choix.
5 calcule de la progretion complette sur une durée de votre choix avec impots .
8 quitté. """)
    print("*"*50)
    user_choise = input("qu'elle choix vouler vous faire :")



    if user_choise == "1":
        chois_impot="sans"
        nombre_année=1
        capitale_de_depart=input("qu'elle capitale avez vous au d'epart? : ")
        while capitale_de_depart.isalpha():
            capitale_de_depart=input("qu'elle capitale avez vous au d'epart? : ")
        capitale_de_depart=float(capitale_de_depart)
        teaux_journalier_attendue = input("combien penser vous gagner en % par jour? :")
        while teaux_journalier_attendue.isalpha() :
            teaux_journalier_attendue = input("combien penser vous gagner en % par jour? :")
        teaux_journalier_attendue=float(teaux_journalier_attendue)
        resulta = capitale_de_depart
        resulta_finale = []
        for i in range(1,254):
            resulta =  resulta * (1+teaux_journalier_attendue/100)
            resulta_b=(i,resulta)
            print (resulta_b)
            resulta_finale.append(resulta_b)


        
    elif user_choise == "2":
        chois_impot="avec"
        nombre_année=1
        capitale_de_depart=input("qu'elle capitale avez vous au d'epart? : ")
        while capitale_de_depart.isalpha():
            capitale_de_depart=input("qu'elle capitale avez vous au d'epart? : ")
        capitale_de_depart=float(capitale_de_depart)
        teaux_journalier_attendue = input("combien penser vous gagner en % par jour? :")
        while teaux_journalier_attendue.isalpha() :
            teaux_journalier_attendue = input("combien penser vous gagner en % par jour? :")
        teaux_journalier_attendue=float(teaux_journalier_attendue) 
        resulta = capitale_de_depart
        resulta_finale = []
        for i in range(254):
            daye=(i  )
            resulta = resulta * (1+teaux_journalier_attendue/100) 
            resulta_b = (i,resulta)
            print (resulta_b)
            resulta_finale.append(resulta_b)
        ponxion_de_limpot = (resulta * 0.30)
        gain_apres_impots= ( resulta - ponxion_de_limpot )
        print(f"""vous avez donc gané a la fin de l'anné {resulta}.
        l'etat vous a ponxioner {ponxion_de_limpot}.
        il vous rest donc en gain net{gain_apres_impots}""")
        resulta_finale.append(gain_apres_impots)



    elif user_choise == "3":
        if etat_de_la_sauveguarde == "desactive":
            choix_tipe_sauveguarde=2
            etat_de_la_sauveguarde="activé"
            continue
        else:
            choix_tipe_sauveguarde=1
            etat_de_la_sauveguarde="desactive"
            continue



    elif user_choise=="4":
        chois_impot="sans"
        capitale_de_depart=input("qu'elle capitale avez vous au d'epart? : ")
        while capitale_de_depart.isalpha():
            capitale_de_depart=input("qu'elle capitale avez vous au d'epart? : ")
        capitale_de_depart=float(capitale_de_depart)
        teaux_journalier_attendue = input("combien penser vous gagner en % par jour? :")
        while teaux_journalier_attendue.isalpha() :
            teaux_journalier_attendue = input("combien penser vous gagner en % par jour? :")
        teaux_journalier_attendue=float(teaux_journalier_attendue)
        nombre_année=input("sur combien d'année?: ")
        while nombre_année.isalpha():
            nombre_année=input("sur combien d'année?: ")
        nombre_année=int(nombre_année)
        resulta = capitale_de_depart
        resulta_finale = []
        resulta_année=[]
        année=1
        for i in range(1,nombre_année +1):
            for i in range(1,254):
                resulta =  resulta * (1+teaux_journalier_attendue/100)
            resulta_finale.append(resulta)
            print(f"pour l'année{année} vous avez gagnée{resulta}")
            année=année+1


            
    elif user_choise=="5":
        chois_impot="avec"
        capitale_de_depart=input("qu'elle capitale avez vous au d'epart? : ")
        while capitale_de_depart.isalpha():
            capitale_de_depart=input("qu'elle capitale avez vous au d'epart? : ")
        capitale_de_depart=float(capitale_de_depart)
        teaux_journalier_attendue = input("combien penser vous gagner en % par jour? :")
        while teaux_journalier_attendue.isalpha() :
            teaux_journalier_attendue = input("combien penser vous gagner en % par jour? :")
        teaux_journalier_attendue=float(teaux_journalier_attendue)
        nombre_année=input("sur combien d'année?: ")
        while nombre_année.isalpha():
            nombre_année=input("sur combien d'année?: ")
        nombre_année=int(nombre_année)
        resulta = capitale_de_depart
        resulta_finale = []
        impot_totale= 0
        année=1
        resulta_finale.append("resulta / ponxion de l'impot /gain apres l'impot")
        for i in range(1,nombre_année+1):
            for i in range(1,254):
                resulta =  resulta * (1+teaux_journalier_attendue/100)  
            ponxion_de_limpot = (resulta * 0.30)
            impot_totale=impot_totale+ponxion_de_limpot
            gain_apres_impots= ( resulta - ponxion_de_limpot )
            resulta_finale.append(f"{resulta} / {ponxion_de_limpot} / {gain_apres_impots}")
            resulta=gain_apres_impots
            print(f"pour l'année{année} vous avez gagnée{gain_apres_impots}")
            print(f"et payer {ponxion_de_limpot}...")
            année=année+1
        print(f"au totale vous aurez payer {impot_totale}")


         
    if choix_tipe_sauveguarde == 1:
            while not sauvegarde == "o" or "n":
                sauvegarde=input("voulez vous sauvegarder ce resultat?o/n: ")
                if sauvegarde == "o":
                    nom_de_svg = (f"{capitale_de_depart}_{teaux_journalier_attendue}_sur_{nombre_année}_année {chois_impot} impot")
                    chemin=Path.cwd()/"svg"
                    chemin.mkdir(parents=True, exist_ok=True)
                    with open(f"{chemin}/{nom_de_svg}.json","w")as f:
                        json.dump(resulta_finale,f,indent=4)
                    print("sauveguarde effectuer") 
                    print(chemin) 
                    break
                elif sauvegarde == "n":
                    print("les resultats non pas eter sauvegarder.") 
                    break
            else:
                print ("veillez rentres une instruction valide...")                 
    elif choix_tipe_sauveguarde==2:
                nom_de_svg = (f"{capitale_de_depart}_{teaux_journalier_attendue}_sur_{nombre_année}_année {chois_impot} impot")
                chemin=Path.cwd()/"svg"
                chemin.mkdir(parents=True, exist_ok=True)
                with open(f"{chemin}/{nom_de_svg}.json","w")as f:
                    json.dump(resulta_finale,f,indent=4)
                print("sauveguarde effectuer")        