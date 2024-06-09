# Citizens Issues Registry

The Citizens Issues Registry is a web application that allows citizens to log in, create accounts, read posts uploaded by others, upvote/downvote posts, and submit their own posts to highlight issues around their region. This platform serves as a social media tool to bring attention to local problems and foster community engagement.

## Features

- User Authentication: Register and log in to access the platform.
- Post Creation: Submit posts highlighting issues in your region.
- Post Interaction: Read, upvote, and downvote posts.
- Responsive Design: Accessible on both desktop and mobile devices.

## Installation

### Prerequisites

- Node.js (v14.x or later)
- npm (v6.x or later)

### Clone the Repository

```bash
git clone https://github.com/your-username/citizens-issues-registry.git
cd citizens-issues-registry
```

### Install Dependencies

```bash
# Install server dependencies
cd backend
npm install

# Install client dependencies
cd ../frontend
npm install
```

### Run the Application

#### Backend

```bash
cd backend
npm start
```

The backend server will run on `http://localhost:5000`.

#### Frontend

```bash
cd frontend
npm start
```

The frontend application will run on `http://localhost:3000`.

## Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Register a new account or log in with existing credentials.
3. Browse posts, upvote/downvote issues, and create new posts to highlight issues in your region.

## Technology Stack

- **Frontend**: ReactJS, MaterialUI
- **Backend**: Node.js, Express.js
- **Database**: JSON files (for simple data storage, consider using MongoDB or another database for production)
- **State Management**: React Hooks
- **Styling**: MaterialUI

## Contributing

We welcome contributions! To contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.


