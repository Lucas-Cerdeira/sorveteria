from conf. db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_picole import TipoPicole
from models.tipo_embalagem import TipoEmbalagem
from models.revendedor import Revendedor
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole



def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando Aditivo Nutritivo')

    nome = str(input('Aditivo Nutritivo: '))
    formula_quimica = str(input('Formula Quimica: '))

    aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(aditivo_nutritivo)
        session.commit()

    return aditivo_nutritivo

def insert_sabor() -> Sabor:
    print('Cadastrando sabor')

    nome = str(input('Sabor: '))

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

    return sabor

def insert_tipo_picole() -> TipoPicole:
    print('Cadastrando Tipo Picole')

    nome = str(input('Tipo Picole: '))

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_picole)
        session.commit()

    return tipo_picole


def insert_tipo_embalagem() -> TipoEmbalagem:
    print('Cadastrando tipo Embalagem: ')

    nome = str(input('Tipo Embalagem: '))

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        session.commit()

    return tipo_embalagem

def insert_revendedor() -> Revendedor:
    print('Cadastrando Revendedor')

    nome = str(input('Revendedor: '))
    razao_social: str = str(input('Razão social: '))
    contato: str = str(input('Contato: '))

    revendedor: Revendedor = Revendedor(nome=nome, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()
        
    return revendedor

def insert_ingrediente() -> Ingrediente:
    print('Cadastrando Ingrediente')

    nome = str(input('Ingrediente: '))

    ingrediente: Ingrediente = Ingrediente(nome=nome)
    with create_session() as session:
        session.add(ingrediente)
        session.commit()
    return ingrediente


def insert_conservante() -> Conservante:
    print('Cadastrando Conservante')

    nome = str(input('Conservante: '))
    descricao = str(input('Descrição: '))

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)
    with create_session() as session:
        session.add(conservante)
        session.commit()

    return conservante

def insert_lote() -> Lote:
    print('Cadastrando Lote')

    id_tipo_picole = int(input('Id Tipo Picole: '))
    quantidade:int = int(input('Quantidade: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lote)
        session.commit()

    return lote

def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastrando Nota Fiscal')

    valor: float = float(input('Valor: R$'))
    numero_serie: str = str(input('Numero de serie: '))
    descricao: str = str(input('Descrição: '))
    id_revendedor: int = int(input('Id Revendedor: '))

    nota_fiscal: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie,descricao=descricao,id_revendedor=id_revendedor)
    #Criar lot e fazer append na nota
    
    while True:  
        lote: Lote = insert_lote()
        nota_fiscal.lotes.append(lote)
        R = str(input('Gostaria de adicionar mais um ingrediente?[S/N] ')).strip()
        if R == 'N':
            break

    with create_session() as session:
        session.add(nota_fiscal)
        session.commit()
    
    return nota_fiscal

def insert_picole() -> Picole:
    print('Cadastro Picole')

    preco: float = float(input('Preço: '))
    id_sabor: int = int(input('Id Sabor: '))
    id_tipo_embalagem: int = int(input('Id Tipo Embalagem: '))
    id_tipo_picole: int = int(input('Id Tipo Picole: '))

    picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)


    while True:  
        ingrediente: Ingrediente = insert_ingrediente()
        picole.ingredientes.append(ingrediente)
        R = str(input('Gostaria de adicionar mais um ingrediente?[S/N] ')).strip()
        if R == 'N':
            break

    while True:  
        conservante: Conservante = insert_conservante()
        picole.conservantes.append(conservante)
        R = str(input('Gostaria de adicionar mais um conservante?[S/N] ')).strip()
        if R == 'N':
            break 

    while True:  
        aditivo_nutritivo: AditivoNutritivo = insert_aditivo_nutritivo()
        picole.aditivos_nutritivos.append(aditivo_nutritivo)
        R = str(input('Gostaria de adicionar mais um aditivo nutritivo?[S/N] ')).strip()
        if R == 'N':
            break

    
    with create_session() as session:
        session.add(picole)
        session.commit()
    return picole

if __name__=='__main__':
    an = insert_aditivo_nutritivo()
    print(an)
    print(an.id)
    print(an.nome)

    #sabor = insert_sabor()
    #print(sabor)
    #print(sabor.id)
    #print(sabor.nome)
    #print(sabor.data_Criacao)

    #tipo_picole = insert_tipo_picole()
    #print(tipo_picole)
    #print(tipo_picole.id)
    #print(tipo_picole.nome)
    #print(tipo_picole.data_Criacao)

    #tipo_embalagem = insert_tipo_embalagem()
    #print(tipo_embalagem)
    #print(tipo_embalagem.id)
    #print(tipo_embalagem.nome)
    
    #revendedor = insert_revendedor()
    #print(revendedor)
    #print(revendedor.id)
    #print(revendedor.nome)
    #print(revendedor.razao_social)
    #print(revendedor.contato)

    #conservante = insert_conservante()
    #print(conservante)
    #print(conservante.id)
    #print(conservante.nome)
    #print(conservante.descricao)
    #print(conservante.data_Criacao)

    #lote = insert_lote()
    #print(lote)
    #print(lote.id)
    #print(lote.data_Criacao)
    #print(lote.id_tipo_picole)
    #print(lote.quantidade)

    #nota_fiscal = insert_nota_fiscal()
    #print(nota_fiscal)
    #print(nota_fiscal.id)
    #print(nota_fiscal.valor)
    #print(nota_fiscal.numero_serie)
    #print(nota_fiscal.descricao)
    #print(nota_fiscal.id_revendedor)
    #print(nota_fiscal.lotes)

    #picole = insert_picole()
    #print(picole)
    #print(picole.preco)
    #print(picole.id_sabor)
    #print(picole.id_tipo_embalagem)
    #print(picole.id_tipo_Picole)
    #print(picole.ingredientes)
    #print(picole.conservantes)
    #print(picole.aditivos_nutritivos)
    ...