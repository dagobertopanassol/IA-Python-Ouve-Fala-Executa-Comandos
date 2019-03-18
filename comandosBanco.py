# -*- coding: utf-8 -*-
"""
Fuções de BD - Dagoberto.panassol@gmail.com
http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
"""
import sqlite3

def ler_frase():
    
    conn = sqlite3.connect('frasesqlite.db')
    cursor = conn.cursor()
    #lendo os dados
    cursor.execute("""
    SELECT * FROM frases;
    """)
    
    for linha in cursor.fetchall():
        print(linha)
    
    conn.close()
    return

def insere_manual():
    conn = sqlite3.connect('frasesqlite.db')
    cursor = conn.cursor()
    # solicitando os dados ao usuário
    pfrase = input('Frase: ')
    psig = input('Significado: ')
    p_criado_em = input('Criado em (yyyy-mm-dd): ')
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO frases (frase, significado, criado_em)
    VALUES (?,?,?)
    """, (pfrase, psig, p_criado_em))
    
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()
    return

def grava_bd():
    conn = sqlite3.connect('frasesqlite.db')
    cursor = conn.cursor()
    
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO frases (frase, significado, criado_em)
    VALUES ('cachorro', 'bicho peludo', '2014-06-08')
    """)
            
    # gravando no bd
    conn.commit()
    
    print('Dados inseridos com sucesso.')
    
    conn.close()
    return


def ver_campos():
    campos = sqlite3.connect
    
    # frasesqlite.db 'PRAGMA table_info(frasesqlite)'
    print (campos)
    return

def criar_banco(): 
    #conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('frasesqlite.db')
    cursor = conn.cursor()
    # criando a tabela (schema)
    cursor.execute("""
    CREATE TABLE frases (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            frase TEXT NOT NULL,
            significado TEXT NOT NULL,
            criado_em DATE
    );
    """)
    
    print('Tabela criada com sucesso.')
    # desconectando...
    conn.close()
    return

#criar_banco()
#grava_bd()
#insere_manual()
ler_frase()
