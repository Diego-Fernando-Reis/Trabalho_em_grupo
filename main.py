lista = []

class Pesquisa:
    def __init__(self, idade, genero, resposta_1, resposta_2, resposta_3, resposta_4, data_hora):
        self.idade = idade
        self.genero = genero
        self.resposta_1 = resposta_1
        self.resposta_2 = resposta_2
        self.resposta_3 = resposta_3
        self.resposta_4 = resposta_4
        self.data_hora = data_hora

    def armazenar(self):
        lista.append([self.data_hora, self.idade, self.genero, self.resposta_1, self.resposta_2,self.resposta_3,self.resposta_4])
       
    
def importar_csv_para_lista(nome_arquivo):
    dados_lista = []
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            dados_lista.append(linha)
    return dados_lista

# Substitua 'arquivo.csv' pelo caminho do seu arquivo CSV
nome_arquivo = 'dados2.csv'
dados = importar_csv_para_lista(nome_arquivo)
print(dados)

i=0
while(i<len(dados)):
    with open('dados.csv', mode='a', newline='') as arquivo_csv:
        cabecalhos = ['idade', 'genero', 'pergunta1', 'pergunta2', 'pergunta3', 'pergunta4', 'pergunta5', 'pergunta6', 'data_hora']
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')

        if arquivo_csv.tell() == 0:
                escritor_csv.writerow(cabecalhos)

        #escreve na linha
        escritor_csv.writerow(dados[i])
        print(dados[i])
    i = i+1

def menu():
    idade=''
    while True: 
        idade = input('Qual a sua idade?')
        if idade != '00':
            genero = input('Qual o seu gênero?')

            print('''
                ======================================
                        PESQUISA DE SEGUROS
                ======================================
                ''')
            
            resposta_1=''
            resposta_2=''
            resposta_3=''
            resposta_4=''
            
            while resposta_1 != '1' and resposta_1 != '2' and resposta_1 != '3':
                resposta_1 = input('''
                    =============================
                            PERGUNTA 1
                    =============================
                    1 - Sim
                    2 - Não
                    3 - Não sei          
                    ''')
            
            while resposta_2 != '1' and resposta_2 != '2' and resposta_2 != '3':
                resposta_2 = input('''
                    =============================
                            PERGUNTA 2
                    =============================
                    1 - Sim
                    2 - Não
                    3 - Não sei
                    ''')

            while resposta_3 != '1' and resposta_3 != '2' and resposta_3 != '3':
                resposta_3 = input('''
                    =============================
                            PERGUNTA 3
                    =============================
                    1 - Sim
                    2 - Não
                    3 - Não sei
                    ''')   

            while resposta_4 != '1' and resposta_4 != '2' and resposta_4 != '3':
                resposta_4 = input('''
                    =============================
                            PERGUNTA 4
                    =============================
                    1 - Sim
                    2 - Não
                    3 - Não sei
                    ''')
        
        else:
            print('''
                ===================================
                    VOCÊ ENCERROU A COLETA DE DADOS
                ===================================
                ''')
            break

        entrevistado = Pesquisa(idade, genero, resposta_1, resposta_2, resposta_3, resposta_4, 'código data e hora')
        entrevistado.armazenar()

menu()

print(lista)