""" Sistema Acadêmico Integrado Projeto Integrado Multidisciplinar - 2º Semestre ADS Versão Corrigida e Melhorada - V3 """

import re
import os
from datetime import datetime, timedelta

# Listas globais para armazenar os dados
professores = []
turmas = []
alunos = []
aulas = []
atividades = []
frequencia = []
financas = []
mensagens = []
equipamentos = []  # Nova lista para equipamentos

# ========== INICIALIZAÇÃO DO SISTEMA ==========

def inicializar_sistema():
    """Inicializa o sistema com usuário administrador e equipamentos pré-cadastrados"""

    # Usuário Administrador pré-definido
    admin = {
        'cpf': 'admin',
        'nome': 'Administrador do Sistema',
        'email': 'admin@etec.sp.gov.br',
        'senha': 'admin123',
        'is_admin': True  # Flag para identificar admin
    }
    professores.append(admin)

    # Equipamentos pré-cadastrados
    equipamentos_iniciais = [
        {'id': 1, 'nome': 'Lousa com Rodinhas', 'nota': 4.5,
'disponibilidade': 'disponível',
         'locador_cpf': None, 'data_locacao': None, 'data_devolucao': None,
'total_avaliacoes': 10},
        {'id': 2, 'nome': 'Projetor', 'nota': 4.8, 'disponibilidade':
'disponível',


         'locador_cpf': None, 'data_locacao': None, 'data_devolucao': None,
'total_avaliacoes': 15},
        {'id': 3, 'nome': 'Microfone', 'nota': 4.2, 'disponibilidade':
'disponível',
         'locador_cpf': None, 'data_locacao': None, 'data_devolucao': None,
'total_avaliacoes': 8},
        {'id': 4, 'nome': 'Notebook', 'nota': 4.7, 'disponibilidade':
'disponível',
         'locador_cpf': None, 'data_locacao': None, 'data_devolucao': None,
'total_avaliacoes': 12}
    ]

    for equip in equipamentos_iniciais:
        equipamentos.append(equip)

