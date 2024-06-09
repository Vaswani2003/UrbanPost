import Toolbar from "@mui/material/Toolbar"
import AppBar from "@mui/material/AppBar"
import Typography from "@mui/material/Typography"
import Button from "@mui/material/Button"
import logo from '../assets/cir_logo.png'

export default function Navbar() {
    return (
        <AppBar position="static" sx={{ backgroundColor: '#fff', padding:0, margin:0 }}>
        <Toolbar>
        <div style={{display: 'flex', justifyContent: 'space-between', width: '100%', }}>
          <div style={{ width: '100%' }}>
              <Typography variant="h5" component="div" sx={{ color: 'black', marginTop:'20px', marginBottom:'20px' }}>Citizen's Issues Registry</Typography>

              <ul className="nav-links" style={{ display: 'flex', justifyContent: 'space-evenly', listStyle: 'none', padding: 0, color: 'black' }}>
              <li><Button><Typography variant="h6"  style={{ color: 'black', textDecoration: 'none' }}>Complaints</Typography></Button></li>
          <li><Button><Typography variant="h6"  style={{ color: 'black', textDecoration: 'none' }}>Top</Typography></Button></li>
          <li><Button><Typography variant="h6" style={{ color: 'black', textDecoration: 'none' }}>New</Typography></Button></li>
          <li><Button><Typography variant="h6" style={{ color: 'black', textDecoration: 'none' }}>Innovation</Typography></Button></li>
          <li><Button><Typography variant="h6" style={{ color: 'black', textDecoration: 'none' }}>Promotion</Typography></Button></li>
          <li><Button><Typography variant="h6"  style={{ color: 'black', textDecoration: 'none' }}>Controversial</Typography></Button></li>
      </ul>
          </div>

          <div>
              <img src={logo} alt="Logo" style={{ width: '125px', height:'100%' }} />
          </div>  
        </div>
        </Toolbar>
      </AppBar>
    );
}
