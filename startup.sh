if [ ! -d "env" ]; then
    virtualenv env -p python3
fi
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=alltheglory.py
python -m flask run --host=0.0.0.0
