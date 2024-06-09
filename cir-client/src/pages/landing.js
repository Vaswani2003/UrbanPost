import React, { useState, useEffect } from 'react';
import { Box,Typography,TextField, Link, Button } from '@mui/material';
import Masonry from '@mui/lab/Masonry';
import { useNavigate } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';
// Components
import Navbar from '../components/navbar';

//icons
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import HomeIcon from '@mui/icons-material/Home';
import NotificationsActiveIcon from '@mui/icons-material/NotificationsActive';
import ViewComfyIcon from '@mui/icons-material/ViewComfy'


export default function Landing() {
  const Navigate = useNavigate();
  const [posts, setPosts] = useState([]);
  const token = localStorage.getItem('token'); 

  let Username = 'Vinamra'; 
  if (token) {
    const decodedToken = jwtDecode(token);
    Username = decodedToken.username; 
  }

  useEffect(() => {
    fetch('http://localhost:5000/sendPosts')
        .then(response => response.json())
        .then(data => setPosts(data));
}, []);
  

  return (
    <div style={{ display: 'flex', height: '100vh' }}>

      {/* Vertical component (20%) */}
      <div style={{ width: '20%', backgroundColor: 'white' }}>
       
       <AccountCircleIcon style={{ fontSize: 50, color: 'black', marginBottom: '5px', marginTop: '10px', marginLeft: '130px' }} />
       
       <Typography variant="h6" component="div" sx={{ color: 'black', marginTop: '10px', marginLeft: '110px', marginBottom: '20px' }}>{Username}</Typography>
       
       <div style={{ borderTop: '3px solid grey', width: '100%' }}></div>
      
       <ul style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '20px', padding: 0, listStyle: 'none' }}>
{/* ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           */}        
         <li>
           <div style={{ display: 'flex', justifyContent: 'space-around', marginTop: '20px' }}>
             <TextField id="outlined-basic" label="Search" variant="outlined" />
           </div>
         </li>
{/* ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           */}
         <li>
           <Button>
             <div style={{ display: 'flex', marginTop: '20px', marginLeft: '30px' }}>
               <HomeIcon style={{ fontSize: 30, color: 'black', marginRight: '30px' }} />
               <Typography variant="h6" onClick={() => { Navigate('/landing') }} component={Link} style={{ color: 'black', textDecoration: 'none' }}>Home</Typography>
             </div>
           </Button>
         </li>
{/* ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           */}
         <li>
           <Button>
             <div style={{ display: 'flex', marginTop: '20px', marginLeft: '30px' }}>
               <NotificationsActiveIcon style={{ fontSize: 30, color: 'black', marginRight: '30px' }} />
               <Typography variant="h6" component={Link} style={{ color: 'black', textDecoration: 'none' }}>Updates</Typography>
             </div>
           </Button>
         </li>
{/* ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           */}
         <li>
           <Button>
             <div style={{ display: 'flex', marginTop: '20px', marginLeft: '30px' }}>
               <NotificationsActiveIcon style={{ fontSize: 30, color: 'black', marginRight: '30px' }} />
               <Typography variant="h6" onClick={() => { Navigate('/createpost') }} component={Link} style={{ color: 'black', textDecoration: 'none' }}>Create post</Typography>
             </div>
           </Button>
         </li>
{/* ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           */}
         <li>
           <Button>
             <div style={{ display: 'flex', marginTop: '20px', marginLeft: '30px' }}>
               <ViewComfyIcon style={{ fontSize: 30, color: 'black', marginRight: '30px' }} />
               <Typography variant="h6" onClick={() => Navigate('/myposts')} component={Link} style={{ color: 'black', textDecoration: 'none' }}>My Posts</Typography>
             </div>
           </Button>
         </li>
{/* ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           */}
       </ul>

     </div>

      {/* Main content (80%) */}
      <div style={{ width: '80%', backgroundColor:'#c0dde6' }}>

        <Navbar />  

        <div className="content" style={{marginLeft:'20px', marginTop:'20px'}}>

          <Masonry columns={3} gap={10}>

          {posts.slice(0,6).map((post, index) => (
      <div key={index}>
        <Box sx={{padding:'20px', backgroundColor:'white'}}>

          <div style={{display: 'flex', flexDirection: 'column', marginBottom:'20px'}}>

        {/* Title */}
        <Typography variant="h6" component="div" sx={{ color: 'black' }}>
          {post.title}
        </Typography>

        {/* Username and Timestamp */}
        <div style={{display: 'flex', justifyContent: 'start', alignItems: 'baseline'}}>
          <Typography variant="body2" component="span" sx={{ color: 'gray', marginRight: '10px' }}>
            {post.username}
          </Typography>
          <Typography variant="body2" component="span" sx={{ color: 'gray' }}>
          {new Date(post.timestamp).toLocaleDateString()}
          </Typography>
        </div>

        {/* Description */}
        <Typography variant="body1" component="div" sx={{ color: 'black', marginTop:'10px' }}>
          {post.description}
        </Typography>

          </div>

        </Box>
      </div>
    ))}


            
          
          </Masonry>

        </div>       
      </div>
    </div>
  );
}
