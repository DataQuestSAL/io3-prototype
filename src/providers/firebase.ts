import {Injectable} from '@angular/core';
import 'rxjs/add/operator/map';
import {AngularFireAuth} from "angularfire2/auth";
import {Toast} from "@ionic-native/toast";
import {AngularFireDatabase} from "angularfire2/database";
import {Events, Platform} from 'ionic-angular';
import {Storage} from '@ionic/storage';
import {Firebase} from "@ionic-native/firebase";
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/catch';
import firebases from "firebase";
import {Facebook} from "@ionic-native/facebook";
import {FCM} from "@ionic-native/fcm";
import {HttpClient} from "@angular/common/http";


@Injectable()
export class FirebaseProvider {
    // authListener;
    users: boolean = true;
    user;
    notregisteredlist;
    authListener;
    userId;
    api = "https://us-central1-client-space-mobile.cloudfunctions.net/";
    type_of_os = "";

    constructor(
                public firebaseAuth: AngularFireAuth,
                public toast: Toast,
                public afDB: AngularFireDatabase,
                public events: Events,
                private storage: Storage,
                public firebase: Firebase,
                public fb: Facebook,
                public platform: Platform,
                public FCMPlugin: FCM,
                public http2:HttpClient) {
        //this is for the push Notifications only and only for ios without this the push wont work
        this.firebase.grantPermission().then((data) => {
            // alert(data);
        }).catch((err) => {
            alert("error-->" + JSON.stringify(err))
        });
        this.firebase.onNotificationOpen().subscribe((data) => {
            alert(JSON.stringify(data));
        }, (err) => {
            alert(JSON.stringify(err))
        });

        // //this is for the push Notifications only and only for ios without this the push wont work
        // this.firebase.hasPermission().then((data) => {
        //     //alert(JSON.stringify(data));
        // }).catch((err) => {
        //     //alert("error-->" + JSON.stringify(err))
        // });


        this.notregisteredlist = afDB.list('/notregistered');
        this.authListener = this.firebaseAuth.authState.subscribe(user => {
            if (user) {
                this.authListener.unsubscribe();
                this.users = true;

            } else {
                this.users = false;
                this.authListener.unsubscribe();
            }
        }, (err) => {
            // alert(err);
        });
    }


    signup(email: string, password: string) {

        // this.firebaseAuth.auth.createUserWithEmailAndPassword(email, password)
        //     .then(value => {
        //         this.onToast('Success!,' + value);
        //     })
        //     .catch(err => {
        //         this.onToast('Something went wrong:,' + err.message);
        //     });
        // this.firebase.onTokenRefresh()
// -----------------------------------------------------------------------
        return this.http2.get(this.api + "sign_up")
    }

    login(newEmail: string, newPassword: string) {
        // return this.firebaseAuth.auth.signInWithEmailAndPassword(newEmail, newPassword).then((user) => {
        //     this.onToast(user);
        //     this.storage.get('UserUID').then((key) => {
        //         this.notregisteredlist.remove(key)
        //             .then((data) => {
        //                 this.storage.get('hasSignIn').then((val) => {
        //                     if (val != true) {
        //                         this.userRegistered(user.uid, user.email);
        //                         this.storage.set('hasSignIn',true)
        //                     }
        //                 });
        //             });
        //     });
        // }).catch((err) => {
        //     this.onToast(err.message);
        // });
    }

    notRegistered(token, typeOfOs) {
        this.afDB.list('/notregistered').push({
            tokenuser: token,
            type_of_os: typeOfOs,
            registered: "Not registered"
        }).then((data) => {
            this.storage.set("gotUserToken", true);
            this.getUserUID(data);
            ///alert(data)
        });
// -------------------------------------------------------------

        // let headers = new Headers({
        //     'content-type': 'application/x-www-form-urlencoded'
        // });
        // let options = new RequestOptions({
        //     headers: headers
        // });
        // let data = {
        //     token: token
        // };
        // return this.http.post(this.api + "notRegistered", JSON.stringify(data), options)
        //     .do(this.logResponse)
        //     .map(this.extractData)
        //     .subscribe(() => {
        //         alert("da");
        //     });
    }

    userRegistered(user, email) {
        if (this.platform.is('ios')) {

            this.type_of_os = "ios"
        }
        if (this.platform.is('android')) {

            this.type_of_os = "android"
        }
        this.storage.get('hasSignIn').then((val) => {
            if (val != true) {
                this.storage.get('UserUID').then((key) => {
                    this.notregisteredlist.remove(key).then(() => {
                        this.firebase.getToken()
                            .then((tokenuser) => {
                                this.afDB.list('/registered').push({
                                    tokenuser: tokenuser,
                                    userName: "danny",
                                    UserUID: user,
                                    Email: email,
                                    type_of_os: this.type_of_os,
                                    registered: "Registered"

                                }).then((data) => {
                                    this.storage.set("gotUserToken", true);
                                    this.getUserUID(data);
                                });
                            }).catch((error) => {
                            this.onToast(error);
                        });
                    })
                });

            }
        });
        this.storage.set('hasSignIn', true);
    }
    onFaceBookLogin() {
        // this.fb.login(['email']).then((data) => {
        //     const fc = firebase.auth.FacebookAuthProvider.credential(data.authResponse.accessToken);
        //     alert(JSON.stringify(fc));
        //     firebase.auth().signInWithCredential(fc).then((datas) => {
        //
        //     })
        // }).catch((err) => {
        //     alert(JSON.stringify(err))
        // })
        let provider = new firebases.auth.FacebookAuthProvider();
        firebases.auth().signInWithRedirect(provider).then(() => {
            firebases.auth().getRedirectResult().then((data) => {
                alert(JSON.stringify(data))
            }).catch((err) => {
                alert("bad");
            })
        })
    }
    logoutUser() {
        return this.firebaseAuth.auth.signOut();
    }

    getUserUID(data) {
        this.userId = data.key;
        this.storage.set("UserUID", this.userId);
    }

    onToast(data) {
        this.toast.show(JSON.stringify(data), '5000', 'top').subscribe();
    }

}