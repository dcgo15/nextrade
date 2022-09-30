from tkinter import *
from datetime import datetime as syd
import requests
import mysql.connector

connect = mysql.connector.connect(host="localhost",
                                  database="nextrade", user="root",
                                  password="META100Kk#")

cursor = connect.cursor()

app2 = Tk()
app2.title("Login - nextrade")
app2.geometry("400x200")
app2.config(bg="black")

def conta():
    em = email.get()
    sen = senha.get()

    cursor.execute("SELECT * FROM usuarios WHERE email=%s AND senha=%s",(em, sen))
    resposta = cursor.fetchone()

    conn = mysql.connector.connect(host="localhost",
                                  database="nextrade", user="root",
                                  password="META100Kk#")

    ku = conn.cursor()

    em = ku.execute("SELECT Nome FROM usuarios WHERE email=%s",(em,))
    emm = ku.fetchone()
    nms2 = [str(i) for i in emm]
    emai = str("".join(nms2))

    if resposta:
        print("ok")
        app2.destroy()
        connect2 = mysql.connector.connect(host="localhost",
                                  database="nextrade", user="root",
                                  password="META100Kk#")

        cursor2 = connect2.cursor()


        link = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
        resposta = requests.get(link)
        conteudo = resposta.json()

        dolar = conteudo["USDBRL"]["bid"]
        dolar_alt = conteudo["USDBRL"]["high"]
        dolar_baix = conteudo["USDBRL"]["low"]

        euro = conteudo["EURBRL"]["bid"]
        euro_alt = conteudo["EURBRL"]["high"]
        euro_baix = conteudo["EURBRL"]["low"]

        bit = conteudo["BTCBRL"]["bid"]
        bit_alt = conteudo["BTCBRL"]["high"]
        bit_baix = conteudo["BTCBRL"]["low"]

        hora = syd.time(syd.now())

        import datetime

        da =  datetime.date.today()

        app = Tk()
        app.title("Dashboard - nextrade")
        app.geometry("600x400")
        app.config(bg="black")

        lb = Label(app, text=f"Olá, {emai}", bg="black",
                   fg="white", font="arial 20 bold italic").place(x=0, y=0)


        lb = Label(app, text="COTAÇÕES:", fg="black", font="arial 24 bold").place(x=40, y=90)


        do = Canvas(app, width=400, height=200) #1

        #w.create_rectangle(50, 25, 150, 75)  #244
        do.place(x=40, y=160)

        eu = Canvas(app, width=400, height=200) #1

        #w.create_rectangle(50, 25, 150, 75)  #2
        eu.place(x=460, y=160)

        bt = Canvas(app, width=400, height=200) #1

        #w.create_rectangle(50, 25, 150, 75)  #2
        bt.place(x=880, y=160)

        lb = Label(app, text="DOLAR:", bg="black",
                   fg="white", font="arial 24 bold").place(x=40, y=170)
        lb = Label(app, text="EURO:", bg="black",
                   fg="white", font="arial 24 bold").place(x=460, y=170)
        lb = Label(app, text="BITCOIN:", bg="black",
                   fg="white", font="arial 24 bold").place(x=880, y=170)

        pre_dol = Label(app, text=f"R${dolar}", bg="black",
                   fg="white", font="arial 24 bold").place(x=40, y=220)
        pre_dol_alt = Label(app, text=f"MAX:R${dolar_alt}", bg="black",
                   fg="green", font="arial 20 bold").place(x=40, y=280)
        pre_dol_bai = Label(app, text=f"MIN:R${dolar_baix}", bg="black",
                   fg="red", font="arial 20 bold").place(x=261, y=280)


        pre_eur = Label(app, text=f"R${euro}", bg="black",
                   fg="white", font="arial 24 bold").place(x=460, y=220)
        pre_eur_alt = Label(app, text=f"MAX:R${euro_alt}", bg="black",
                   fg="green", font="arial 20 bold").place(x=460, y=280)
        pre_eur_bai = Label(app, text=f"MIN:R${euro_baix}", bg="black",
                   fg="red", font="arial 20 bold").place(x=701, y=280)


        pre_bit =Label(app, text=f"R${bit}", bg="black",
                   fg="white", font="arial 24 bold").place(x=880, y=220)
        pre_bit_alt = Label(app, text=f"MAX:R${bit_alt}", bg="black",
                   fg="green", font="arial 20 bold").place(x=880, y=280)
        pre_bit_bai = Label(app, text=f"MIN:R${bit_baix}", bg="black",
                   fg="red", font="arial 20 bold").place(x=1101, y=280)


        def pesq():
            app3 = Tk()
            app3.title("Pesquisar ação")
            app3.config(bg="black")
            app3.geometry("1000x800")

            def pesqu():
                link = f"https://www.okanebox.com.br/api/acoes/ultima/{pesq.get()}/"
                resposta = requests.get(link)
                conteudo = resposta.json()

                name = pesq.get()

                pri = conteudo["PREMED"]
                pre = conteudo["DATPRG"]
                maxim = conteudo["PREMAX"]
                minim = conteudo["PREMIN"]
                volu = conteudo["VOLTOT"]
                qua = conteudo["QUATOT"]

                nome["text"] = "NOME:",name
                price["text"] = "PREÇO:R$",pri
                pregao["text"] = "PREGÃO:",pre
                qtd["text"]="QTD:R$",qua
                vol["text"]="VOLTOT:",volu
                maxi["text"]="MAX:R$",maxim
                mini["text"]="MIN:R$",minim

                
                

            lb = Label(app3, text="PESQUISAR COTAÇÃO", bg="black",
                       fg="white",font="arial 30 bold" )
            lb.place(x=400,y=0)

            pesq = Entry(app3, width=90)
            pesq.place(x=250,y=100)


            button = Button(app3, text="Pesquisar", width=20,
                            fg="black",bg="white",command=pesqu).place(x=800,y=100)

            do = Canvas(app3, width=800, height=400) #1

            do.place(x=250, y=200)

            nome = Label(app3, text="NOME:{}", bg="black",
                   fg="white", font="arial 30 bold")
            nome.place(x=250, y=220)
            price = Label(app3, text="PREÇO:{}", bg="black",
                   fg="white", font="arial 30 bold")
            price.place(x=821, y=220)
            
            pregao = Label(app3, text="PREGÃO:{}", bg="black",
                   fg="white", font="arial 16 bold")
            pregao.place(x=250, y=280)

            qtd = Label(app3, text="QTD:R$", bg="black",
                   fg="white", font="arial 20 bold")
            qtd.place(x=250, y=350)
            vol = Label(app3, text="VOL:R$", bg="black",
                   fg="white", font="arial 20 bold")
            vol.place(x=821, y=350)

            
            maxi = Label(app3, text="MAX:R$", bg="black",
                   fg="green", font="arial 20 bold")
            maxi.place(x=250, y=500)
            mini = Label(app3, text="MIN:R$", bg="black",
                   fg="red", font="arial 20 bold")
            mini.place(x=828, y=500)

            

            app3.mainloop()

        bai = Button(app,text="Pesquisar",width=20,bg="white",fg="black"
                     ,font="arial 10 bold",command=pesq).place(x=1100,y=0)


        hora = Label(app, text=f"HORA: {hora}", fg="white", font="arial 16 bold"
                   ,bg="black").place(x=750,y=600)
        data =Label(app, text=f"DATA: {da}", fg="white", font="arial 16 bold"
                   ,bg="black").place(x=1050,y=600)

        def ajud():
            manu = Tk()
            manu.title("help")
            manu.geometry("300x200")
            manu.config(bg="black")
            manu.resizable(0, 0)

            lb = Label(manu, text="CONTATE-NOS", font="arial 15 bold",
                       fg="white", bg="black").pack()

            lb= Label(manu, text="Numero:(75) 98224-3100", font="arial 12 bold",
                       fg="white", bg="black").pack()
            lb= Label(manu, text="Email:softmaze6@gmail.com", font="arial 12 bold",
                       fg="white", bg="black").pack()
            lb= Label(manu, text="Site:dcgo15.github.io/nex", font="arial 12 bold",
                       fg="white", bg="black").pack()

            manu.mainloop()

        aj = Button(app, text="ajuda",width=10,bg="white",fg="black",
                     font="arial 10 bold",command=ajud).place(x=40,y=500)


        hora = Label(app, text="v1.0.7 - BETA . MAZE SOFTWARE CORPORATION.", fg="white", font="arial 16 bold"
                   ,bg="black").place(x=40,y=600)


        app.mainloop()

