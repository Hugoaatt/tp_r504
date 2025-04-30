#!/bin/bash


n=1000       
delay=3      


redis-cli DBSIZE >/dev/null
if ! [ $? = 0 ]; then
    echo "Erreur, pas de connexion avec le serveur redis!"
    exit 1
fi

while :
do
    for ((i=0; i<n; i++)); do
        redis-cli LPUSH mafile $RANDOM >/dev/null
    done

    taille=$(redis-cli LLEN mafile)
    echo "Taille de la liste : $taille"
    sleep $delay
done
