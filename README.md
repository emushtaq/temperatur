# Temperatur - the temperature converter

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

### Tests:
- Backend tests are located in the [Test folder](backend/app/test)
- To run tests locally
  - ensure required environment is setup (as mentioned above in the running application locally - backend section)
  - cd backend
  - execute the tests by running `pytest`. This will automatically pick up the test for the controller and the service layer and execute them.

### TO-DO:
- Improve validation and add test cases on the frontend 
- Enhance error handling
- Reduce image size (eg: package for production)
- Try a CI/CD setup with actions 
- Explore publishing and hosting in Heroku