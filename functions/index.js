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
       var str = '{ "status": "success"}';
      // var obj = JSON.parse(str);
       var token= request.body.token;
       const Ref = admin.database().ref('notRegistered');
         Ref.push({'token':token}).then(() => {
       response.status(200).send(str);
       });
   }
});




exports.Registered = functions.https.onRequest((request, response) => {
    if(request.method=="POST")
   {
       var str1 = '{ "status": "success"}';
       var email= request.body.email;
       var tokennew= request.body.token;
       var UserUID= request.body.UserUID;
       const Ref = admin.database().ref('Registered');
       Ref.push({'token':tokennew,'email':email,'UserUID':UserUID}).then((data) => {
           response.status(200).send(str1);

            });
       response.status(500).send("bad");

   }


});



