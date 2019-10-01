import os, sys
import smtplib
import time, datetime
from libs.audio import *

#globals

contactos = {}
gmail_user = ""
gmail_password = ""

#globals

#auxiliary functions

def extract_cmd(cmd, kw):
    for i in cmd.split():
        if kw in i:
            juice = cmd.split()[cmd.split().index(i) + 1::]
    try:
        return " ".join(juice)
    except:
        return 0

def anotate(string):
    if not os.getcwd() == "C:\\Users\\Usuario\\Desktop\\ROS\\data":
        try:
            os.chdir("C:\\Users\\Usuario\\Desktop\\ROS\\data")
        except:
            os.mkdir("C:\\Users\\Usuario\\Desktop\\ROS\\data")
            os.chdir("C:\\Users\\Usuario\\Desktop\\ROS\\data")
    if os.path.exists("notes.txt"):
        f = open("notes.txt", "a")
        f.write(string + "\n")
        f.close()
    else:
        f = open("notes.txt", "w+")
        f.write(string + "\n")
        f.close()

def show_anotations():
    os.chdir("C:\\Users\\Usuario\\Desktop\\ROS\\data")
    try:
        f = open("notes.txt")
        content = f.read()
        all_notes = content.splitlines()
        print("\n".join(all_notes))
    except:
        say("Señor, actualmente no tiene ninguna nota")
        print("Sin notas")

def jimena_help():
    helptext = "Puedo hacer gran variedad de cosas, señor. Entre ellas están administrar contactos, mandar correos electrónicos, darle la hora, llevar a cabo operaciones matemáticas... Usted solo pida"
    return helptext

def login():
    global gmail_user
    global gmail_password
    if os.path.exists("database.txt"):
        f = open("database.txt", "r")
        content = f.read().split()
        gmail_user = content[0]
        gmail_password = content[1]
    else:
        gmail_user = input("Usuario de gmail > ")
        gmail_password = input("Contraseña de gmail > ")
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            f = open("database.txt", "w+")
            f.write(gmail_user + "\n" + gmail_password)
            f.close()
        except:
            print("Usuario o contraseña incorrectos")
            login()

def greeting():
    hour = datetime.datetime.now().hour
    if hour == 12:
        say("Buen mediodía señor, ¿en qué puedo ayudarle?")
    elif hour < 12 and hour > 7:
        say("Buenos días señor, ¿en qué puedo ayudarle?")
    elif hour < 12 and hour < 7:
        say("Señor, debería volver a la cama")
    elif hour > 12 and hour < 20:
        say("Buenas tardes señor, ¿en qué puedo ayudarle?")
    elif hour >= 20:
        say("Buenas noches señor, ¿en qué puedo ayudarle?")
    else:
        say("Señor, parece que toca arreglar el tema greeting, ¿no le parece?")

def gmail(username):
    global gmail_user
    global gmail_password
    sent_from = gmail_user
    to = username
    subject = input("Señor, el subject > ")
    body = f"""Subject: {subject}\n"""
    while True:
        line = input("--> ") + "\n"
        if line == "abort\n":
            break
        else:
            body += line
    email_text = """\
        From: {}
        To: {}
        Subject: {}


        {}
        """.format(sent_from, ", ".join(to), subject, body)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print(f"Señor, el mensaje \"{subject}\" ha sido enviado a: {to}")


def add_contacts():
    global contactos
    say("Señor, ¿cuántos contactos desea añadir?")
    times = int(input("Número de contactos > "))
    f = open("contactos.txt", "a")
    for i in range(times):
        name = input("Nombre del contacto > ")
        gmail = input("Dirección de correo electrónico del contacto > ")
        f.write(name + "\n")
        f.write(gmail + "\n")
        contactos[name] = gmail
        if times == 1:
            say("Señor, " + str(times) + " contacto nuevo ha sido añadido a su lista")
        else:
            say("Señor, " + str(times) + " contactos nuevos han sido añadidos a su lista")

def accurate_add(username, gmail):
    global contactos
    edited_username = username.replace("-", "")
    f = open("contactos.txt", "a")
    f.write("\n" + edited_username + "\n")
    f.write(gmail.replace("-", "") + "\n")
    contactos[username] = gmail
    print(f"Señor, el contacto {edited_username} ha sido añadido a su lista")


