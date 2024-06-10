import React, { useState, useRef } from 'react';
import { Box,Typography,TextField, Link, Button, Grid } from '@mui/material';
import { jwtDecode } from 'jwt-decode';
import Navbar from '../components/navbar';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import HomeIcon from '@mui/icons-material/Home';
import NotificationsActiveIcon from '@mui/icons-material/NotificationsActive';
import ViewComfyIcon from '@mui/icons-material/ViewComfy'
import { useNavigate } from 'react-router-dom';

export default function Createpost() {
  const Navigate = useNavigate();
  const [title, setTitle] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const [file, setFile] = useState(null);

  const token = localStorage.getItem('token'); 
  const fileInputRef = useRef(null);

  let Username = 'Vinamra'; 

  if (token) {
    const decodedToken = jwtDecode(token);
    Username = decodedToken.username; 
  }

  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  }

  const handleCategoryChange = (e) => {
    setCategory(e.target.value);
  }

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  }

  const handleAddImageClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setFile(file);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('title', title);
    formData.append('category', category);
    formData.append('description', description);
    formData.append('image', file); 
    formData.append('timestamp', new Date().toISOString());
  
    try {
      const response = await fetch('http://localhost:5000/posts', { 
        method: 'POST',
        body: formData 
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json(); 
      alert("Post created successfully");
      Navigate('/landing');
    }
    catch (error) {
      console.error('Error creating post:', error);
    }
  };


  return (
    <div style={{ display: 'flex', height: '100vh' }}>

      {/* Vertical component (20%) */}
      <div style={{ width: '20%', backgroundColor: 'white' }}>
        
        <AccountCircleIcon style={{ fontSize: 50, color: 'black', marginBottom:'5px', marginTop:'10px',marginLeft:'130px' }} />
        <Typography variant="h6" component="div" sx={{ color: 'black', marginTop:'10px' , marginLeft:'110px', marginBottom:'20px'}}>{Username}</Typography>
      
        <div style={{ borderTop: '3px solid grey', width: '100%' }}></div>

        <ul style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '20px', padding: 0, listStyle:'none'  }}>
       
            <li>
              <div style={{display:'flex', justifyContent:'space-around', marginTop:'20px'}}>
                <TextField id="outlined-basic" label="Search" variant="outlined" />
              </div>
            </li>
            
            <li>
              <Button>
              <div style={{display:'flex', marginTop:'20px', marginLeft:'30px'}}>
                <HomeIcon style={{ fontSize: 30, color: 'black', marginRight:'30px' }} />
                <Typography variant="h6" onClick={()=>{Navigate('/landing')}} component={Link} style={{ color: 'black', textDecoration: 'none' }}>Home</Typography>
              </div>
              </Button>
            </li>

            <li>
              <Button>
            <div style={{display:'flex', marginTop:'20px', marginLeft:'30px'}}>
                <NotificationsActiveIcon style={{ fontSize: 30, color: 'black', marginRight:'30px' }} />
                <Typography variant="h6" component={Link} style={{ color: 'black', textDecoration: 'none' }}>Updates</Typography>
              </div>
              </Button>
            </li>

            <li>
              <Button>
            <div style={{display:'flex', marginTop:'20px', marginLeft:'30px'}}>
                <NotificationsActiveIcon style={{ fontSize: 30, color: 'black', marginRight:'30px' }} />
                <Typography variant="h6" onClick={()=>{Navigate('/createpost')}} component={Link} style={{ color: 'black', textDecoration: 'none' }}>Create post</Typography>
              </div>
              </Button>
            </li>

            <li>
              <Button>
            <div style={{display:'flex', marginTop:'20px', marginLeft:'30px'}}>
                <ViewComfyIcon style={{ fontSize: 30, color: 'black', marginRight:'30px' }} />
                <Typography variant="h6" onClick={()=>Navigate('/myposts')} component={Link} style={{ color: 'black', textDecoration: 'none' }}>My Posts</Typography>
              </div>
              </Button>
            </li>

        </ul>
      </div>

      {/* Main content (80%) */}
      <div style={{ width: '80%', backgroundColor:'#c0dde6' }}>

        <Navbar />  

        <div className="content" style={{marginLeft:'20px', marginTop:'20px'}}>

        <Box style={{ backgroundColor: 'white', width: '1090px', height: '500px', padding: '20px' }}>
            <Typography variant="h4" style={{marginBottom: '20px'}}>Create a Post</Typography>
            <form noValidate autoComplete="off">
                <Grid container spacing={3}>

                    <Grid item xs={10} sm={5}>
                        <TextField required id="post-title" value={title} onChange={handleTitleChange} label="Post Title"  fullWidth variant="outlined"/>
                    </Grid>

                    <Grid item xs={10} sm={5}>
                        <TextField required id="post-category" value={category} onChange={handleCategoryChange} label="Category" fullWidth variant="outlined"/>
                    </Grid>
                
                    <Grid item xs={10}>
                        <TextField id="post-description" value={description} onChange={handleDescriptionChange} label="Description" fullWidth multiline rows={4} variant="outlined"/>
                    </Grid>

                    <Grid item xs={10}>
                        <input type="file" accept="image/*" style={{ display: 'none' }} ref={fileInputRef} onChange={handleFileChange}/>
                        <Button variant="contained" color="primary" onClick={handleAddImageClick}> Add Image </Button>
                    </Grid>

                    <Grid item xs={10}>
                        <Button variant="contained" color="primary" onClick={handleSubmit}>Submit Post</Button>
                    </Grid>

                </Grid>
            </form>
        </Box>
        </div>       
      </div>
    </div>
  );
}
