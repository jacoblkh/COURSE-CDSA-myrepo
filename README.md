# COURSE-CDSA-myrepo
NUS ISS Course: Containers for Deploying and Scaling Apps, pre assessment

# Setup (Macbook)
create new virtual environment
python3 -m venv course-cdsa-venv

activate the new virtual environment
source course-cdsa-venv/bin/activate

download requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

run the python application
uvicorn main:app --reload