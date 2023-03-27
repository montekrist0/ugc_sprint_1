while ! nc -z $VERTICA_HOST $VERTICA_PORT; do
      sleep 5.0
done
python main.py
