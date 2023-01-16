const express = require('express');
const app = express();
const cors = require('cors')

app.use(cors())

app.listen(9000, function(){

    console.log('App running on port 9000')
})

app.get("/", function(request, response){
    response.json({message: "Hello World"})
})