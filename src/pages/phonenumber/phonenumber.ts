import {Component} from '@angular/core';
import {AlertController, NavController, NavParams} from 'ionic-angular';
import {FirebaseProvider} from "../../providers/firebase";
import {ValidationcodePage} from "../validationcode/validationcode";

@Component({
    selector: 'page-phonenumber',
    templateUrl: 'phonenumber.html',
})
export class PhonenumberPage {

    phoneNumber = "";

    constructor(public firebaseprovider: FirebaseProvider,
                public alertCtrl: AlertController,
                public navCtrl:NavController) {
    }

    signIn(phoneNumber: string) {

        if (phoneNumber == "") {
            let alert = this.alertCtrl.create({
                title: "The Phone Number is Empty",
                subTitle: "Please Enter A Phone Number",
                buttons: ['Dismiss']
            });
            alert.present();
        }
        else {

            let alert = this.alertCtrl.create({
                title: "The Phone Number",
                subTitle: 'This is Number correct ' + phoneNumber,
                buttons: [
                    {
                        text: "yes",
                        handler: () => {
                            this.firebaseprovider.phoneVerification(phoneNumber);
                            this.navCtrl.push(ValidationcodePage);

                        }
                    },
                    {
                        text: 'No'
                    }
                ]
            });
            alert.present();


        }

    }


}