lb = Label(app2, text="nextrade", fg="white", font="arial 16 bold"
           ,bg="black").pack()

em = Label(app2, text="email:", fg="white", font="arial 10 bold"
           ,bg="black").place(x=60, y=30)


email = Entry()
email.pack()

Label(app2, bg="black", height=1).pack()

se = Label(app2, text="senha:", fg="white", font="arial 10 bold"
           ,bg="black").place(x=60, y=70)


senha = Entry(app2, show="●")
senha.pack()

Label(app2, bg="black", height=1).pack()


continu= Button(app2, text="continuar",command=conta).pack()

Label(app2, bg="black", height=1).pack()

def criar():
    app2.destroy()

    appz = Tk()
    appz.title("Sign up - nextrade")
    appz.geometry("400x200")
    appz.config(bg="black")

    def criar():
        name = nome.get()
        em = email.get()
        se = senha.get()

        resposta = cursor.execute("INSERT INTO usuarios(id, Nome, Email, Senha) VALUES(null, %s, %s, %s)", (name, em, se))
        connect.commit()
        connect.close()

        
        appz.destroy()

        conn = mysql.connector.connect(host="localhost",
                                  database="nextrade", user="root",
                                  password="META100Kk#")

        ku = conn.cursor()

        em = ku.execute("SELECT Nome FROM usuarios WHERE email=%s",(em,))
        emm = ku.fetchone()
        nms2 = [str(i) for i in emm]
        emai = str("".join(nms2))

        connect2 = mysql.connector.connect(host="localhost",
                                  database="nextrade", user="root",
                                  password="META100Kk#")

        cursor2 = connect2.cursor()


        link = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
        resposta = requests.get(link)
        conteudo = resposta.json()

        dolar = conteudo["USDBRL"]["bid"]
        dolar_alt = conteudo["USDBRL"]["high"]
        dolar_baix = conteudo["USDBRL"]["low"]

        euro = conteudo["EURBRL"]["bid"]
        euro_alt = conteudo["EURBRL"]["high"]
        euro_baix = conteudo["EURBRL"]["low"]

        bit = conteudo["BTCBRL"]["bid"]
        bit_alt = conteudo["BTCBRL"]["high"]
        bit_baix = conteudo["BTCBRL"]["low"]

        hora = syd.time(syd.now())

        import datetime

        da =  datetime.date.today()

        app = Tk()
        app.title("Dashboard - nextrade")
        app.geometry("600x400")
        app.config(bg="black")

        lb = Label(app, text=f"Olá, {emai}", bg="black",
                   fg="white", font="arial 20 bold italic").place(x=0, y=0)


        lb = Label(app, text="COTAÇÕES:", fg="black", font="arial 24 bold").place(x=40, y=90)


        do = Canvas(app, width=400, height=200) #1

        #w.create_rectangle(50, 25, 150, 75)  #244
        do.place(x=40, y=160)

        eu = Canvas(app, width=400, height=200) #1

        #w.create_rectangle(50, 25, 150, 75)  #2
        eu.place(x=460, y=160)

        bt = Canvas(app, width=400, height=200) #1

        #w.create_rectangle(50, 25, 150, 75)  #2
        bt.place(x=880, y=160)

        lb = Label(app, text="DOLAR:", bg="black",
                   fg="white", font="arial 24 bold").place(x=40, y=170)
        lb = Label(app, text="EURO:", bg="black",
                   fg="white", font="arial 24 bold").place(x=460, y=170)
        lb = Label(app, text="BITCOIN:", bg="black",
                   fg="white", font="arial 24 bold").place(x=880, y=170)

        pre_dol = Label(app, text=f"R${dolar}", bg="black",
                   fg="white", font="arial 24 bold").place(x=40, y=220)
        pre_dol_alt = Label(app, text=f"MAX:R${dolar_alt}", bg="black",
                   fg="green", font="arial 20 bold").place(x=40, y=280)
        pre_dol_bai = Label(app, text=f"MIN:R${dolar_baix}", bg="black",
                   fg="red", font="arial 20 bold").place(x=261, y=280)


        pre_eur = Label(app, text=f"R${euro}", bg="black",
                   fg="white", font="arial 24 bold").place(x=460, y=220)
        pre_eur_alt = Label(app, text=f"MAX:R${euro_alt}", bg="black",
                   fg="green", font="arial 20 bold").place(x=460, y=280)
        pre_eur_bai = Label(app, text=f"MIN:R${euro_baix}", bg="black",
                   fg="red", font="arial 20 bold").place(x=701, y=280)


        pre_bit =Label(app, text=f"R${bit}", bg="black",
                   fg="white", font="arial 24 bold").place(x=880, y=220)
        pre_bit_alt = Label(app, text=f"MAX:R${bit_alt}", bg="black",
                   fg="green", font="arial 20 bold").place(x=880, y=280)
        pre_bit_bai = Label(app, text=f"MIN:R${bit_baix}", bg="black",
                   fg="red", font="arial 20 bold").place(x=1101, y=280)


        def pesq():
            app3 = Tk()
            app3.title("Pesquisar ação")
            app3.config(bg="black")
            app3.geometry("1000x800")

            def pesqu():
                link = f"https://www.okanebox.com.br/api/acoes/ultima/{pesq.get()}/"
                resposta = requests.get(link)
                conteudo = resposta.json()

                name = pesq.get()

                pri = conteudo["PREMED"]
                pre = conteudo["DATPRG"]
                maxim = conteudo["PREMAX"]
                minim = conteudo["PREMIN"]
                volu = conteudo["VOLTOT"]
                qua = conteudo["QUATOT"]

                nome["text"] = "NOME:",name
                price["text"] = "PREÇO:R$",pri
                pregao["text"] = "PREGÃO:",pre
                qtd["text"]="QTD:R$",qua
                vol["text"]="VOLTOT:",volu
                maxi["text"]="MAX:R$",maxim
                mini["text"]="MIN:R$",minim

                
                

            lb = Label(app3, text="PESQUISAR COTAÇÃO", bg="black",
                       fg="white",font="arial 30 bold" )
            lb.place(x=400,y=0)

            pesq = Entry(app3, width=90)
            pesq.place(x=250,y=100)


            button = Button(app3, text="Pesquisar", width=20,
                            fg="black",bg="white",command=pesqu).place(x=800,y=100)

            do = Canvas(app3, width=800, height=400) #1

            do.place(x=250, y=200)

            nome = Label(app3, text="NOME:{}", bg="black",
                   fg="white", font="arial 30 bold")
            nome.place(x=250, y=220)
            price = Label(app3, text="PREÇO:{}", bg="black",
                   fg="white", font="arial 30 bold")
            price.place(x=821, y=220)
            
            pregao = Label(app3, text="PREGÃO:{}", bg="black",
                   fg="white", font="arial 16 bold")
            pregao.place(x=250, y=280)

            qtd = Label(app3, text="QTD:R$", bg="black",
                   fg="white", font="arial 20 bold")
            qtd.place(x=250, y=350)
            vol = Label(app3, text="VOL:R$", bg="black",
                   fg="white", font="arial 20 bold")
            vol.place(x=821, y=350)

            
            maxi = Label(app3, text="MAX:R$", bg="black",
                   fg="green", font="arial 20 bold")
            maxi.place(x=250, y=500)
            mini = Label(app3, text="MIN:R$", bg="black",
                   fg="red", font="arial 20 bold")
            mini.place(x=828, y=500)

            

            app3.mainloop()

        bai = Button(app,text="Pesquisar",width=20,bg="white",fg="black"
                     ,font="arial 10 bold",command=pesq).place(x=1100,y=0)


        hora = Label(app, text=f"HORA: {hora}", fg="white", font="arial 16 bold"
                   ,bg="black").place(x=750,y=600)
        data =Label(app, text=f"DATA: {da}", fg="white", font="arial 16 bold"
                   ,bg="black").place(x=1050,y=600)

        def ajud():
            manu = Tk()
            manu.title("help")
            manu.geometry("300x200")
            manu.config(bg="black")
            manu.resizable(0, 0)

            lb = Label(manu, text="CONTATE-NOS", font="arial 15 bold",
                       fg="white", bg="black").pack()

            lb= Label(manu, text="Numero:(75) 98224-3100", font="arial 12 bold",
                       fg="white", bg="black").pack()
            lb= Label(manu, text="Email:softmaze6@gmail.com", font="arial 12 bold",
                       fg="white", bg="black").pack()
            lb= Label(manu, text="Site:dcgo15.github.io/nex", font="arial 12 bold",
                       fg="white", bg="black").pack()

            manu.mainloop()

        aj = Button(app, text="ajuda",width=10,bg="white",fg="black",
                     font="arial 10 bold",command=ajud).place(x=40,y=500)


        hora = Label(app, text="v1.0.7 - BETA . MAZE SOFTWARE CORPORATION.", fg="white", font="arial 16 bold"
                   ,bg="black").place(x=40,y=600)


        app.mainloop()
        


    lb = Label(appz, text="nextrade", fg="white", font="arial 16 bold"
               ,bg="black").pack()



    no = Label(appz, text="nome:", fg="white", font="arial 10 bold"
               ,bg="black").place(x=60, y=30)

    nome = Entry()
    nome.pack()

    Label(appz, bg="black", height=1).pack()

    em = Label(appz, text="email:", fg="white", font="arial 10 bold"
               ,bg="black").place(x=60, y=70)


    email = Entry()
    email.pack()

    Label(appz, bg="black", height=1).pack()

    se = Label(appz, text="senha:", fg="white", font="arial 10 bold"
               ,bg="black").place(x=60, y=110)


    senha = Entry(appz, show="●")
    senha.pack()

    Label(appz, bg="black", height=1).pack()


    continu= Button(appz, text="criar",command=criar).pack()

    Label(appz, bg="black", height=1).pack()

    def conta():
        appz.destroy()
        import login


    conta= Button(appz, text="já tem uma conta?",
                  command=conta).pack()


    appz.mainloop()

    
    


conta= Button(app2, text="não tem uma conta?",
              command=criar).pack()


app2.mainloop()
