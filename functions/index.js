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
        Ref.push({'registered':request.body.registered,'token':request.body.token,'email':request.body.email,'Type_Of_OS':request.body.type_of_os,'UserUID':request.body.UserUID}).then((data) => {
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
    admin.auth().createCustomToken(uid,additionalClaims)
        .then(function (token) {

            response.status(200).send(JSON.stringify(token));
            console.log(token);
        }).catch(function (error) {
        response.status(200).send(JSON.stringify(error));
    });
    admin.auth().updateUser(uid, {
        email: "newuuser@dq.com.lb"
    }).then(function(userRecord) {
            // See the UserRecord reference doc for the contents of userRecord.
            console.log("Successfully updated user", userRecord.toJSON());
            response.status(200).send(JSON.stringify(userRecord));
        })
        .catch(function(error) {
            console.log("Error updating user:", error);
            response.status(200).send(JSON.stringify(error));
        });
});


exports.Sendpushnotification = functions.https.onRequest(function (request, response) {
    if(request.method=="POST") {
        // var registrationTokens = response;
        var registrationTokens =[
            "eXjBZwQ8gkQ:APA91bGGKE6ipu9WoquHkFaW_5ZF4aFzhJH3yfBuWNOFC6IWUh0excQd6eTpJ_HjmM6qWF7oW27pt2G7pc7fiNHl8KGDcKHHILucnM786y5jil3dI1yfUrrT9GpAyKFFU6NVM2wWJ_o9",//android
            "fiY0WKOcYlA:APA91bGD3mHlKi-UtwirKJ0ErGgI7UP9aUgPzxcQ34b9IcNmkhfBpKu-JBvxs1zymooj8mkY9lRNg0bPDWjKtHTX4OLO5VfGS9V6oy44Ebnz2Zlp-1osfFfl1uzbYV8sP9sXAB_2NJS2",//ios
            "et4begOXEF8:APA91bE5fScdPyXO-FS1wURxqsW6OOp3K7aF39x6IZ_CVw4RcW2F9MlX6D6HCGjlKYT5fjI-wF2QljjMyqWVssbvOYnYnYHDhqwgEhM9WSPrYH2DYDD8QYyKEvfAZJiS6fxcq8QeY6qh",//android
            "dI_u0QnuM-s:APA91bFkTGbHtXmbWvS0Us9spKSZHm9bPdmqex7nmzHqWaB41c0zxYSnk16jXBG842CRVIxflb7aIBqA8P1shvV4diS1-ZD5nZWNeOny7vfqwFtoPvBuKpZFbja8IwThXg9XzBd6PW7E"//ios
    ];
        console.log(registrationTokens);
        var payload = {
            notification: {
                title: "Hi Android",
            }
        };

        const options = {
            content_available: true
        }

        admin.messaging().sendToDevice(registrationTokens, payload,options)
            .then(function (response) {
                console.log("Successfully sent message:", response);
            })
            .catch(function (error) {
                console.log("Error sending message:", error);
            });
       // console.log("new");
       // console.log("-->"+request.body)
    }
});
