while ! nc -z $VERTICA_HOST $VERTICA_PORT; do
      sleep 0.1
done
python main.py
