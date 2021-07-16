# Temperatur - the temperature converter
[![Frontend](https://github.com/emushtaq/temperatur/actions/workflows/node.js.yml/badge.svg)](https://github.com/emushtaq/temperatur/actions/workflows/node.js.yml)

[![Backend](https://github.com/emushtaq/temperatur/actions/workflows/main.yml/badge.svg)](https://github.com/emushtaq/temperatur/actions/workflows/main.yml)

[![CI to Docker Hub (only tagged versions)](https://github.com/emushtaq/temperatur/actions/workflows/deploy_images.yml/badge.svg?branch=v0.0.1)](https://github.com/emushtaq/temperatur/actions/workflows/deploy_images.yml)

A sample project running a React frontend applicatoin and a FastAPI backed python backend application. It is packaged using a `docker-compose.yml`.

### To run the application with Docker (RECOMMENDED):
- Clone this repository
- Ensure that Docker, Docker compose
- Enter the repository directory and execute `docker-compose up -d`
- Allow a few minutes for the containers to be built (Took ~3min on my machine)
- If everything goes well, you should notice  
    ```
    Creating temperatur-fastAPI  ... done
    Creating temperatur-frontend ... done
    ```
- Access the frontend of the application at http://localhost:3001

### To run the application locally:
- Clone this repository
- Ensure that a python environment (3.9) and node >10 is present and working
- For the frontend
  - `cd frontend` and execute `npm install`
  - after the dependencies are installed, run `npm start`
  - the frontend should be up and running at http://localhost:3000
- For the backend
  - `cd backend`
  - optionally create a virtual environment for python 3.9 and activate it. [Link to some reference](https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/)
  - install the requirements with `pip install -r requirements.txt`
  - once dependencies are installed, execute `uvicorn app.main:app --host 0.0.0.0 --port 80`
  - the backend should be up and running at http://localhost:80
  - Swagger UI based API docs are available on http://localhost:80/docs#/

### CI:
The following Github Actions are setup
- [Python Backend](https://github.com/emushtaq/temperatur/blob/master/.github/workflows/main.yml) Builds and tests and backend application. Triggered on every push and PR to master branch
- [React Frontend](https://github.com/emushtaq/temperatur/blob/master/.github/workflows/node.js.yml) Builds and tests and backend application. Triggered on every push and PR to master branch
- [CI to Docker Hub](https://github.com/emushtaq/temperatur/blob/master/.github/workflows/deploy_images.yml) Builds the FE and BE docker images and publishes them to Docker Hub. Triggered when commits are tagged with the format `v*.*.*`
    - [Front end image](https://hub.docker.com/repository/docker/eshmeister/temperatur-frontend)
    - [Back end image](https://hub.docker.com/repository/docker/eshmeister/temperatur-backend) 

### Tests:
- Backend tests are located in the [Test folder](backend/app/test)
- Frontend tests are located in the [Test file](frontend/src/App.test.js)
- These tests are executed automatically using GitHub actions on every push. Runs can be viewed [here](https://github.com/emushtaq/temperatur/actions)
- To run backend tests locally
  - ensure required environment is setup (as mentioned above in the running application locally - backend section)
  - cd backend
  - execute the tests by running `pytest`. This will automatically pick up the test for the controller and the service layer and execute them.
- To run frontend tests locally
  - ensure required frontend dependencies are installed by running `cd frontend` & `npm install`
  - `run npm test`

### TO-DO:
- Fix `Each child in a list should have a unique "key" prop` error on the FE.
- Improve validation and add more test cases 
- Enhance error handling (both FE and BE)
- Reduce image size (eg: package for production)
- Deploy on heroku
