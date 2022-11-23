import re
import os
from time import sleep


print("################  CONVERSOR OTP #############################")

print("-----------------TIPOS DE SQL---------------------------------")


print("1 -CREATE TABLE     2-SELECT     3-Procedores / Functions")


sql_type = int(input('Qual o tipo de sql deseja converter? '))


sql = """
-- auto-generated definition
create table TISS_CONTA_ATEND
(
    NR_SEQUENCIA             NUMBER(10)   not null
        constraint TISSCOA_PK
            primary key,
    NR_INTERNO_CONTA         NUMBER(15),
    DT_ATUALIZACAO           DATE         not null,
    NM_USUARIO               VARCHAR2(15) not null,
    DT_ENTRADA               DATE,
    DT_ALTA                  DATE,
    IE_TIPO_INTERNACAO       VARCHAR2(10),
    IE_REGIME_INTERNACAO     VARCHAR2(2),
    IE_CARATER_INTERNACAO    VARCHAR2(2),
    IE_TIPO_ACOMODACAO       VARCHAR2(30),
    IE_OBSTETRICA            VARCHAR2(2),
    CD_PESSOA_FISICA         VARCHAR2(10) not null,
    NM_PESSOA_FISICA         VARCHAR2(100),
    NR_CARTAO_NAC_SUS        NUMBER(20),
    CD_CONVENIO              NUMBER(15),
    DS_PLANO                 VARCHAR2(100),
    DT_VALIDADE_CARTEIRA     DATE,
    CD_USUARIO_CONVENIO      VARCHAR2(30),
    IE_MOTIVO_SAIDA          VARCHAR2(2),
    CD_CID                   VARCHAR2(10),
    CD_CID_2                 VARCHAR2(10),
    CD_CID_3                 VARCHAR2(10),
    CD_CID_4                 VARCHAR2(10),
    CD_CID_OBITO             VARCHAR2(10),
    NR_DECLARACAO_OBITO      VARCHAR2(20),
    IE_OBITO_MULHER          VARCHAR2(2),
    IE_GESTACAO              VARCHAR2(2),
    IE_ABORTO                VARCHAR2(2),
    IE_TRANSTORNO            VARCHAR2(2),
    IE_COMPLIC_PUERPERIO     VARCHAR2(2),
    QT_OBITO_PRECOCE         NUMBER(5),
    QT_OBITO_TARDIO          NUMBER(5),
    QT_NASC_VIVO             NUMBER(5),
    QT_NASC_MORTO            NUMBER(5),
    QT_NASC_PREMATURO        NUMBER(5),
    NR_DNV                   VARCHAR2(255),
    IE_COMPLIC_NEONATAL      VARCHAR2(2),
    IE_BAIXO_PESO            VARCHAR2(2),
    IE_CESAREO               VARCHAR2(2),
    IE_NORMAL                VARCHAR2(2),
    IE_ATEND_RN              VARCHAR2(2),
    CD_CGC_HOSP              VARCHAR2(14),
    DS_RAZAO_SOCIAL          VARCHAR2(100),
    CD_CNES                  VARCHAR2(30),
    DS_TIPO_FATUR            VARCHAR2(30),
    NR_ATENDIMENTO           NUMBER(10),
    CD_TABELA_CID            VARCHAR2(10),
    DS_CID                   VARCHAR2(255),
    IE_TIPO_CID              VARCHAR2(5),
    IE_UNIDADE_TEMPO_CID     VARCHAR2(10),
    QT_TEMPO_CID             NUMBER(15),
    IE_TIPO_ACIDENTE         VARCHAR2(2),
    CD_TABELA_CID_2          VARCHAR2(20),
    DS_CID_2                 VARCHAR2(255),
    CD_TABELA_CID_OBITO      VARCHAR2(20),
    DS_CID_OBITO             VARCHAR2(255),
    IE_TIPO_CONSULTA         VARCHAR2(40),
    IE_TIPO_SAIDA_CONSULTA   VARCHAR2(40),
    IE_COMPLIC_NEONATAL_XML  VARCHAR2(10),
    IE_BAIXO_PESO_XML        VARCHAR2(10),
    IE_CESAREO_XML           VARCHAR2(10),
    IE_NORMAL_XML            VARCHAR2(10),
    IE_COMPLIC_PUERPERIO_XML VARCHAR2(10),
    IE_ATEND_RN_XML          VARCHAR2(10),
    IE_ABORTO_XML            VARCHAR2(10),
    IE_GESTACAO_XML          VARCHAR2(10),
    IE_TRANSTORNO_XML        VARCHAR2(10),
    NR_SEQ_MED_FATUR         NUMBER(10),
    NR_ATEND_MED             NUMBER(10),
    NR_SEQ_PROT_MED          NUMBER(10),
    NR_SEQ_REAP_CONTA        NUMBER(10),
    NR_SEQ_LOTE_HIST         NUMBER(10),
    IE_ATENDIMENTO_RN        VARCHAR2(1),
    CD_VALIDACAO_TISS        VARCHAR2(2),
    CD_AUSENCIA_COD_VALID    VARCHAR2(2),
    NR_DFM                   VARCHAR2(40),
    NR_COBERTURA_ESPEC       VARCHAR2(3),
    IE_SAUDE_OCUPACIONAL     VARCHAR2(3),
    CD_REGIME_ATENDIMENTO    VARCHAR2(3)
)
/

create index TISSCOA_ATEPACI_FK_I
    on TISS_CONTA_ATEND (NR_ATENDIMENTO)
/

create index TISSCOA_CONPACI_FK_I
    on TISS_CONTA_ATEND (NR_INTERNO_CONTA)
/

create index TISSCOA_PESFISI_FK_I
    on TISS_CONTA_ATEND (CD_PESSOA_FISICA)
/

create index TISSCOA_MEDFATU_FK_I
    on TISS_CONTA_ATEND (NR_SEQ_MED_FATUR)
/

create index TISSCOA_MEDATEN_FK_I
    on TISS_CONTA_ATEND (NR_ATEND_MED)
/

create index TISSCOA_MEDPRCO_FK_I
    on TISS_CONTA_ATEND (NR_SEQ_PROT_MED)
/

create index TISSCOA_TISSREC_FK_I
    on TISS_CONTA_ATEND (NR_SEQ_REAP_CONTA)
/

create index TISSCOA_LOTAUHI_FK_I
    on TISS_CONTA_ATEND (NR_SEQ_LOTE_HIST)
/



                                          
 """


