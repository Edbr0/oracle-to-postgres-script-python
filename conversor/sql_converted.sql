
-- AUTO-GENERATED DEFINITION
CREATE TABLE TISS_CONTA_ATEND
(
    NR_SEQUENCIA             INTEGER   NOT NULL
        CONSTRAINT TISSCOA_PK
            PRIMARY KEY,
    NR_INTERNO_CONTA         INTEGER,
    DT_ATUALIZACAO           TIMESTAMP         NOT NULL,
    NM_USUARIO               VARCHAR(15) NOT NULL,
    DT_ENTRADA               TIMESTAMP,
    DT_ALTA                  TIMESTAMP,
    IE_TIPO_INTERNACAO       VARCHAR(10),
    IE_REGIME_INTERNACAO     VARCHAR(2),
    IE_CARATER_INTERNACAO    VARCHAR(2),
    IE_TIPO_ACOMODACAO       VARCHAR(30),
    IE_OBSTETRICA            VARCHAR(2),
    CD_PESSOA_FISICA         VARCHAR(10) NOT NULL,
    NM_PESSOA_FISICA         VARCHAR(100),
    NR_CARTAO_NAC_SUS        INTEGER,
    CD_CONVENIO              INTEGER,
    DS_PLANO                 VARCHAR(100),
    DT_VALIDADE_CARTEIRA     TIMESTAMP,
    CD_USUARIO_CONVENIO      VARCHAR(30),
    IE_MOTIVO_SAIDA          VARCHAR(2),
    CD_CID                   VARCHAR(10),
    CD_CID_2                 VARCHAR(10),
    CD_CID_3                 VARCHAR(10),
    CD_CID_4                 VARCHAR(10),
    CD_CID_OBITO             VARCHAR(10),
    NR_DECLARACAO_OBITO      VARCHAR(20),
    IE_OBITO_MULHER          VARCHAR(2),
    IE_GESTACAO              VARCHAR(2),
    IE_ABORTO                VARCHAR(2),
    IE_TRANSTORNO            VARCHAR(2),
    IE_COMPLIC_PUERPERIO     VARCHAR(2),
    QT_OBITO_PRECOCE         INTEGER,
    QT_OBITO_TARDIO          INTEGER,
    QT_NASC_VIVO             INTEGER,
    QT_NASC_MORTO            INTEGER,
    QT_NASC_PREMATURO        INTEGER,
    NR_DNV                   VARCHAR(255),
    IE_COMPLIC_NEONATAL      VARCHAR(2),
    IE_BAIXO_PESO            VARCHAR(2),
    IE_CESAREO               VARCHAR(2),
    IE_NORMAL                VARCHAR(2),
    IE_ATEND_RN              VARCHAR(2),
    CD_CGC_HOSP              VARCHAR(14),
    DS_RAZAO_SOCIAL          VARCHAR(100),
    CD_CNES                  VARCHAR(30),
    DS_TIPO_FATUR            VARCHAR(30),
    NR_ATENDIMENTO           INTEGER,
    CD_TABELA_CID            VARCHAR(10),
    DS_CID                   VARCHAR(255),
    IE_TIPO_CID              VARCHAR(5),
    IE_UNIDADE_TEMPO_CID     VARCHAR(10),
    QT_TEMPO_CID             INTEGER,
    IE_TIPO_ACIDENTE         VARCHAR(2),
    CD_TABELA_CID_2          VARCHAR(20),
    DS_CID_2                 VARCHAR(255),
    CD_TABELA_CID_OBITO      VARCHAR(20),
    DS_CID_OBITO             VARCHAR(255),
    IE_TIPO_CONSULTA         VARCHAR(40),
    IE_TIPO_SAIDA_CONSULTA   VARCHAR(40),
    IE_COMPLIC_NEONATAL_XML  VARCHAR(10),
    IE_BAIXO_PESO_XML        VARCHAR(10),
    IE_CESAREO_XML           VARCHAR(10),
    IE_NORMAL_XML            VARCHAR(10),
    IE_COMPLIC_PUERPERIO_XML VARCHAR(10),
    IE_ATEND_RN_XML          VARCHAR(10),
    IE_ABORTO_XML            VARCHAR(10),
    IE_GESTACAO_XML          VARCHAR(10),
    IE_TRANSTORNO_XML        VARCHAR(10),
    NR_SEQ_MED_FATUR         INTEGER,
    NR_ATEND_MED             INTEGER,
    NR_SEQ_PROT_MED          INTEGER,
    NR_SEQ_REAP_CONTA        INTEGER,
    NR_SEQ_LOTE_HIST         INTEGER,
    IE_ATENDIMENTO_RN        VARCHAR(1),
    CD_VALIDACAO_TISS        VARCHAR(2),
    CD_AUSENCIA_COD_VALID    VARCHAR(2),
    NR_DFM                   VARCHAR(40),
    NR_COBERTURA_ESPEC       VARCHAR(3),
    IE_SAUDE_OCUPACIONAL     VARCHAR(3),
    CD_REGIME_ATENDIMENTO    VARCHAR(3)
)
