from random import randint
from conf.db_session import create_session
from insert_main import insert_aditivo_nutritivo
from utils.dados import alfabeto
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.revendedor import Revendedor
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.lote import Lote
from models.picole import Picole
from models.nota_fiscal import NotaFiscal



def populate_aditivo_nutritivo(quantidade:int):
    for i in range(quantidade):
        modelo_nome = 'XXXXXX'.capitalize()
        nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
        
        with create_session() as session:
            aditivo = AditivoNutritivo(nome=nome)
            session.add(aditivo)
    session.commit()


def populate_conservante(quantidade:int):
    for i in range(quantidade):
        modelo_nome = 'XXXXXX'.capitalize()
        nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
        
        descricao = f'Conserva por até {randint(1, 8)} horas fora da geladeira.'
        
        with create_session() as session:
            conservante = Conservante(nome=nome, descricao=descricao)
            session.add(conservante)

    session.commit()


def populate_ingrediente(quantidade:int):
    for i in range(quantidade):
        modelo_nome = 'XXXXXX'.capitalize()
        nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
        
        with create_session() as session:
            ingrediente = Ingrediente(nome=nome)
            session.add(ingrediente)

    session.commit()


def populate_revendedor(quantidade:int):
    for i in range(quantidade):
        modelo_nome = 'XXXXXX'.capitalize()
        nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
        
        modelo_razão_social = 'XXXXXX XXXXXX'.title()
        razao_social = modelo_razão_social.replace('X', alfabeto[randint(0, 26)])
        
        modelo_contato = 'XX 9XXXX-XXXX'
        contato = modelo_contato.replace('X', randint(0, 9))
        
        with create_session() as session:
                revendedor = Revendedor(nome=nome, razao_social=razao_social, contato=contato)
                session.add(revendedor)

    session.commit()

def populate_sabor(quantidade:int):
    for i in range(quantidade):
        modelo_nome = 'XXXXXX'.capitalize()
        nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
        
        with create_session() as session:
                sabor = Sabor(nome=nome)
                session.add(sabor)
    
    session.commit()
    


def populate_tipo_embalagem(quantidade:int):
    for i in range(quantidade):
        modelo_nome = 'XXXXXX'.capitalize()
        nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
        
        with create_session() as session:
                tipo_embalagem = TipoEmbalagem(nome=nome)
                session.add(tipo_embalagem)
    
    session.commit()


def populate_tipo_picole(quantidade:int):
    for i in range(quantidade):
        modelo_nome = 'XXXXXX'.capitalize()
        nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
        
        with create_session() as session:
                tipo_picole = TipoPicole(nome=nome)
                session.add(tipo_picole)
    
    session.commit()


def populate_lote(quantidade:int):
    for i in range(quantidade):
        id_tipo_picole = randint(1, 30)
        quantidade = randint(50, 300)

        with create_session() as session:
            lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
            session.add(lote)
    session.commit()

def populate_nota_fiscal(quantidade:int):
    for i in range(quantidade):
        modelo_valor = 'XXXX.XX'
        valor = float(modelo_valor.replace('X', randint(1, 9)))

        modelo_numero_serie = 'XXXXXXXX'
        numero_serie = modelo_numero_serie.replace('X', randint(0, 9))

        descricao = f'Nota Fiscal N°:{numero_serie} - Valor: {valor}'

        id_revendedor = randint(1, 30)

        with create_session() as session:
            nota_fiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)
            session.add(nota_fiscal)

        for i in range(3):
            id_tipo_picole = randint(1, 30)
            quantidade = randint(50, 300)

            with create_session() as session:
                lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
                session.add(lote)
                nota_fiscal.lotes.append(lote)
                
    session.commit()


def populate_picole(quantidade:int):
    for i in range(quantidade):
        modelo_preco = 'X.XX'
        preco = modelo_preco.replace('X', randint(0, 9))

        id_sabor = randint(1, 30)
        id_tipo_embalagem = randint(1, 30)
        id_tipo_picole = randint(1, 30)

        with create_session() as session:
            picole = Picole(id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)
            session.add(picole)


        for i in range(3):
            modelo_nome = 'XXXXXX'.capitalize()
            nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
            
            descricao = f'Conserva por até {randint(1, 8)} horas fora da geladeira.'
            
            with create_session() as session:
                conservante = Conservante(nome=nome, descricao=descricao)
                session.add(conservante)
                picole.conservantes.append(conservante)

       
        for i in range(3):
            modelo_nome = 'XXXXXX'.capitalize()
            nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
            
            with create_session() as session:
                ingrediente = Ingrediente(nome=nome)
                session.add(ingrediente)
                picole.ingredientes.append(ingrediente)

        for i in range(3):
            modelo_nome = 'XXXXXX'.capitalize()
            nome = modelo_nome.replace('X', alfabeto[randint(0, 26)])
            
            with create_session() as session:
                aditivo = AditivoNutritivo(nome=nome)
                session.add(aditivo)
                picole.aditivos_nutritivos.append(aditivo)

    session.commit()

    

    
        

    

        
if __name__=='__main__':
    populate_aditivo_nutritivo(2)





#30 SABORES
#30 ADITIVOS NUTRITIVOS
#30 INGREDIENTES
#30 TIPOS EMBALAGENS
#30 TIPOS PICOLE
#30 REVENDEDORES