def printLoading(text):
    i = 0
    while i < 5:
        os.system('clear') or None
        print(text+('.' * i))
        i += 1
        sleep(0.5)


# Função para converter sql de cração de tabela
def convertOracleToPostgresCreateTable(sqlOracle):
    printLoading('Convertendo sql.. Aguarde ')
    textConverted = str(sqlOracle).upper().split('/')[0].replace('TASY.', 'MANAGER.').replace('TASY', 'MANAGER').replace('SAMEL', 'MANAGER').replace('SAMEL.', 'MANAGER.').replace(
        'APPV2.', 'APP.').replace('APPV2', 'APPV2').replace('/', ';').replace('VARCHAR2', 'VARCHAR').replace('CLOB', 'TEXT').replace('BLOB', 'TEXT').replace('DATE', 'TIMESTAMP')
    regex = re.sub(
        r"(([B-U]){6})\(+([0-9]?)+((\,)+\s)?\w+\)?", "INTEGER", textConverted)
    print('Sql convetido com sucesso!')
    return regex


# Função para converter funções e trigres ainda não está 100% então sempre validar se foi convertido corretamente
def convertOracleToPostgresSelect(sqlOracle):
    printLoading('Convertendo sql.. Aguarde ')
    textConverted = str(sqlOracle).upper().replace('TASY.', 'MANAGER.').replace('TASY', 'MANAGER').replace('SAMEL', 'MANAGER').replace('SAMEL.', 'MANAGER.').replace(
        'APPV2.', 'APP.').replace('APPV2', 'APP').replace('/', ';').replace('CLOB', 'TEXT').replace('BLOB', 'TEXT').replace('VARCHAR2', 'VARCHAR')
    replaceTrunc = textConverted.replace('TRUNC(', "DATE_TRUNC('day',")
    replaceTrunSysdate = replaceTrunc.replace('TRUNC(SYSDATE)', 'CURRENT_DATE')
    replaceSysdateToTimestamp = replaceTrunSysdate.replace(
        'SYSDATE', 'CURRENT_TIME_STAMP')
    replaceNvltoCoalesce = replaceSysdateToTimestamp.replace('NVL', 'COALESCE')
    replaceRownumToLimit = replaceNvltoCoalesce.replace('ROWNUM', '||')
    replaceFirstFetchToLimit = replaceRownumToLimit.replace(
        'FETCH FIRST', 'LIMIT').replace('ROWS ONLY', '')
    removeAnd = re.sub(r"([AND])+\s+([||])+(\s?)+\=",
                       "LIMIT", replaceFirstFetchToLimit)
    print('Sql convetido com sucesso!')
    return removeAnd


