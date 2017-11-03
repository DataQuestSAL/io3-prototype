const functions = require('firebase-functions');
const admin = require('firebase-admin');


const serviceAccount=require('./client-space-mobile-5ee7e5905d13.json');
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://client-space-mobile.firebaseio.com"
});
//const bodyParser = require('body-parser')
//admin.initializeApp(functions.config().firebase);




exports.sign_up = functions.https.onRequest(function (request, response) {
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



exports.notRegistered = functions.https.onRequest(function (request, response) {
    if(request.method=="POST")
   {
       var str = '{ "status": "success"}';
      // var obj = JSON.parse(str);
       var token= request.body.token;
       const Ref = admin.database().ref('notRegistered');
         Ref.push({'token':token}).then( function () {
       response.status(200).send(str);
       });
   }
});




exports.Registered = functions.https.onRequest(function (request, response) {
    if(request.method=="POST")
   {
       var str1 = '{ "status": "success"}';
       var email= request.body.email;
       var tokennew= request.body.token;
       var UserID= request.body.UserUID;

       //response.status(200).send(UserUID);
       const Ref = admin.database().ref('Registered');
       Ref.push({'token':request.body.token,'email':request.body.email,'UserUID':request.body.UserUID}).then((data) => {
           response.status(200).send(str1);

            });


   }

});

exports.CreateUserToken = functions.https.onRequest(function (request, response) {

    var uid = "1";
    var str = '{ "status": customToken}';


    var additionalClaims = {
        premiumAccount: true
    };

    admin.auth().createCustomToken(uid)
        .then(function (token) {

            response.status(200).send(JSON.stringify(token));
            console.log(token);
        }).catch(function (error) {
        response.status(200).send(JSON.stringify(error));
    });


    admin.auth().updateUser(uid, {
        email: "newuuser@dq.com.lb"
    })
        .then(function(userRecord) {
            // See the UserRecord reference doc for the contents of userRecord.
            response.status(200).send(JSON.stringify(userRecord));
            console.log("Successfully updated user", userRecord.toJSON());
        })
        .catch(function(error) {
            response.status(200).send(JSON.stringify(error));
            console.log("Error updating user:", error);
        });



});


