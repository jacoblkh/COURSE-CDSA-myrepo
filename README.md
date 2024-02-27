# COURSE-CDSA-myrepo
NUS ISS Course: Containers for Deploying and Scaling Apps, pre assessment

# Setup (Macbook)
create new virtual environment
python3 -m venv course-cdsa-venv

activate the new virtual environment
source course-cdsa-venv/bin/activate

run the python application
uvicorn workshop01.backend.main:app --reload