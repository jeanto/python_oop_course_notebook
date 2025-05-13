import json
from faker import Faker
import random
import unicodedata

fake = Faker('pt_BR')

# Lista de órgãos necessários e gravidade da condição
orgaos_necessarios = ["Coração", "Rins",  "Fígado", "Pâncreas", "Pulmão", "Intestino", 
                   "Córneas", "Pele", "Ossos", "Válvulas cardíacas", "Cartilagem", "Medula Óssea", 
                   "Tendões", "Vasos Sanguíneos", "Sangue de Cordão Umbilical", "Sangue Universal"]
gravidade_condicoes = ["Leve", "Moderada", "Grave", "Crítica"]

# Lista de profissões e estados civis para variar os dados
professions = ["Professor", "Engenheiro", "Médico", "Advogado", "Enfermeiro", "Arquiteto", "Contador", "Policial", "Motorista", "Vendedor"]
marital_statuses = ["Solteiro", "Casado", "Divorciado", "Viuvo"]
tipo_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
capitais_brasil = {"AC": "Rio Branco", "AL": "Maceió", "AP": "Macapá", "AM": "Manaus", 
                   "BA": "Salvador", "CE": "Fortaleza", "DF": "Brasília", "ES": "Vitória", 
                   "GO": "Goiânia", "MA": "São Luís", "MT": "Cuiabá", "MS": "Campo Grande", 
                   "MG": "Belo Horizonte", "PA": "Belém", "PB": "João Pessoa", 
                   "PR": "Curitiba", "PE": "Recife", "PI": "Teresina", 
                   "RJ": "Rio de Janeiro", "RN": "Natal", "RS": "Porto Alegre", 
                   "RO": "Porto Velho", "RR": "Boa Vista", "SC": "Florianópolis", 
                   "SP": "São Paulo", "SE": "Aracaju", "TO": "Palmas" }

# Função para remover acentos de caracteres Unicode
def remover_acentos(texto):
    """Remove acentos de caracteres Unicode."""
    nfkd_form = unicodedata.normalize('NFKD', texto)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('utf-8')
    return only_ascii

# Função para gerar um receptor sintético
def generate_receptores():
    
    dados = {
            "nome": remover_acentos(fake.name()),
            "idade": random.randint(18, 80),
            "sexo": random.choice(["M", "F"]),
            "data_nascimento": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%d/%m/%Y"),
            "cidade_natal": fake.city(),
            "estado_natal": fake.state_abbr(),
            "cpf": fake.ssn(),
            "profissao": random.choice(professions),
            "cidade_residencia": fake.city(),
            "estado_residencia": fake.state_abbr(),
            "estado_civil": random.choice(marital_statuses),
            "contato_emergencia": fake.phone_number(),
            "tipo_sanguineo": random.choice(tipo_sanguineos)
        }
    
    necessidade = {
            "orgao_necessario": remover_acentos(random.choice(orgaos_necessarios)).lower(),
            "gravidade_condicao": random.choice(gravidade_condicoes),
            "centro_transplante": capitais_brasil[dados["estado_residencia"]],
            "posicao_lista_espera": random.randint(1, 500)
        }
        
    return { "dados": dados, "necessidade": necessidade }

# Função para gerar um receptor sintético
def generate_receptores_short():
    
    dados = {
            "nome": remover_acentos(fake.name()),
            "idade": random.randint(18, 80),
            "estado_residencia": fake.state_abbr(),
            "tipo_sanguineo": random.choice(tipo_sanguineos)
        }
    
    necessidade = {
            "orgao_necessario": remover_acentos(random.choice(orgaos_necessarios)).lower(),
            "gravidade_condicao": random.choice(gravidade_condicoes),
            "centro_transplante": capitais_brasil[dados["estado_residencia"]],
            "posicao_lista_espera": random.randint(1, 500)
        }
        
    return { "dados": dados, "necessidade": necessidade }

def main():
    # Gerar x receptores sintéticos
    recipients = [generate_receptores() for _ in range(10)]

    # Salvar os dados em um arquivo JSON
    with open("receptores.json", "w", encoding="utf-8") as f:
        json.dump(recipients, f, ensure_ascii=False, indent=4)

    print("Arquivo JSON com dados sintéticos de potenciais receptores gerado com sucesso!")


if __name__ == '__main__':
    pass