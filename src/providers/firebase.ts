import {Inject, Injectable} from '@angular/core';
import 'rxjs/add/operator/map';
import {AngularFireAuth} from "angularfire2/auth";
import {Toast} from "@ionic-native/toast";
import {Events, Platform} from 'ionic-angular';
import {Storage} from '@ionic/storage';
import {Firebase} from "@ionic-native/firebase";
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/catch';
import firebases from "firebase";
import {Facebook} from "@ionic-native/facebook";
import {FCM} from "@ionic-native/fcm";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {AngularFirestore} from "angularfire2/firestore";
import {APP_CONFIG, AppConfig} from "../config/configs";


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
    Nodeapi: string = '';

    constructor(public firebaseAuth: AngularFireAuth,
                public toast: Toast,
                public events: Events,
                private storage: Storage,
                public firebase: Firebase,
                public fb: Facebook,
                public platform: Platform,
                public FCMPlugin: FCM,
                public http: HttpClient,
                private db: AngularFirestore,
                @Inject(APP_CONFIG) public config: AppConfig) {
        this.Nodeapi = this.config.apiNode;
        //this is for the push Notifications only and only for ios without this the push wont work
        this.firebase.onNotificationOpen().subscribe((data) => {

        }, (err) => {

        });

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
        return this.http.get(this.api + "sign_up")
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
        //firestroe ---> database
        this.db.collection('notregistered').add({
            tokenuser: token,
            type_of_os: typeOfOs,
            registered: "Not registered"
        }).then((data) => {
            this.storage.set("gotUserToken", true);
            this.getUserUID(data.id);
        });

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
                    alert(JSON.stringify(key));
                    this.firebase.getToken()
                        .then((tokenuser) => {
                            this.db.collection("notregistered").doc(key).delete().then((data) => {
                                this.db.collection("registered").add({
                                    tokenuser: tokenuser,
                                    userName: "danny",
                                    UserUID: user,
                                    Email: email,
                                    type_of_os: this.type_of_os,
                                    registered: "Registered"
                                })

                            })
                        });
                });
            }
        });
        this.storage.set('hasSignIn', true);
    }

    onFaceBookLogin() {
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
        this.userId = data;
        this.storage.set("UserUID", this.userId);
    }

    onToast(data) {
        this.toast.show(JSON.stringify(data), '5000', 'top').subscribe();
    }


    phoneVerification(phoneNumber: String) {
        const headers = new HttpHeaders({'Content-Type': 'application/json'});
        this.http.post(this.Nodeapi + "sendsms", {number: phoneNumber}, {headers})
            .subscribe((data) => {

            }, (err) => {

            });
    }

    validationCode(code) {
        const headers = new HttpHeaders({'Content-Type': 'application/json'});
       return this.http.post(this.Nodeapi + "code", {code: code}, {headers});

    }

}