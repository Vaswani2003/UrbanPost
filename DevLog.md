# 🛠️ DevLog – CIR Backend

## October 3, 2025

### 🔹 User Schema & Endpoint

- Created **`User` model** with Beanie `Document`:
  - Split into `PersonalInfo` and `AccountDetails` for clean separation of personal vs account data.
  - Added `UserRoles` enum to manage roles: `CITIZEN`, `AUTHORITY`, `ADMIN`, `SUPER_ADMIN`.
  - Configured `id` as `PydanticObjectId` with alias `_id` for MongoDB compatibility.
  - Added collection name and indexes for username and email in `Settings`.

- Defined **Pydantic viewmodels** for API:
  - `CreateUserRequest`:
    - Fields required for creating a user: `first_name`, `last_name`, `email`, `username`, `password`.
    - Optional fields: `middle_name`, `phone_number`, `date_of_birth`, `recovery_email`, `recovery_phone`.
  - `CreateUserResponse`:
    - Returns safe user information excluding sensitive fields like `password_hash`.
    - Includes `id`, `username`, `email`, role, active status, timestamps, and basic personal info.

- Implemented **endpoint definition** for creating a new user:
  - Route: `POST /auth/create-user`
  - Request body: `CreateUserRequest`
  - Response model: `CreateUserResponse`
  - Setup stub with FastAPI `APIRouter` for later integration with service function.


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
