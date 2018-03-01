import {Component} from '@angular/core';
import {AlertController, NavController, NavParams} from 'ionic-angular';
import {FirebaseProvider} from "../../providers/firebase";
import {HomePage} from "../login/login";

@Component({
    selector: 'page-validationcode',
    templateUrl: 'validationcode.html',
})
export class ValidationcodePage {
tryCount=0;
    constructor(public navCtrl: NavController,
                public navParams: NavParams,
                public firebaseprovider: FirebaseProvider,
                public alertCtrl: AlertController) {
    }

    onCode(code) {
        this.firebaseprovider.validationCode(code).subscribe((data) => {
            console.log(data["validation"]);
            if (data["validation"] == "validate") {
                let alert = this.alertCtrl.create({
                    title: "Validation",
                    subTitle: "Thank For Validate Your Phone Number",
                    buttons: [
                        {
                            text: 'Close',
                            handler: () => {
                                this.navCtrl.push(HomePage);
                            }
                        }
                    ]
                });
                alert.present();
            }else {
                let alert = this.alertCtrl.create({
                    title: "Validation",
                    subTitle: "The Code You Enter Was Wrong",
                    buttons: [
                        {
                            text: 'Close',
                            handler: () => {
                                this.tryCount=this.tryCount+1;
                            }
                        }
                    ]
                });
                alert.present();
            }


        }, (err) => {

        });


    }

}
