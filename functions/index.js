const functions = require('firebase-functions');
const admin = require('firebase-admin');
//const bodyParser = require('body-parser')
admin.initializeApp(functions.config().firebase);

exports.sign_up = functions.https.onRequest((request, response) => {
    admin.auth().createUser({
    email: "user@example.com",
    password: "secretPassword"
}).then(function(userRecord) {
    // A UserRecord representation of the newly created user is returned
    response.send(userRecord);
}).catch(function(error) {
    response.send(error);
});
});


exports.notRegistered = functions.https.onRequest((request, response) => {
    if(request.method=="POST")
   {

       var str = '{ "name": "John Doe", "age": 42 }';
       var obj = JSON.parse(str);
       var data= request.body.token;
       const projectsRef = admin.database().ref('notRegistered/');
       projectsRef.push({'token':data});
       console.log(obj);
       response.send("done");
       return obj;

   }

});





