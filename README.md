# Full Stack Test Project

This is a full stack application built with Svelte for the frontend and FastAPI for the backend. The application fetches cryptocurrency market information from the CoinGecko API and displays it.

## Project Structure

full-stack-test-project/
├── my-svelte-project/
│ ├── public/
│ ├── src/
│ │ ├── App.svelte
│ │ ├── main.js
│ ├── package.json
│ ├── rollup.config.js
│ ├── ... (other Svelte project files)
├── my-fastapi-backend/
│ ├── main.py
│ ├── venv/
│ ├── Pipfile (if using pipenv)
│ ├── Pipfile.lock (if using pipenv)
├── README.md

## Frontend (Svelte)

### Prerequisites

- Node.js and npm

### Setup Instructions

1. Navigate to the frontend directory:

   ```bash
   cd my-svelte-project
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   npm run dev
   ```

4. The frontend application will be available at `http://localhost:5000`.

### Project Structure

- `public/`: Contains static assets
- `src/`: Contains the Svelte components and main application code
  - `App.svelte`: Main Svelte component that fetches and displays cryptocurrency data
  - `main.js`: Entry point for the Svelte application

### Fetching Data from Backend

The frontend fetches cryptocurrency data from the backend FastAPI server running at `http://localhost:8000/cryptos`.

## Backend (FastAPI)

### Prerequisites

- Python 3.6+
- `pip` (Python package installer)
- `pipenv` (optional, for managing virtual environments and dependencies)

### Setup Instructions

1. Navigate to the backend directory:

   ```bash
   cd my-fastapi-backend
   ```

2. Create and activate a virtual environment:

   - Using `venv`:

     - On macOS/Linux:

       ```bash
       python -m venv venv
       source venv/bin/activate
       ```

     - On Windows:
       ```bash
       python -m venv venv
       venv\Scripts\activate
       ```

   - Using `pipenv` (optional):

     ```bash
     pipenv install
     pipenv shell
     ```

3. Install dependencies:

   ```bash
   pip install fastapi uvicorn requests
   ```

4. Run the development server:

   ```bash
   uvicorn main:app --reload
   ```

5. The backend API will be available at `http://localhost:8000`.

### Project Structure

- `main.py`: Main FastAPI application that defines the `/cryptos` endpoint

### API Endpoint

- `GET /cryptos`: Fetches cryptocurrency market data from the CoinGecko API

## Running the Application

### Starting the Backend

1. Navigate to the backend directory:

   ```bash
   cd my-fastapi-backend
   ```

2. Start the backend server:

   ```bash
   uvicorn main:app --reload
   ```

### Starting the Frontend

1. Navigate to the frontend directory:

   ```bash
   cd my-svelte-project
   ```

2. Start the frontend development server:

   ```bash
   npm run dev
   ```

### Accessing the Application

Open your browser and go to `http://localhost:5000` to see the application in action.

## Additional Notes

- Ensure both the frontend and backend servers are running simultaneously to fetch and display the data correctly.
- If you encounter any CORS issues, ensure that the FastAPI application has CORS middleware configured to allow requests from the frontend.

### CORS Configuration in FastAPI

- Add the following to `main.py` to enable CORS:

  ```python
  from fastapi.middleware.cors import CORSMiddleware

  app = FastAPI()

  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],  # Allows all origins
      allow_credentials=True,
      allow_methods=["*"],  # Allows all methods
      allow_headers=["*"],  # Allows all headers
  )
  ```

This `README.md` provides comprehensive instructions for setting up, running, and understanding both the frontend and backend parts of the project. If you need further customization or have additional questions, feel free to ask!