# ========== FUNÇÕES DE UTILIDADE E VALIDAÇÃO ==========

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa a execução e aguarda o usuário pressionar ENTER"""
    input("\nPressione ENTER para continuar...")
    limpar_tela()

def confirmar_cancelamento():
    """Pergunta se o usuário deseja cancelar a operação"""
    resposta = input("\nDeseja cancelar e voltar ao menu? (S/N): ").upper()
    return resposta == 'S'

def validar_data(data):
    """Valida se a data está no formato DD/MM/AAAA"""
    if re.match(r"^\d{2}/\d{2}/\d{4}$", data):
        return True
    return False

def adicionar_dias(data_str, dias):
    """Adiciona dias a uma data no formato DD/MM/AAAA e retorna a nova data"""
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        nova_data = data + timedelta(days=dias)
        return nova_data.strftime("%d/%m/%Y")
    except:
        return None

def buscar_turma(codigo):
    """Busca uma turma pelo código usando busca linear"""
    for i in range(len(turmas)):


        if turmas[i]['codigo'] == codigo:
            return i
    return None

def buscar_professor(cpf):
    """Busca um professor pelo CPF usando busca linear"""
    for i in range(len(professores)):
        if professores[i]['cpf'] == cpf:
            return i
    return None

def buscar_aluno(ra):
    """Busca um aluno pelo RA usando busca linear"""
    for i in range(len(alunos)):
        if alunos[i]['ra'] == ra:
            return i
    return None

def buscar_equipamento(id_equip):
    """Busca um equipamento pelo ID"""
    for i in range(len(equipamentos)):
        if equipamentos[i]['id'] == id_equip:
            return i
    return None

def listar_turmas():
    """Lista todas as turmas cadastradas"""
    print("\n=== TURMAS CADASTRADAS ===")

    if len(turmas) == 0:
        print("Nenhuma turma cadastrada.")
        return False
    else:
        for i in range(len(turmas)):
            print(f"\nTurma {i+1}:")
            print(f"  Código: {turmas[i]['codigo']}")
            print(f"  Nome: {turmas[i]['nome']}")
            print(f"  Período: {turmas[i]['periodo']}")
            print(f"  Alunos: {len(turmas[i]['alunos'])}")
        return True

def listar_atividades():
    """Lista todas as atividades cadastradas"""
    print("\n=== ATIVIDADES CADASTRADAS ===")

    if len(atividades) == 0:
        print("Nenhuma atividade cadastrada.")
        return False
    else:


        for i in range(len(atividades)):
            print(f"\nAtividade {i+1}:")
            print(f"  Turma: {atividades[i]['turma']}")
            print(f"  Título: {atividades[i]['titulo']}")
            print(f"  Disciplina: {atividades[i]['disciplina']}")
            print(f"  Data de entrega: {atividades[i]['data_entrega']}")
            print(f"  Peso: {atividades[i]['peso']:.1f}")
            print(f"  Notas lançadas: {len(atividades[i]['notas'])}")
        return True

# ========== FUNÇÕES DE GERENCIAMENTO DE PROFESSORES ==========

def cadastrar_professor(usuario_logado):
    """Cadastra um novo professor no sistema (apenas admin)"""
    print("\n=== CADASTRAR PROFESSOR ===")

    # Verificar se o usuário logado é admin
    if not usuario_logado.get('is_admin', False):
        print("\n⚠️  ACESSO NEGADO!")
        print("Apenas o administrador do sistema pode cadastrar professores.")
        pausar()
        return

    cpf = input("CPF do professor (será o login) ou 0 para cancelar: ")
    if cpf == '0':
        return

    nome = input("Nome completo: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    professor = {
        'cpf': cpf,
        'nome': nome,
        'email': email,
        'senha': senha,
        'is_admin': False
    }

    professores.append(professor)
    print(f"\nProfessor '{nome}' cadastrado com sucesso!")
    pausar()

# ========== FUNÇÕES DE LOGIN ==========

def fazer_login(perfil):
    """Realiza o login do usuário (Professor ou Aluno)"""
    print(f"\n=== LOGIN - {perfil.upper()} ===")



    if perfil == 'professor':
        identificador = input("CPF (ou 0 para cancelar): ")
        if identificador == '0':
            return None
        indice = buscar_professor(identificador)
        if indice is not None:
            usuario = professores[indice]
        else:
            print("Professor não encontrado.")
            pausar()
            return None

    elif perfil == 'aluno':
        identificador = input("RA (ou 0 para cancelar): ")
        if identificador == '0':
            return None
        indice = buscar_aluno(identificador)
        if indice is not None:
            usuario = alunos[indice]
        else:
            print("Aluno não encontrado.")
            pausar()
            return None

    else:
        return None

    senha = input("Senha: ")

    if usuario['senha'] == senha:
        print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario['nome']}!")
        pausar()
        return usuario
    else:
        print("\nSenha incorreta.")
        pausar()
        return None

# ========== FUNÇÕES DE GERENCIAMENTO DE TURMAS ==========

def cadastrar_turma():
    """Cadastra uma nova turma no sistema"""
    print("\n=== CADASTRAR TURMA ===")

    codigo = input("Código da turma (ou 0 para cancelar): ")
    if codigo == '0':
        return

    nome = input("Nome da turma: ")



    # Validação de período com opções pré-definidas
    print("\nSelecione o período:")
    print("1. Manhã")
    print("2. Tarde")
    print("3. Noite")
    print("0. Cancelar")

    while True:
        opcao_periodo = input("Escolha uma opção (1-3 ou 0): ")
        if opcao_periodo == '0':
            return
        elif opcao_periodo == '1':
            periodo = 'Manhã'
            break
        elif opcao_periodo == '2':
            periodo = 'Tarde'
            break
        elif opcao_periodo == '3':
            periodo = 'Noite'
            break
        else:
            print("Opção inválida! Escolha 1, 2, 3 ou 0 para cancelar.")

    turma = {
        'codigo': codigo,
        'nome': nome,
        'periodo': periodo,
        'alunos': []
    }

    turmas.append(turma)
    print(f"\nTurma '{nome}' cadastrada com sucesso no período {periodo}!")
    pausar()

# ========== FUNÇÕES DE GERENCIAMENTO DE ALUNOS ==========

def cadastrar_aluno():
    """Cadastra um novo aluno no sistema e permite vincular a uma turma"""
    print("\n=== CADASTRAR ALUNO ===")

    ra = input("RA do aluno (será o login) ou 0 para cancelar: ")
    if ra == '0':
        return

    # Verificar se o aluno já existe
    if buscar_aluno(ra) is not None:
        print(f"\n⚠️  Aluno com RA '{ra}' já está cadastrado no sistema!")
        pausar()


        return

    nome = input("Nome completo: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    aluno = {
        'ra': ra,
        'nome': nome,
        'email': email,
        'senha': senha,
        'turma': None,
        'notas': []
    }

    alunos.append(aluno)
    print(f"\nAluno '{nome}' cadastrado com sucesso!")

    # Vincular aluno à turma automaticamente
    if listar_turmas():
        codigo_turma = input("\nDeseja vincular o aluno a uma turma agora? Digite o Código da turma (ou ENTER para pular): ")
        if codigo_turma:
            indice_turma = buscar_turma(codigo_turma)
            if indice_turma is not None:
                # Vincular
                alunos[buscar_aluno(ra)]['turma'] = turmas[indice_turma]['codigo']
                turmas[indice_turma]['alunos'].append(ra)
                print(f"Aluno '{nome}' vinculado à turma '{turmas[indice_turma]['nome']}'!")

    pausar()

def listar_alunos():
    """Lista todos os alunos cadastrados"""
    print("\n=== ALUNOS CADASTRADOS ===")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for i in range(len(alunos)):
            print(f"\nAluno {i+1}:")
            print(f"  RA: {alunos[i]['ra']}")
            print(f"  Nome: {alunos[i]['nome']}")
            print(f"  E-mail: {alunos[i]['email']}")

            if alunos[i]['turma'] is not None:
                print(f"  Turma: {alunos[i]['turma']}")


            else:
                print(f"  Turma: Não vinculado")

    pausar()

def vincular_aluno_turma():
    """Vincula um aluno a uma turma ou transfere para outra turma"""
    print("\n=== VINCULAR/TRANSFERIR ALUNO ===")

    ra = input("RA do aluno (ou 0 para cancelar): ")
    if ra == '0':
        return

    indice_aluno = buscar_aluno(ra)

    if indice_aluno is None:
        print("Aluno não encontrado.")
        pausar()
        return

    # Verificar se aluno já está em uma turma
    turma_atual = alunos[indice_aluno]['turma']
    if turma_atual is not None:
        print(f"\n⚠️  O aluno '{alunos[indice_aluno]['nome']}' já está vinculado à turma '{turma_atual}'.")
        print("\nDeseja transferir o aluno para outra turma?")
        confirmacao = input("Digite 'S' para transferir ou qualquer tecla para cancelar: ").upper()
        if confirmacao != 'S':
            pausar()
            return

        # Remover aluno da turma atual
        indice_turma_atual = buscar_turma(turma_atual)
        if indice_turma_atual is not None:
            if ra in turmas[indice_turma_atual]['alunos']:
                turmas[indice_turma_atual]['alunos'].remove(ra)

    if not listar_turmas():
        pausar()
        return

    codigo_turma = input("\nCódigo da turma para vincular/transferir (ou 0 para cancelar): ")
    if codigo_turma == '0':
        return

    indice_turma = buscar_turma(codigo_turma)



    if indice_turma is None:
        print("Turma não encontrada.")
        pausar()
        return

    # Vincular à nova turma
    alunos[indice_aluno]['turma'] = turmas[indice_turma]['codigo']

    # Evita duplicidade na lista de alunos da turma
    if ra not in turmas[indice_turma]['alunos']:
        turmas[indice_turma]['alunos'].append(ra)

    if turma_atual is not None:
        print(f"\nAluno '{alunos[indice_aluno]['nome']}' transferido para a turma '{turmas[indice_turma]['nome']}'!")
    else:
        print(f"\nAluno '{alunos[indice_aluno]['nome']}' vinculado à turma '{turmas[indice_turma]['nome']}'!")
    pausar()

# ========== FUNÇÕES DE GERENCIAMENTO DE AULAS ==========

def cadastrar_aula():
    """Cadastra uma nova aula para uma turma com validação de data"""
    print("\n=== CADASTRAR AULA ===")

    if not listar_turmas():
        pausar()
        return

    codigo_turma = input("\nCódigo da turma (ou 0 para cancelar): ")
    if codigo_turma == '0':
        return

    indice_turma = buscar_turma(codigo_turma)

    if indice_turma is None:
        print("Turma não encontrada.")
        pausar()
        return

    while True:
        data = input("Data da aula (DD/MM/AAAA) ou 0 para cancelar: ")
        if data == '0':
            return
        if validar_data(data):
            break
        print("Formato de data inválido. Use DD/MM/AAAA.")



    disciplina = input("Disciplina: ")
    conteudo = input("Conteúdo ministrado: ")

    aula = {
        'turma': codigo_turma,
        'data': data,
        'disciplina': disciplina,
        'conteudo': conteudo,
        'presencas': []
    }

    aulas.append(aula)
    print(f"\nAula de '{disciplina}' cadastrada para a turma '{turmas[indice_turma]['nome']}'!")
    pausar()

def listar_aulas():
    """Lista todas as aulas cadastradas"""
    print("\n=== AULAS CADASTRADAS ===")

    if len(aulas) == 0:
        print("Nenhuma aula cadastrada.")
    else:
        for i in range(len(aulas)):
            print(f"\nAula {i+1}:")
            print(f"  Turma: {aulas[i]['turma']}")
            print(f"  Data: {aulas[i]['data']}")
            print(f"  Disciplina: {aulas[i]['disciplina']}")
            print(f"  Conteúdo: {aulas[i]['conteudo']}")

    pausar()

def registrar_presenca():
    """Registra a presença dos alunos em uma aula específica"""
    print("\n=== REGISTRAR PRESENÇA ===")

    if len(aulas) == 0:
        print("Nenhuma aula cadastrada para registrar presença.")
        pausar()
        return

    listar_aulas()

    while True:
        try:
            entrada = input("\nNúmero da aula para registrar presença (ou 0 para cancelar): ")
            if entrada == '0':
                return


            num_aula = int(entrada)
            if 1 <= num_aula <= len(aulas):
                aula_selecionada = aulas[num_aula - 1]
                break
            else:
                print("Aula inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    codigo_turma = aula_selecionada['turma']
    indice_turma = buscar_turma(codigo_turma)

    if indice_turma is None:
        print("Erro: Turma da aula não encontrada.")
        pausar()
        return

    alunos_turma = turmas[indice_turma]['alunos']

    if len(alunos_turma) == 0:
        print("Nenhum aluno vinculado a esta turma.")
        pausar()
        return

    print(f"\nRegistrando presença para a aula de {aula_selecionada['disciplina']} em {aula_selecionada['data']}")
    print(f"Turma: {codigo_turma}")

    for ra in alunos_turma:
        indice_aluno = buscar_aluno(ra)
        if indice_aluno is not None:
            nome_aluno = alunos[indice_aluno]['nome']
            while True:
                status = input(f"{nome_aluno} (RA: {ra}) - (P)resente ou (F)alta? ").upper()
                if status in ['P', 'F']:
                    break
                print("Entrada inválida. Digite 'P' para Presente ou 'F' para Falta.")

            registro = {
                'ra': ra,
                'turma': codigo_turma,
                'data': aula_selecionada['data'],
                'disciplina': aula_selecionada['disciplina'],
                'status': status
            }

            frequencia.append(registro)


            aula_selecionada['presencas'].append(ra if status == 'P' else None)

    print("\nPresença registrada com sucesso!")
    pausar()

# ========== FUNÇÕES DE GERENCIAMENTO DE ATIVIDADES ==========

def cadastrar_atividade():
    """Cadastra uma nova atividade/avaliação para uma turma"""
    print("\n=== CADASTRAR ATIVIDADE ===")

    if not listar_turmas():
        pausar()
        return

    codigo_turma = input("\nCódigo da turma (ou 0 para cancelar): ")
    if codigo_turma == '0':
        return

    indice_turma = buscar_turma(codigo_turma)

    if indice_turma is None:
        print("Turma não encontrada.")
        pausar()
        return

    titulo = input("Título da atividade: ")
    disciplina = input("Disciplina: ")

    while True:
        data_entrega = input("Data de entrega (DD/MM/AAAA) ou 0 para cancelar: ")
        if data_entrega == '0':
            return
        if validar_data(data_entrega):
            break
        print("Formato de data inválido. Use DD/MM/AAAA.")

    while True:
        try:
            peso = float(input("Peso da atividade (valor positivo): "))
            if peso > 0:
                break
            else:
                print("Peso deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número.")



    atividade = {
        'turma': codigo_turma,
        'titulo': titulo,
        'disciplina': disciplina,
        'data_entrega': data_entrega,
        'peso': peso,
        'notas': {}
    }

    atividades.append(atividade)
    print(f"\nAtividade '{titulo}' cadastrada para a turma '{turmas[indice_turma]['nome']}'!")
    pausar()

def atribuir_nota():
    """Atribui nota a um aluno em uma atividade específica"""
    print("\n=== ATRIBUIR NOTA ===")

    if not listar_atividades():
        pausar()
        return

    while True:
        try:
            entrada = input("\nNúmero da atividade (ou 0 para cancelar): ")
            if entrada == '0':
                return
            num_atividade = int(entrada)
            if 1 <= num_atividade <= len(atividades):
                atividade_selecionada = atividades[num_atividade - 1]
                break
            else:
                print("Atividade inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    ra = input("RA do aluno (ou 0 para cancelar): ")
    if ra == '0':
        return

    indice_aluno = buscar_aluno(ra)

    if indice_aluno is None:
        print("Aluno não encontrado.")
        pausar()
        return

    while True:
        try:


            nota = float(input(f"Nota para {alunos[indice_aluno]['nome']} (0-10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    atividade_selecionada['notas'][ra] = nota
    print(f"\nNota {nota:.2f} atribuída a {alunos[indice_aluno]['nome']} na atividade '{atividade_selecionada['titulo']}'!")
    pausar()

# ========== FUNÇÕES DE CÁLCULO E RELATÓRIOS ==========

def calcular_media_aluno(ra):
    """Calcula a média ponderada de um aluno"""
    notas_aluno = []
    soma_pesos = 0

    for i in range(len(atividades)):
        if ra in atividades[i]['notas']:
            nota_ponderada = atividades[i]['notas'][ra] * atividades[i]['peso']
            notas_aluno.append(nota_ponderada)
            soma_pesos += atividades[i]['peso']

    if len(notas_aluno) == 0 or soma_pesos == 0:
        return 0, 0

    soma_notas_ponderadas = sum(notas_aluno)
    media = soma_notas_ponderadas / soma_pesos

    return media, len(notas_aluno)

def exibir_media_aluno():
    """Calcula e exibe a média de um aluno"""
    print("\n=== CALCULAR MÉDIA DO ALUNO ===")

    ra = input("RA do aluno (ou 0 para cancelar): ")
    if ra == '0':
        return

    indice_aluno = buscar_aluno(ra)

    if indice_aluno is None:
        print("Aluno não encontrado.")
        pausar()


        return

    media, total_atividades = calcular_media_aluno(ra)

    if total_atividades == 0:
        print(f"\nO aluno '{alunos[indice_aluno]['nome']}' não possui notas cadastradas.")
    else:
        print(f"\n=== RESULTADO ===")
        print(f"Aluno: {alunos[indice_aluno]['nome']}")
        print(f"Total de atividades com nota: {total_atividades}")
        print(f"Média Ponderada: {media:.2f}")

        if media >= 7.0:
            print("Situação: APROVADO")
        elif media >= 5.0:
            print("Situação: RECUPERAÇÃO")
        else:
            print("Situação: REPROVADO")

    pausar()

def visualizar_historico(aluno_logado):
    """Exibe o histórico escolar (resumo de desempenho) do aluno logado"""
    print("\n=== HISTÓRICO ESCOLAR ===")

    ra_aluno = aluno_logado['ra']
    media, total_atividades = calcular_media_aluno(ra_aluno)

    print(f"Aluno: {aluno_logado['nome']} (RA: {ra_aluno})")

    if total_atividades == 0:
        print("\nNenhum registro de notas para gerar o histórico.")
        pausar()
        return

    # 1. Calcular Frequência Geral
    registros_aluno = [reg for reg in frequencia if reg['ra'] == ra_aluno]
    total_aulas = len(registros_aluno)
    presencas = len([reg for reg in registros_aluno if reg['status'] == 'P'])

    frequencia_geral = (presencas / total_aulas) * 100 if total_aulas > 0 else print("\nRESUMO GERAL:")
    print(f"Média Ponderada Geral: {media:.2f}")
    print(f"Frequência Geral: {frequencia_geral:.2f}%")

    # 2. Situação Final


    situacao_media = ""
    if media >= 7.0:
        situacao_media = "APROVADO POR MÉDIA"
    elif media >= 5.0:
        situacao_media = "RECUPERAÇÃO"
    else:
        situacao_media = "REPROVADO POR MÉDIA"

    situacao_frequencia = "APROVADO POR FREQUÊNCIA" if frequencia_geral >= 75.0 else "REPROVADO POR FREQUÊNCIA"

    print(f"\nSITUAÇÃO FINAL:")
    print(f"Situação por Média: {situacao_media}")
    print(f"Situação por Frequência: {situacao_frequencia}")

    if media >= 7.0 and frequencia_geral >= 75.0:
        print("\nRESULTADO FINAL: APROVADO")
    else:
        print("\nRESULTADO FINAL: REPROVADO")

    pausar()

def visualizar_calendario(aluno_logado):
    """Exibe o calendário de aulas e avaliações do aluno logado"""
    print("\n=== CALENDÁRIO DE AULAS E AVALIAÇÕES ===")

    ra_aluno = aluno_logado['ra']
    turma_aluno = aluno_logado['turma']

    if turma_aluno is None:
        print("Aluno não está vinculado a nenhuma turma.")
        pausar()
        return

    print(f"Aluno: {aluno_logado['nome']} (Turma: {turma_aluno})")

    eventos = []

    # 1. Aulas
    for aula in aulas:
        if aula['turma'] == turma_aluno:
            eventos.append({
                'tipo': 'AULA',
                'data': aula['data'],
                'descricao': f"Aula de {aula['disciplina']} - Conteúdo: {aula['conteudo']}"
            })

    # 2. Atividades/Avaliações


    for atividade in atividades:
        if atividade['turma'] == turma_aluno:
            eventos.append({
                'tipo': 'AVALIAÇÃO',
                'data': atividade['data_entrega'],
                'descricao': f"Entrega da Atividade: {atividade['titulo']} ({atividade['disciplina']})"
            })

    if not eventos:
        print("Nenhum evento (aula ou avaliação) encontrado para sua turma.")
        pausar()
        return

    eventos_ordenados = sorted(eventos, key=lambda x: (x['tipo'], x['data']))

    print("\nEVENTOS ORDENADOS:")
    for evento in eventos_ordenados:
        print(f"[{evento['tipo']}] {evento['data']} - {evento['descricao']}")

    pausar()

def cadastrar_boleto():
    """Cadastra um novo boleto/informação financeira"""
    print("\n=== CADASTRAR BOLETO/FINANCEIRO ===")

    ra = input("RA do aluno (ou 0 para cancelar): ")
    if ra == '0':
        return

    indice_aluno = buscar_aluno(ra)

    if indice_aluno is None:
        print("Aluno não encontrado.")
        pausar()
        return

    aluno = alunos[indice_aluno]

    # Descrição do boleto - apenas Mensalidade
    mes_ano = input("\nInforme o mês/ano da mensalidade (Ex: Janeiro/2024) ou 0 para cancelar: ")
    if mes_ano == '0':
        return
    descricao = f"Mensalidade {mes_ano}"

    while True:
        try:
            valor = float(input("Valor (R$): "))


            if valor > 0:
                break
            else:
                print("Valor deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    while True:
        data_vencimento = input("Data de Vencimento (DD/MM/AAAA) ou 0 para cancelar: ")
        if data_vencimento == '0':
            return
        if validar_data(data_vencimento):
            break
        print("Formato de data inválido. Use DD/MM/AAAA.")

    # Validação de status com opções pré-definidas
    print("\nSelecione o status do boleto:")
    print("1. Pendente")
    print("2. Pago")
    print("3. Vencido")
    print("0. Cancelar")

    while True:
        opcao_status = input("Escolha uma opção (1-3 ou 0): ")
        if opcao_status == '0':
            return
        elif opcao_status == '1':
            status = "Pendente"
            break
        elif opcao_status == '2':
            status = "Pago"
            break
        elif opcao_status == '3':
            status = "Vencido"
            break
        else:
            print("Opção inválida! Escolha 1, 2, 3 ou 0 para cancelar.")

    boleto = {
        'ra': ra,
        'descricao': descricao,
        'valor': valor,
        'vencimento': data_vencimento,
        'status': status
    }

    financas.append(boleto)
    print(f"\nBoleto para {aluno['nome']} cadastrado com sucesso!")


    pausar()

def visualizar_financeiro(aluno_logado):
    """Exibe as informações financeiras (boletos) do aluno logado"""
    print("\n=== INFORMAÇÕES FINANCEIRAS ===")

    ra_aluno = aluno_logado['ra']

    boletos_aluno = [b for b in financas if b['ra'] == ra_aluno]

    if not boletos_aluno:
        print("Nenhum boleto ou informação financeira encontrada.")
        pausar()
        return

    print(f"Aluno: {aluno_logado['nome']} (RA: {ra_aluno})")

    for i, boleto in enumerate(boletos_aluno):
        print(f"\n--- Boleto {i+1} ---")
        print(f"  Descrição: {boleto['descricao']}")
        print(f"  Valor: R$ {boleto['valor']:.2f}")
        print(f"  Vencimento: {boleto['vencimento']}")
        print(f"  Status: {boleto['status']}")

    pausar()

def relatorio_turma():
    """Gera relatório completo de uma turma"""
    print("\n=== RELATÓRIO DA TURMA ===")

    if not listar_turmas():
        pausar()
        return

    codigo_turma = input("\nCódigo da turma (ou 0 para cancelar): ")
    if codigo_turma == '0':
        return

    indice_turma = buscar_turma(codigo_turma)

    if indice_turma is None:
        print("Turma não encontrada.")
        pausar()
        return

    print(f"\n{'='*50}")
    print(f"RELATÓRIO - {turmas[indice_turma]['nome']}")
    print(f"{'='*50}")
    print(f"Código: {turmas[indice_turma]['codigo']}")


    print(f"Período: {turmas[indice_turma]['periodo']}")
    print(f"Total de alunos: {len(turmas[indice_turma]['alunos'])}")

    # Contar aulas da turma
    aulas_turma = 0
    for aula in aulas:
        if aula['turma'] == codigo_turma:
            aulas_turma = aulas_turma + 1

    print(f"Total de aulas: {aulas_turma}")

    # Contar atividades da turma
    atividades_turma = 0
    for atividade in atividades:
        if atividade['turma'] == codigo_turma:
            atividades_turma = atividades_turma + 1

    print(f"Total de atividades: {atividades_turma}")

    print(f"\nALUNOS DA TURMA:")
    for ra in turmas[indice_turma]['alunos']:
        indice = buscar_aluno(ra)
        if indice is not None:
            print(f"  - {alunos[indice]['nome']} (RA: {ra})")

    pausar()

# ========== FUNÇÕES DE GERENCIAMENTO DE MENSAGENS ==========

def enviar_mensagem(remetente_tipo, remetente_id):
    """Permite ao usuário logado enviar uma mensagem para outro usuário"""
    print("\n=== ENVIAR MENSAGEM ===")

    if remetente_tipo == 'professor':
        destinatario_tipo = input("Enviar para (A)luno ou (P)rofessor? (ou 0 para cancelar): ").upper()
        if destinatario_tipo == '0':
            return
        if destinatario_tipo == 'A':
            destinatario_tipo = 'aluno'
            destinatario_id = input("RA do aluno: ")
            if buscar_aluno(destinatario_id) is None:
                print("Aluno não encontrado.")
                pausar()
                return
        elif destinatario_tipo == 'P':
            destinatario_tipo = 'professor'
            destinatario_id = input("CPF do professor: ")
            if buscar_professor(destinatario_id) is None:


                print("Professor não encontrado.")
                pausar()
                return
        else:
            print("Opção inválida.")
            pausar()
            return

    elif remetente_tipo == 'aluno':
        destinatario_tipo = input("Enviar para (A)luno ou (P)rofessor? (ou 0 para cancelar): ").upper()
        if destinatario_tipo == '0':
            return
        if destinatario_tipo == 'A':
            destinatario_tipo = 'aluno'
            destinatario_id = input("RA do aluno: ")
            if buscar_aluno(destinatario_id) is None:
                print("Aluno não encontrado.")
                pausar()
                return
        elif destinatario_tipo == 'P':
            destinatario_tipo = 'professor'
            destinatario_id = input("CPF do professor: ")
            if buscar_professor(destinatario_id) is None:
                print("Professor não encontrado.")
                pausar()
                return
        else:
            print("Opção inválida.")
            pausar()
            return

    assunto = input("Assunto: ")
    corpo = input("Mensagem: ")

    mensagem = {
        'remetente_tipo': remetente_tipo,
        'remetente_id': remetente_id,
        'destinatario_tipo': destinatario_tipo,
        'destinatario_id': destinatario_id,
        'assunto': assunto,
        'corpo': corpo,
        'lida': False
    }

    mensagens.append(mensagem)
    print("\nMensagem enviada com sucesso!")
    pausar()



def visualizar_mensagens(usuario_tipo, usuario_id):
    """Exibe as mensagens recebidas pelo usuário logado"""
    print("\n=== MENSAGENS RECEBIDAS ===")

    mensagens_usuario = [m for m in mensagens if m['destinatario_tipo'] == usuario_tipo and m['destinatario_id'] == usuario_id]

    if not mensagens_usuario:
        print("Nenhuma mensagem recebida.")
        pausar()
        return

    for i, msg in enumerate(mensagens_usuario):
        status = "[LIDA]" if msg['lida'] else "[NÃO LIDA]"
        print(f"\n--- Mensagem {i+1} {status} ---")
        print(f"De: {msg['remetente_tipo'].capitalize()} ({msg['remetente_id']})")
        print(f"Assunto: {msg['assunto']}")
        print(f"Mensagem: {msg['corpo']}")
        msg['lida'] = True

    pausar()

# ========== FUNÇÕES DE GERENCIAMENTO DE EQUIPAMENTOS ==========

def listar_equipamentos():
    """Lista todos os equipamentos disponíveis"""
    print("\n=== EQUIPAMENTOS DISPONÍVEIS ===")

    for equip in equipamentos:
        status = f"[{equip['disponibilidade'].upper()}]"
        print(f"\nID: {equip['id']} - {equip['nome']} {status}")
        print(f"  Nota de Avaliação: {equip['nota']:.1f}/5.0 ({equip['total_avaliacoes']} avaliações)")

        if equip['disponibilidade'] == 'em uso':
            print(f"  Em uso por: CPF {equip['locador_cpf']}")
            print(f"  Data de Locação: {equip['data_locacao']}")
            print(f"  Prazo de Devolução: {equip['data_devolucao']}")

def alugar_equipamento(professor_logado):
    """Permite ao professor alugar um equipamento"""
    print("\n=== ALUGAR EQUIPAMENTO ===")

    listar_equipamentos()

    # Verificar se professor já tem equipamento alugado
    for equip in equipamentos:
        if equip['locador_cpf'] == professor_logado['cpf']:


            print(f"\nVocê já possui um equipamento alugado: {equip['nome']} (ID: {equip['id']})")
            print("Devolva o equipamento atual antes de alugar outro.")
            pausar()
            return

    while True:
        try:
            entrada = input("\nDigite o ID do equipamento que deseja alugar (ou 0 para cancelar): ")
            if entrada == '0':
                return
            id_equip = int(entrada)

            indice = buscar_equipamento(id_equip)
            if indice is None:
                print("Equipamento não encontrado.")
                continue

            if equipamentos[indice]['disponibilidade'] == 'em uso':
                print("Este equipamento já está em uso. Escolha outro.")
                continue

            break
        except ValueError:
            print("Entrada inválida. Digite um número.")

    # Solicitar data de locação
    while True:
        data_locacao = input("Data da locação (DD/MM/AAAA) ou 0 para cancelar: ")
        if data_locacao == '0':
            return
        if validar_data(data_locacao):
            break
        print("Formato de data inválido. Use DD/MM/AAAA.")

    # Calcular data de devolução (7 dias após a locação)
    data_devolucao = adicionar_dias(data_locacao, 7)

    if data_devolucao is None:
        print("Erro ao calcular data de devolução.")
        pausar()
        return

    # Registrar a locação
    equipamentos[indice]['disponibilidade'] = 'em uso'
    equipamentos[indice]['locador_cpf'] = professor_logado['cpf']
    equipamentos[indice]['data_locacao'] = data_locacao


    equipamentos[indice]['data_devolucao'] = data_devolucao

    print(f"\n{'='*50}")
    print("LOCAÇÃO REALIZADA COM SUCESSO!")
    print(f"{'='*50}")
    print(f"Equipamento: {equipamentos[indice]['nome']}")
    print(f"Data de Locação: {data_locacao}")
    print(f"Prazo de Devolução: {data_devolucao}")
    print(f"\nLembre-se de devolver o equipamento até a data limite!")
    pausar()

def devolver_equipamento(professor_logado):
    """Permite ao professor devolver um equipamento alugado"""
    print("\n=== DEVOLVER EQUIPAMENTO ===")

    cpf_professor = professor_logado['cpf']

    # Buscar equipamento alugado pelo professor
    equipamento_alugado = None
    indice_equip = None

    for i, equip in enumerate(equipamentos):
        if equip['locador_cpf'] == cpf_professor:
            equipamento_alugado = equip
            indice_equip = i
            break

    if equipamento_alugado is None:
        print("Você não possui nenhum equipamento alugado no momento.")
        pausar()
        return

    # Exibir informações do equipamento
    print(f"\n{'='*50}")
    print("EQUIPAMENTO ALUGADO")
    print(f"{'='*50}")
    print(f"ID: {equipamento_alugado['id']}")
    print(f"Nome: {equipamento_alugado['nome']}")
    print(f"Data de Locação: {equipamento_alugado['data_locacao']}")
    print(f"Prazo de Devolução: {equipamento_alugado['data_devolucao']}")
    print(f"Nota Atual: {equipamento_alugado['nota']:.1f}/5.0")

    # Confirmar devolução
    confirmacao = input("\nDeseja efetuar a devolução deste equipamento? (S/N): ").upper()

    if confirmacao != 'S':
        print("Devolução cancelada.")
        pausar()


        return

    # Solicitar avaliação obrigatória
    while True:
        try:
            avaliacao = float(input("\nAvalie o equipamento (0 a 5): "))
            if 0 <= avaliacao <= 5:
                break
            else:
                print("Avaliação deve estar entre 0 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    # Calcular nova nota do equipamento (média ponderada)
    nota_atual = equipamento_alugado['nota']
    total_avaliacoes = equipamento_alugado['total_avaliacoes']

    nova_nota = ((nota_atual * total_avaliacoes) + avaliacao) / (total_avaliacoes + 1)

    # Atualizar equipamento
    equipamentos[indice_equip]['disponibilidade'] = 'disponível'
    equipamentos[indice_equip]['locador_cpf'] = None
    equipamentos[indice_equip]['data_locacao'] = None
    equipamentos[indice_equip]['data_devolucao'] = None
    equipamentos[indice_equip]['nota'] = nova_nota
    equipamentos[indice_equip]['total_avaliacoes'] = total_avaliacoes + 1

    print(f"\n{'='*50}")
    print("DEVOLUÇÃO REALIZADA COM SUCESSO!")
    print(f"{'='*50}")
    print(f"Equipamento: {equipamento_alugado['nome']}")
    print(f"Sua Avaliação: {avaliacao:.1f}/5.0")
    print(f"Nova Nota do Equipamento: {nova_nota:.1f}/5.0")
    print(f"\nObrigado por utilizar nossos equipamentos!")
    pausar()

# ========== FUNÇÕES DE VISUALIZAÇÃO PARA ALUNOS ==========

def visualizar_notas(aluno_logado):
    """Exibe as notas do aluno logado"""
    print("\n=== MINHAS NOTAS ===")

    ra_aluno = aluno_logado['ra']

    notas_encontradas = False

    for atividade in atividades:
        if ra_aluno in atividade['notas']:


            notas_encontradas = True
            print(f"\n--- {atividade['titulo']} ---")
            print(f"Disciplina: {atividade['disciplina']}")
            print(f"Data de Entrega: {atividade['data_entrega']}")
            print(f"Peso: {atividade['peso']:.1f}")
            print(f"Nota: {atividade['notas'][ra_aluno]:.2f}")

    if not notas_encontradas:
        print("Nenhuma nota cadastrada.")
    else:
        # Exibir média
        media, total = calcular_media_aluno(ra_aluno)
        print(f"\n{'='*50}")
        print(f"MÉDIA PONDERADA GERAL: {media:.2f}")
        print(f"{'='*50}")

    pausar()

def visualizar_frequencia_aluno(aluno_logado):
    """Exibe a frequência do aluno logado"""
    print("\n=== MINHA FREQUÊNCIA ===")

    ra_aluno = aluno_logado['ra']

    registros_aluno = [reg for reg in frequencia if reg['ra'] == ra_aluno]

    if not registros_aluno:
        print("Nenhum registro de frequência encontrado.")
        pausar()
        return

    total_aulas = len(registros_aluno)
    presencas = len([reg for reg in registros_aluno if reg['status'] == 'P'])
    faltas = total_aulas - presencas

    percentual = (presencas / total_aulas) * 100 if total_aulas > 0 else 0

    print(f"\nAluno: {aluno_logado['nome']}")
    print(f"Total de Aulas: {total_aulas}")
    print(f"Presenças: {presencas}")
    print(f"Faltas: {faltas}")
    print(f"Percentual de Frequência: {percentual:.2f}%")

    if percentual >= 75.0:
        print("Situação: Frequência Adequada")
    else:
        print("Situação: Abaixo do Mínimo (Risco de Reprovação)")

    print("\nDETALHES:")


    for reg in registros_aluno:
        status_texto = "PRESENTE" if reg['status'] == 'P' else "FALTA"
        print(f"  {reg['data']} - {reg['disciplina']}: {status_texto}")

    pausar()

# ========== MENUS DE PERFIL ==========

def menu_professor(professor_logado):
    """Exibe o menu da área do Professor"""
    while True:
        limpar_tela()
        print("\n" + "="*50)
        print("ÁREA DO PROFESSOR")
        print("="*50)
        print(f"Bem-vindo(a), {professor_logado['nome']}")
        print("="*50)
        print("1.  Cadastrar Turma")
        print("2.  Listar Turmas")
        print("3.  Cadastrar Aluno")
        print("4.  Listar Alunos")
        print("5.  Vincular/Transferir Aluno")
        print("6.  Cadastrar Aula")
        print("7.  Listar Aulas")
        print("8.  Registrar Presença")
        print("9.  Cadastrar Atividade")
        print("10. Atribuir Nota")
        print("11. Listar Atividades")
        print("12. Cadastrar Boleto/Financeiro")
        print("13. Relatório da Turma")
        print("14. Alugar Equipamento")
        print("15. Devolver Equipamento")
        print("16. Mensagens (Enviar/Visualizar)")
        if professor_logado.get('is_admin', False):
            print("17. Cadastrar Professor (Admin)")
        print("0.  Voltar ao Menu Principal")
        print("="*50)

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            cadastrar_turma()
        elif opcao == "2":
            limpar_tela()
            listar_turmas()
            pausar()
        elif opcao == "3":
            limpar_tela()


            cadastrar_aluno()
        elif opcao == "4":
            limpar_tela()
            listar_alunos()
        elif opcao == "5":
            limpar_tela()
            vincular_aluno_turma()
        elif opcao == "6":
            limpar_tela()
            cadastrar_aula()
        elif opcao == "7":
            limpar_tela()
            listar_aulas()
        elif opcao == "8":
            limpar_tela()
            registrar_presenca()
        elif opcao == "9":
            limpar_tela()
            cadastrar_atividade()
        elif opcao == "10":
            limpar_tela()
            atribuir_nota()
        elif opcao == "11":
            limpar_tela()
            listar_atividades()
            pausar()
        elif opcao == "12":
            limpar_tela()
            cadastrar_boleto()
        elif opcao == "13":
            limpar_tela()
            relatorio_turma()
        elif opcao == "14":
            limpar_tela()
            alugar_equipamento(professor_logado)
        elif opcao == "15":
            limpar_tela()
            devolver_equipamento(professor_logado)
        elif opcao == "16":
            limpar_tela()
            print("\n--- MENU MENSAGENS ---")
            print("1. Enviar Mensagem")
            print("2. Visualizar Mensagens")
            op_msg = input("Escolha uma opção: ")
            if op_msg == '1':
                enviar_mensagem('professor', professor_logado['cpf'])
            elif op_msg == '2':
                visualizar_mensagens('professor', professor_logado['cpf'])
            else:


                print("Opção inválida.")
                pausar()
        elif opcao == "17" and professor_logado.get('is_admin', False):
            limpar_tela()
            cadastrar_professor(professor_logado)
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            pausar()

def menu_aluno(aluno_logado):
    """Exibe o menu da área do Aluno"""
    while True:
        limpar_tela()
        print("\n" + "="*50)
        print("ÁREA DO ALUNO")
        print("="*50)
        print(f"Bem-vindo(a), {aluno_logado['nome']}")
        print("="*50)
        print("1.  Visualizar Notas")
        print("2.  Visualizar Frequência")
        print("3.  Visualizar Histórico Escolar")
        print("4.  Visualizar Calendário (Aulas/Avaliações)")
        print("5.  Informações Financeiras (Boletos)")
        print("6.  Mensagens (Enviar/Visualizar)")
        print("0.  Voltar ao Menu Principal")
        print("="*50)

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            visualizar_notas(aluno_logado)
        elif opcao == "2":
            limpar_tela()
            visualizar_frequencia_aluno(aluno_logado)
        elif opcao == "3":
            limpar_tela()
            visualizar_historico(aluno_logado)
        elif opcao == "4":
            limpar_tela()
            visualizar_calendario(aluno_logado)
        elif opcao == "5":
            limpar_tela()
            visualizar_financeiro(aluno_logado)
        elif opcao == "6":
            limpar_tela()
            print("\n--- MENU MENSAGENS ---")


            print("1. Enviar Mensagem")
            print("2. Visualizar Mensagens")
            op_msg = input("Escolha uma opção: ")
            if op_msg == '1':
                enviar_mensagem('aluno', aluno_logado['ra'])
            elif op_msg == '2':
                visualizar_mensagens('aluno', aluno_logado['ra'])
            else:
                print("Opção inválida.")
                pausar()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            pausar()

# ========== MENU PRINCIPAL ==========

def exibir_menu_principal():
    """Exibe o menu principal de seleção de perfil"""
    print("\n" + "="*50)
    print("SISTEMA ACADÊMICO INTEGRADO")
    print("="*50)
    print("1.  Acessar como Professor")
    print("2.  Acessar como Aluno")
    print("0.  Sair")
    print("="*50)

def main():
    """Função principal do sistema"""
    # Inicializar sistema com dados pré-definidos
    inicializar_sistema()

    limpar_tela()
    print("\n*** BEM-VINDO AO SISTEMA ACADÊMICO ETEC ***")

    print("\nINSTRUÇÕES:")
    print("- Digite o número da opção desejada e pressione ENTER.")
    print("- Em qualquer menu, a opção '0' permite voltar ao menu anterior ou sair do sistema.")
    print("- O sistema não salva os dados. Eles serão perdidos ao encerrar o programa.")
    print("\nUSUÁRIO ADMINISTRADOR PADRÃO:")
    print("  CPF: admin")
    print("  Senha: admin123")

    pausar()

    opcao = ""



    while opcao != "0":
        limpar_tela()
        exibir_menu_principal()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            professor = fazer_login('professor')
            if professor:
                menu_professor(professor)
        elif opcao == "2":
            limpar_tela()
            aluno = fazer_login('aluno')
            if aluno:
                menu_aluno(aluno)
        elif opcao == "0":
            limpar_tela()
            print("\n*** Encerrando o sistema... ***")
            print("Obrigado por usar o Sistema Acadêmico ETEC!")
        else:
            print("\nOpção inválida! Tente novamente.")
            pausar()

# Executar o programa
if __name__ == "__main__":
    main()