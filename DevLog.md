# 🛠️ DevLog – CIR Backend

## July 29, 2025

### 🔹 Database Connection
- Working on `feature/connect-db` branch
- Established connection with database using Beanie (Pydantic ODM)
- Added 3 endpoints for monitoring database health:
  - `/test_db_write` 
  - `/test_db_read`
  - `/test_db_cleanup` 
- Configured MongoDB connection with environment variables
- Successfully tested all endpoints and verified database connectivity


## July 26, 2025

### 🔹 Project Initialization
- Created a new branch from `main` named `project-structure`
- Started setting up the backend structure:
  - Base FastAPI app
  - Project folder layout
  - Planning to connect MongoDB using Beanie (Pydantic ODM)
  - Added `/health` route for initial testing
