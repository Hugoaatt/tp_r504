redis-cli DBSIZE >/dev/null
if ! [ $? = 0 ]
then
	echo "Erreur, pas de connection avec le serveur redis!"
	exit 1
fi
