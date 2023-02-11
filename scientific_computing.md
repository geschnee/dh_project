
# Anleitung

https://www.sc.uni-leipzig.de/user-doc/quickstart/hpc/#copy-data-from-and-to-the-sc-systems

# Schritte

AnyConnect VPN

Browser:
https://lab.sc.uni-leipzig.de/jupyter/hub/login?next=%2Fjupyter%2Fhub%2F
User:
gf346tmau
passwort:
rwzegi pws

# SSH

ssh gf346tmau@login01.sc.uni-leipzig.de

# SCP

scp metadata.parquet gf346tmau@login01.sc.uni-leipzig.de:/home/sc.uni-leipzig.de/gf346tmau

# Pip

erst das venv aktivieren:
[gf346tmau@login01 ~]$ source venv/py39/bin/activate
(py39) [gf346tmau@login01 ~]$ pip install pyarrow


# Conda

conda activate my_env

https://www.sc.uni-leipzig.de/user-doc/quickstart/jupyter/#using-conda

Jupyter Notebook funktioniert hiermit