const express = require('express');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const fs = require('fs-extra');
const bodyParser = require('body-parser');
const path = require('path');

// -------------------------------------------------------------------------------------- //

const app = express();
const port = 5000;

app.use(cors());
app.use(bodyParser.json());
app.use(express.urlencoded({ extended: true }));

const multer = require('multer');

const storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, 'uploads/');
    },
    filename: function(req, file, cb) {
        cb(null, file.originalname);
    }
});

// -------------------------------------------------------------------------------------- //

const upload = multer({ storage: storage });

const SECRET_KEY = 'hackathon_three'; 

function generateToken(username) {
    return jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
}

// -------------------------------------------------------------------------------------- //

const userExists = (email, password) => {
    try {
        const users = JSON.parse(fs.readFileSync('users.json', 'utf-8'));
        return users.some(user => user.email === email && user.password === password);
    } catch (error) {
        console.error('Error reading or parsing users.json', error);
        return false;
    }
};

// -------------------------------------------------------------------------------------- //

function addUser(name, email, password) {
    let users;
    try {
        users = JSON.parse(fs.readFileSync('users.json', 'utf-8'));
    } catch (error) {
        console.error('Error reading or parsing users.json', error);
        users = [];
    }

    users.push({ name, email, password });
    fs.writeFileSync('users.json', JSON.stringify(users, null, 2));

    return true;
}

// -------------------------------------------------------------------------------------- //

app.post('/posts', upload.single('image'), async (req, res) => {
    const {title, category, description, timestamp} = req.body;
    const image = req.file;

    const username = "Vinamra";
    
    const post = { title, category, description, timestamp, imageName: image.originalname, username };

    try{
        const postsPath = path.join(__dirname, 'posts.json');
        let posts = [];

        if (fs.existsSync(postsPath)) {
            posts = JSON.parse(fs.readFileSync(postsPath, 'utf-8'));
        }

        posts.push(post);

        await fs.writeJson(postsPath, posts, { spaces: 2 });

        res.status(201).json({ success: true, message: 'Post created successfully' });
    }
    catch(error){
        console.error('Error creating post:', error);
        res.status(500).json({ success: false, message: 'Error creating post' });
    }
});

// -------------------------------------------------------------------------------------- //

app.get('/sendPosts', (req, res) => {
    

    fs.readFile(path.join(__dirname, 'posts.json'), 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            res.status(500).send('An error occurred while reading the posts file.');
        } else {
            res.send(JSON.parse(data));
        }
    });
});

// -------------------------------------------------------------------------------------- //

app.post('/signup', async (req, res) => {
    const { name, email, password } = req.body;

    const userAddedSuccessfully = await addUser(name, email, password);

    if (userAddedSuccessfully) {
        res.json({ success: true, message: `Signup successful, added user ${name}, ${email}` });
    }
    else {
        res.json({ success: false, message: 'Signup failed' });
    }
});

// -------------------------------------------------------------------------------------- //

app.post('/login', (req, res) => {
    const { email, password } = req.body;
    if (userExists(email, password)) {
        const token = jwt.sign( { email: email }, SECRET_KEY, { expiresIn: '1h' } 
        );

        res.json({ success: true, message: 'User exists', token: token });
    } else {
        res.json({ success: false, message: 'Login failed' });
    }
});

// -------------------------------------------------------------------------------------- //

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
