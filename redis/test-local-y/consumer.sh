threshold=30000     
delay_process=4     

redis-cli DBSIZE >/dev/null
if ! [ $? = 0 ]; then
    echo "Erreur, pas de connexion avec le serveur redis!"
    exit 1
fi

while :
do
    nb=$(redis-cli --raw LLEN mafile)
    if [ $nb -gt 0 ]; then
        val=$(redis-cli --raw RPOP mafile)

        if [ $val -gt $threshold ]; then
            echo "ALARME ! Valeur = $val"
            sleep $delay_process
        fi
    else
        echo "Liste vide, attente 2s."
        sleep 3
    fi
done

