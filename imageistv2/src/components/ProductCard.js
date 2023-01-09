import React from "react";
import axios from "axios";
import { useEffect, useState,useContext } from "react";
import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { useNavigate } from "react-router-dom";
import { SKU } from "../App";
import { q } from '../App'

export default function ProductCard() {
  
  const {query,setQuery}=useContext(q);
  const {setSKU}=useContext(SKU);
  const [data, setData] = useState([]);
  const navigate=useNavigate();
  function navi(sku){
    setSKU(sku);
    navigate("/product-details")

  }
  
  useEffect(() => {
    console.log(query);
    if (query!='all')
    {
    axios.get('http://127.0.0.1:8000/search/?q='+query)
      .then(response => {
        setData(response.data);
        console.log('images',data.images);
        setQuery('all');
      })
      .catch(error => {
        console.error(error);
      });
    }
    else{
      axios.get('http://127.0.0.1:8000/search/?q=all')
      .then(response => {
        setData(response.data);
        console.log('images',data.images);
        setQuery('all');
      })
      .catch(error => {
        console.error(error);
      });
    }


  }, []);

  return (
    <div>

    <main>
    <Container  sx={{ py: 8 }}>
    
      <Grid container spacing={4}>
        {data.map((card) => (
          <Grid item key={card} xs={12} sm={6} md={3}>
            <Card
            style={{backgroundColor:"#6353C6",height:"550px"}}
            raised
            sx={{
              maxWidth: 280,
              margin: "0 auto",
              padding: "0.1em",
              maxHeight:600
            }}
      
             
            >
              <CardMedia
                component="img"
            height={150}
                image={card.images}
                alt="random"
                sx={{ padding: "1em 1em 0 1em" }}
              />
              <CardContent sx={{ flexGrow: 1 }}>
                <Typography gutterBottom variant="h8" component="h8" >
                  {card.type}
                </Typography>
<br></br>
                <Typography variant="p">
                 {card.title}
                </Typography>
<br></br>
                <Typography variant="p" style={{topmargin:"5px"}}>
                {card.price}
               </Typography>
               <br></br>
              </CardContent>
              <Box alignItems={"center"} >
                      <CardActions sx={{ marginLeft: 8}}>
                        <Button class="more-info" style={{backgroundColor:"white"}} onClick={()=>{navi(card.product_link)}}>View Product</Button>

                      </CardActions>
                    </Box>
            </Card>
          </Grid>
        ))}
      </Grid>
      
    </Container>
  </main>



    </div>                
  )
          }