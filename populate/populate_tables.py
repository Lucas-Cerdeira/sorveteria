from random import randint
from conf.db_session import create_session
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
    

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','r','s','t','u','v','w','x','y','z']


def change_x_by_number(char:str):
    return char.replace('X', str(randint(0, 9)))

def change_x_by_str(char:str):
    return char.replace('X', alfabeto[randint(0, 26)])

def change_caracters(iterable:str, numbers:bool=False):
    if numbers:
        iterable = map(change_x_by_number, iterable)
        iterable = ''.join(list(iterable))
        return iterable
    
    iterable = map(change_x_by_str, iterable)
    iterable = ''.join(list(iterable))
    return iterable


def populate_aditivo_nutritivo(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            modelo_nome = 'XXXXXX'
            nome = change_caracters(modelo_nome, numbers=False).capitalize()
            
            modelo_formula_quimica = 'XXXXX'
            formula_quimica = change_caracters(modelo_formula_quimica, numbers=False).capitalize()
            
            aditivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
            session.add(aditivo)
        session.commit()


def populate_conservante(quantidade:int):
        with create_session() as session:
            for i in range(quantidade):
                modelo_nome = 'XXXXXX'
                nome = change_caracters(modelo_nome, numbers=False).capitalize()
                
                descricao = f'Conserva por até {randint(1, 8)} horas fora da geladeira.'
                
                conservante = Conservante(nome=nome, descricao=descricao)
                session.add(conservante)

            session.commit()


def populate_ingrediente(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            modelo_nome = 'XXXXXX'
            nome = change_caracters(modelo_nome, numbers=False).capitalize()
            
            ingrediente = Ingrediente(nome=nome)
            session.add(ingrediente)

        session.commit()


def populate_revendedor(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            modelo_nome = 'XXXXXX'
            nome = change_caracters(modelo_nome, numbers=False).capitalize()
            
            modelo_razão_social = 'XXXXXX XXXXXX'
            razao_social = change_caracters(modelo_razão_social, numbers=False).capitalize()
            
            modelo_contato = 'XX 9XXXX-XXXX'
            contato = change_caracters(modelo_contato, numbers=True)
            
            revendedor = Revendedor(nome=nome, razao_social=razao_social, contato=contato)
            session.add(revendedor)

        session.commit()

def populate_sabor(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            modelo_nome = 'XXXXXX'
            nome = change_caracters(modelo_nome, numbers=False).capitalize()
        
            sabor = Sabor(nome=nome)
            session.add(sabor)
    
        session.commit()
    


def populate_tipo_embalagem(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            modelo_nome = 'XXXXXX'
            nome = change_caracters(modelo_nome, numbers=False).capitalize()

            tipo_embalagem = TipoEmbalagem(nome=nome)
            session.add(tipo_embalagem)
    
        session.commit()


def populate_tipo_picole(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            modelo_nome = 'XXXXXX'
            nome = change_caracters(modelo_nome, numbers=False).capitalize()
    
            tipo_picole = TipoPicole(nome=nome)
            session.add(tipo_picole)
    
        session.commit()


def populate_lote(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            id_tipo_picole = randint(1, 30)
            quantidade = randint(50, 300)

            lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
            session.add(lote)
        session.commit()

def populate_nota_fiscal(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            modelo_valor = f'{randint(50, 500)}.{1, 99}'
            valor = float(change_caracters(modelo_valor, numbers=True))

            modelo_numero_serie = 'XXXXXXXX'
            numero_serie = change_caracters(modelo_numero_serie, numbers=True)

            descricao = f'Nota Fiscal N°:{numero_serie} - Valor: {valor}'

            id_revendedor = randint(1, 30)

            nota_fiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)
            session.add(nota_fiscal)

            
            for i in range(3):
                id_tipo_picole = randint(1, 30)
                quantidade = randint(50, 300)

                lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
                session.add(lote)
                nota_fiscal.lotes.append(lote)
                
        session.commit()


def populate_picole(quantidade:int):
    with create_session() as session:
        for i in range(quantidade):
            modelo_preco = 'X.XX'
            preco = float(change_caracters(modelo_preco, numbers=True))

            id_sabor = randint(1, 30)
            id_tipo_embalagem = randint(1, 30)
            id_tipo_picole = randint(1, 30)

            picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)
            session.add(picole)



            for i in range(3):
                modelo_nome = 'XXXXXX'
                nome = change_caracters(modelo_nome, numbers=False).capitalize()
                
                descricao = f'Conserva por até {randint(1, 8)} horas fora da geladeira.'

                conservante = Conservante(nome=nome, descricao=descricao)
                session.add(conservante)
                
                picole.conservantes.append(conservante)

       
            for i in range(3):
                modelo_nome = 'XXXXXX'
                nome = change_caracters(modelo_nome, numbers=False).capitalize()
                
                ingrediente = Ingrediente(nome=nome)
                session.add(ingrediente)
                
                picole.ingredientes.append(ingrediente)

            for i in range(3):
                modelo_nome = 'XXXXXX'
                nome = change_caracters(modelo_nome, numbers=False).capitalize()
                
                modelo_formula_quimica = 'XXXXX'
                formula_quimica = change_caracters(modelo_formula_quimica, numbers=False).capitalize()

                aditivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
                session.add(aditivo)
                
                picole.aditivos_nutritivos.append(aditivo)

        session.commit()
    

        
if __name__=='__main__':
    ...






#30 SABORES
#30 ADITIVOS NUTRITIVOS
#30 INGREDIENTES
#30 TIPOS EMBALAGENS
#30 TIPOS PICOLE
#30 REVENDEDORES