def remove_contacts():
    global contactos
    f = open("contactos.txt", "r")
    content_copy = f.read()
    f.close()
    f = open("contactos.txt", "w+")
    counter = 0
    print("\nEstos son sus contactos actuales, señor: \n")
    for i in contactos:
        counter += 1
        print(str(counter) + ". " + i.title() + "   -> " + contactos[i])
    print("\n")
    rm_name = input("Introduzca el nombre del contacto que desea borrar > ")
    content_copy = content_copy.replace(contactos[rm_name], "")
    content_copy = content_copy.replace(rm_name + "\n", "")
    del(contactos[rm_name])
    f.write(content_copy)
    f.close()

def accurate_removal(contact_name):
    global contactos
    f = open("contactos.txt", "r")
    content_copy = f.read()
    f.close()
    f = open("contactos.txt", "w+")
    content_copy = content_copy.replace(contactos[contact_name], "")
    content_copy = content_copy.replace(contact_name + "\n", "")
    del(contactos[contact_name])
    f.write(content_copy)
    f.close()

def contact_setup():
    global contactos
    if not os.path.exists("contactos.txt"):
        f = open("contactos.txt", "w+")
        times = int(input("Señor, ¿cuántos contactos desea añadir? > "))
        for i in range(times):
            name = input("Nombe del contacto > ")
            gmail = input("Dirección de correo electrónico del contacto > ")
            f.write(name + "\n")
            f.write(gmail + "\n")
            contactos[name] = gmail
        f.close()
    else:
        counter = 0
        f = open("contactos.txt", "r")
        content = f.read()
        all_contacts_mashup = content.split()
        for i in all_contacts_mashup:
            try:
                contactos[all_contacts_mashup[counter]] = all_contacts_mashup[counter + 1]
                counter += 2
            except:
                pass

def operate(cmd):
    try:
        cmd = cmd.replace("calcula ", "")
        print(f"{cmd} = {str(eval(cmd))}")
    except:
        say("Señor, ha habido un error en la sintaxis de la operación")

def makeCall():
    pass


def setup():
    login()
    contact_setup()

# auxiliary functions

def Jimena():
    setup()
    greeting()
    global contactos
    destinatarios = []
    while True:
        cmd = input("> ")
        if "ayuda" in cmd or "puedes hacer" in cmd:
            say(jimena_help())
        elif "manda" in cmd and "gmail" in cmd or "correo" in cmd:
            for i in contactos:
                if i in cmd:
                    destinatarios.append(contactos[i])
            election = input("En consola o en app? > ")
            if election == "consola":
                    say("Abriendo consola...")
                    gmail(destinatarios)
            elif election == "app":
                    print("Abriendo app...")
                    os.chdir("..")
                    os.system("Gmail.lnk")
            else:
                    print("No le he entendido, señor")
        elif "contact" in cmd:
            if "enseñ" in cmd:
                counter = 0
                say("Estos son sus contactos actuales, señor")
                for i in contactos:
                    counter += 1
                    print(str(counter) + ". " + i.title() + "   -> " + contactos[i])
                print("\n")
            elif "añad" in cmd:
                data_to_add = []
                accurate_confirmation = False
                for i in cmd.split():
                    if i.startswith("-"):
                        data_to_add.append(i)
                        if not len(data_to_add) == 2:
                            print("Señor, debería haber un nombre de usuario y un gmail")
                            print(len(data_to_add))
                        else:
                            accurate_confirmation = True      
                if accurate_confirmation:
                    accurate_add(data_to_add[0], data_to_add[1])
                else:
                    add_contacts()
            elif "borr" in cmd:
                accurate_confirmation = False
                for i in contactos:
                    if i in cmd:
                        accurate_confirmation = True
                if accurate_confirmation:
                    accurate_removal(i)
                else:
                    remove_contacts()
        elif "hora" in cmd:
            if "numero" in cmd:
                print(f"Señor, son las {datetime.datetime.now().hour}")
            else:
                print(f"Señor, son las {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")
        elif "calcu" in cmd:
            operate(cmd)
        elif "llama" in cmd:
            makeCall()
        elif "not" in cmd:
            if "enseñ" in cmd or "muestr" in cmd or "mostr" in cmd:
                show_anotations()
            else:
                anotate(extract_cmd(cmd, "not"))
        elif "adios" in cmd:
                say("Hasta la próxima, señor")
                time.sleep(1)
                sys.exit()

if __name__ == "__main__":
    Jimena()
