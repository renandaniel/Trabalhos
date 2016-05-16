#!/bin/bash

DIRECTORY="$(dirname "$0")"


# Init

echo "Entrando em: $DIRECTORY"
cd "$DIRECTORY"


# Estilo de código

flake8 minhacaixa
if [ "$?" -ne "0" ]; then
  echo 'ERRO: Estilo de código incorreto'
  exit 1
fi


# Criar estutura

psql -U postgres -c 'CREATE DATABASE minhacaixa'
DATABASE_URL='postgres://postgres@127.0.0.1/minhacaixa' python -m minhacaixa.initialdata
if [ "$?" -ne "0" ]; then
  echo 'ERRO: Falha ao criar estrutura'
  exit 1
fi
