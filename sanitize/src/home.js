import React, {Component} from "react";
import {Link} from 'react-router-dom';

//import assets
import HomeImg from './welcome.png';
// import { sdk } from 'symbl-node';




class Home extends Component {
  constructor(props) {
    super(props);
  } 
//   componentDidMount(){
//     sdk.init({
//         appId: '##',
//         appSecret: '##',
//         basePath: 'https://api.symbl.ai'
//       })
//       .then(() => console.log('SDK Initialized.'))
//       .catch(err => console.error('Error in initialization.', err));
//   }
    render() {
        return (
         <div>
            <div>
              
            </div>
            <div>
              <div style={{margin:"15vh 2.5%",fontFamily:"Raleway", fontSize:"9.75vh",lineHeight:"100%", color:"#6c63ff", width:"41.7%", float: "left"}}>
                Sanitize.ai
                <div style={{fontFamily:"Montserrat", lineHeight:"100%", fontSize:"3vh", marginTop: "5%"}}>
                Send a message to Sanitize.ai
                </div>
                <div style={{fontFamily:"Montserrat", lineHeight:"100%", fontSize:"3vh", marginTop: "5%"}}>
                <input style={{width:'50%', height:'20%', fontSize:20}}></input>
                </div>
                <div style={{ marginRight:"25%"}}>
              
                <Link style={{textDecoration:'none'}} to="/login">
               
                <div style={{fontFamily:"Montserrat", lineHeight:"100%", fontSize:"2vh", marginTop: "25%", color:'#FFF',backgroundColor:"#6c63ff", width:'75%', paddingTop:'5%', paddingBottom:'5%', borderRadius:20, marginLeft:'29%'}}>
                Send
                </div> </Link>
                </div>
                </div>
              <div style={{float: "right", marginTop:'10%', marginRight:'5%'}}><img src={HomeImg} alt="home" height="600vh"></img></div>
            </div>
         </div>   
        );
    }
}

export default Home;