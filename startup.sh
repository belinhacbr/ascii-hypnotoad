if [ ! -d "env" ]; then
    virtualenv env -p python3
fi
source env/bin/activate
pip install -r requirements.txt
python3 alltheglory.py
