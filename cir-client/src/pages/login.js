import logo from '../assets/cir_logo.png';
import {useNavigate } from 'react-router-dom';
import {useState} from 'react';
import { Typography, Box, Container, TextField, FormControlLabel,Link,  Checkbox, Button } from '@mui/material';

export default function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    }

    const handleLogin = async () => {
        const response = await fetch('http://localhost:5000/login', {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                email: email,
                password: password
            
            })
        });

        const data = await response.json();

        if (data.success) {
            navigate('/');
        }
        else{
            alert('Login failed!');
        }
    }

    return (
      <div className="login-page" style={{display: "grid", gridTemplateColumns: "1fr 1fr", height: "100vh"}}>
        <Container component="main" maxWidth="xs" style={{display: "flex", justifyContent: "center", alignItems: "center"}}>
            <Box>

            <form noValidate autoComplete="off" style={{ display: 'flex', flexDirection: 'column' }}>

                {/* First Heading */}
                <Typography variant="h4" style={{marginBottom: '10px', textAlign:"left"}}>Welcome back!</Typography>
               

               {/* heading subtext */}
                <Typography variant="h6"
                    style={{marginBottom: '20px', textAlign:"left", whiteSpace: 'nowrap',overflow: 'hidden', textOverflow: 'ellipsis'}}>
                        Enter your credentials to access your account
                </Typography> 


                {/* Email label */}
                <Typography variant='h6' align='left' style={{color: 'black', fontSize: '0.9rem', marginBottom: '0px'}}>Email address</Typography>
                <TextField label="Email" value={email} onChange={handleEmailChange} required variant="outlined" fullWidth margin="dense" />


                {/* Password label */}
                <Typography variant='h6' align='left' style={{color: 'black', fontSize: '0.9rem', marginBottom: '0px'}}>Password</Typography>
                <TextField label="Password" value={password} onChange={handlePasswordChange} required variant="outlined" fullWidth margin="dense" type="password" />

                {/* Remember me checkbox */}
                <FormControlLabel control={<Checkbox />} label="Remember me for 30 days?" />

                {/* Login button */}
                <Button variant="contained" onClick={handleLogin} sx={{ width: '100%', margin: 2, alignSelf: 'center', backgroundColor: '#59B6B1' }} type="button"> Login </Button>

                {/* Forgot password link */}
                <Typography variant='h6' align='center' style={{color: 'black', fontSize: '0.9rem', marginBottom: '0px'}}>Don't have an account?  
                <Link component="button" onClick={ ()=> navigate('/signup')} style={{color: 'blue', marginLeft:"3px"}}>Sign up</Link>
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