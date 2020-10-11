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
//         appId: '687a6a325630305736476f47707536625255547334593175716d7a4c67655033',
//         appSecret: '4b673743476f326333766554496e4d4370592d2d704370775a5948323568662d644c356579556544515871455177354f3271384349396a5f326a5952596a6f6e',
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