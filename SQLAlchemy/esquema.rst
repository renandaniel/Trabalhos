Esquema do Banco
================

**Grupo** (**codigo**, nome, razao_social, cnpj)

**Cliente** (**codigo**, nome, rua, cidade, nascimento)

**Agencia** (**codigo**, nome, cidade, fundos, *grupo_codigo*)

**Conta** (*agencia_codigo*, **numero**, *cliente_codigo*, saldo, abertura)

**Emprestimo** (*agencia_codigo*, *cliente_codigo*, **codigo**, total)

**Depositante** (**codigo**, *agencia_codigo*, *conta_numero*, *cliente_codigo*, valor, data)

**Devedor** (**codigo**, *agencia_codigo*, *cliente_codigo*, *emprestimo_codigo*, saldo)

**CartaoCredito** (*agencia_codigo*, *cliente_codigo*, **codigo**, limite)