# Função para converter funções e trigres ainda não está 100% então sempre validar se foi convertido corretamente
def convertOracleToPostgresFunctionsOrProcedores(sqlOracle):
    printLoading('Convertendo sql.. Aguarde ')
    textConverted = str(sqlOracle).upper().replace('TASY.', 'MANAGER.').replace('TASY', 'MANAGER').replace('SAMEL', 'MANAGER').replace('SAMEL.', 'MANAGER.').replace('APPV2.', 'APP.').replace('APPV2', 'APP').replace(
        '/', ';').replace('CLOB', 'TEXT').replace('BLOB', 'TEXT').replace('VARCHAR2', 'VARCHAR').replace('PROCEDURE', 'FUNCTION').replace("""CREATE OR REPLACE""",  """CREATE""").replace("""CREATE""",  """CREATE OR REPLACE""")
    replaceNumberToInteger = re.sub(
        r"(([B-U]){6})\(+([0-9]?)+((\,)+\s)?\w+\)?", "INTEGER", textConverted).replace('NUMBER', 'INTEGER')
    replaceIsToReturnAS = re.sub(
        r"(IS)\W", "\n RETURNS /*COLOCAR TIPO DE RETORNO AQUI*/ AS $$   \n\n DECLARE \n\n", replaceNumberToInteger, 1)
    replaceLastEND = re.sub(
        r"(END)\W[^IF][^LOOP]\w+\;", "END \n $$  LANGUAGE plpgsql;", replaceIsToReturnAS)
    replaceTrunc = replaceLastEND.replace('TRUNC(', "DATE_TRUNC('day',")
    replaceTrunSysdate = replaceTrunc.replace('TRUNC(SYSDATE)', 'CURRENT_DATE')
    replaceSysdateToTimestamp = replaceTrunSysdate.replace(
        'SYSDATE', 'CURRENT_TIME_STAMP')
    replaceNvltoCoalesce = replaceSysdateToTimestamp.replace('NVL', 'COALESCE')
    replaceRownumToLimit = replaceNvltoCoalesce.replace('ROWNUM', '||')
    replaceFirstFetchToLimit = replaceRownumToLimit.replace(
        'FETCH FIRST', 'LIMIT').replace('ROWS ONLY', '')
    removeAnd = re.sub(r"([AND])+\s+([||])+(\s?)+\=",
                       "LIMIT", replaceFirstFetchToLimit)
    print('Sql convetido com sucesso!')
    return removeAnd


# colocar o caminho do arquivo que deseja aramazenar o sql
myFile = open("/home/eduardo/Documents/conversor/sql_converted.sql", "w")

if sql_type == 1:
    myFile.write(convertOracleToPostgresCreateTable(sql))
elif sql_type == 2:
    myFile.write(convertOracleToPostgresSelect(sql))
elif sql_type == 3:
    myFile.write(convertOracleToPostgresFunctionsOrProcedores(sql))
else:
    print("ERRO: Menu inválido!")
