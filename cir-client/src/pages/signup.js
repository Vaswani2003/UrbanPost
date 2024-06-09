import logo from '../assets/cir_logo.png';
import {useNavigate } from 'react-router-dom';
import React, { useRef, useState} from 'react';
import { Typography, Box, Container, TextField, FormControlLabel,Link,  Checkbox, Button } from '@mui/material';

export default function Signup() {
    const navigate = useNavigate();
    const fileInputRef = useRef(null);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleNameChange = (e) => {
        setName(e.target.value);
    }
    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    }
    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    }

    const handleAadharUploadClick = () => {
        fileInputRef.current.click();          
    };

    const handleFileChange = (event) => {
        const file = event.target.files[0];
    };

    const handleSignup = async () => {
        const response = await fetch('http://localhost:5000/signup', {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                name: name,
                email: email,
                password: password,
                aadhar: fileInputRef.current.files[0],
            })
        });

        const data = await response.json();

        if (data.success) {
            navigate('/login');
        }
        else{
            alert('Signup failed!');
        }
    }

    return (
      <div className="login-page" style={{display: "grid", gridTemplateColumns: "1fr 1fr", height: "100vh"}}>
        <Container component="main" maxWidth="xs" style={{display: "flex", justifyContent: "center", alignItems: "center"}}>
            <Box>

            <form noValidate autoComplete="off" style={{ display: 'flex', flexDirection: 'column' }}>

                {/* First Heading */}
                <Typography variant="h4" style={{marginBottom: '10px', textAlign:"left"}}>Get Started Now</Typography>
               

               {/* heading subtext */}
                <Typography variant="h6"
                    style={{marginBottom: '20px', textAlign:"left", whiteSpace: 'nowrap',overflow: 'hidden', textOverflow: 'ellipsis'}}>
                        Create your credentials to access your account
                </Typography> 

                
                {/* Name label */}
                <Typography variant='h6' align='left' style={{color: 'black', fontSize: '0.9rem', marginBottom: '0px'}}>Full Name</Typography>
                <TextField label="Name" value={name} onChange={handleNameChange} required variant="outlined" fullWidth margin="dense" style={{marginBottom:'20px'}} />

                {/* Email label */}
                <Typography variant='h6' align='left' style={{color: 'black', fontSize: '0.9rem', marginBottom: '0px'}}>Email address</Typography>
                <TextField label="Email" value={email} onChange={handleEmailChange} required variant="outlined" fullWidth margin="dense" style={{marginBottom:'20px'}}/>


                {/* Password label */}
                <Typography variant='h6' align='left' style={{color: 'black', fontSize: '0.9rem', marginBottom: '0px'}}>Password</Typography>
                <TextField label="Password" value={password} onChange={handlePasswordChange} required variant="outlined" fullWidth margin="dense" type="password" style={{marginBottom:'20px'}}/>

                {/* Remember me checkbox */}
                <FormControlLabel control={<Checkbox />} label="I agree to terms and policies" />

                {/* Aadhar Button */}
                <Button variant="contained" sx={{ width: '100%', margin: 2, alignSelf: 'center', backgroundColor: '#301C3B' }}  type="button"  onClick={handleAadharUploadClick}>Upload Aadhar</Button>
                <input type="file" style={{ display: 'none' }} ref={fileInputRef} onChange={handleFileChange} />

                {/* SignUp button */}
                <Button variant="contained" onClick={handleSignup} sx={{ width: '100%', margin: 2, alignSelf: 'center', backgroundColor: '#59B6B1' }} type="button"> Sign Up </Button>

                {/* Forgot password link */}
                <Typography variant='h6' align='center' style={{color: 'black', fontSize: '0.9rem', marginBottom: '0px'}}>Already have an account?  
                <Link component="button" onClick={ ()=> navigate('/login')} style={{color: 'blue', marginLeft:"3px"}}>Sign up</Link>
                </Typography>
                
            </form>
            </Box>
        </Container>


        {/* Image */}
        <div className="login-page-image" style={{width: "100%", height: "100%", display: "flex", justifyContent: "center", alignItems: "center"}}>
            <img src={logo} alt="logo" style={{maxWidth: "100%", maxHeight: "100%"}}/>
        </div>


      </div>
    );
}