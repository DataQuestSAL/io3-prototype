import {Component} from '@angular/core';
import {NavController, Platform, ActionSheetController, AlertController} from 'ionic-angular';
import {DataServiceProvider} from '../../providers/data-service';
import {basePage} from '../../models/basePage';
import {RegisterPage} from '../register/register';
import {CommonServiceProvider} from '../../providers/common-service';
import {Toast} from '@ionic-native/toast';
import {TranslateService} from "@ngx-translate/core";
import {Storage} from '@ionic/storage';
import {Keyboard} from "@ionic-native/keyboard";
import {FirebaseanalyticsPage} from "../firebaseanalytics/firebaseanalytics";
import {Firebase} from "@ionic-native/firebase";
import {FirebaseProvider} from "../../providers/firebase";
import {PortfolioPage} from "../portfolio/portfolio";
import {AuthenticateProvider} from "../../providers/authenticate.providers";
import {ForgetpasswordPage} from "../forgetpassword/forgetpassword";
import * as _ from 'lodash';
import {Params_Authenticate} from "../../models/login.models";
import {Facebook} from "@ionic-native/facebook";
import {BackgroundMode} from "@ionic-native/background-mode";
import {OneSignal} from "@ionic-native/onesignal";

@Component({
    selector: 'page-home',
    templateUrl: 'login.html'
})
export class HomePage extends basePage {
    language: string;
    data: Params_Authenticate = new Params_Authenticate();
    user;
    userToken;
    remember: boolean = false;
    type_of_os = "";

    constructor(public navCtrl: NavController,
                private toast: Toast,
                private api: DataServiceProvider,
                private common: CommonServiceProvider,
                public translateService: TranslateService,
                public platform: Platform,
                public actionSheetCtrl: ActionSheetController,
                private storage: Storage,
                Keyboard: Keyboard,
                public firebaseprovider: FirebaseProvider,
                public firebase: Firebase,
                public alertCtrl: AlertController,
                public authenticateprovider: AuthenticateProvider,
                private fb: Facebook,
                private backgroundMode: BackgroundMode,
                private oneSignal: OneSignal) {
        super();

        // this.oneSignal.deleteTags(["name", "lastname"])
        this.oneSignal.sendTags({"name": "12", "lastname": "nader"});
        this.backgroundMode.enable();
        if (this.platform.is('ios')) {
            this.type_of_os = "ios"
        }
        if (this.platform.is('android')) {
            this.type_of_os = "android"
        }
        this.storage.get("userInfo1").then((data) => {
            if (data.USER_NAME != "" || !_.isEmpty(data)) {
                this.navCtrl.setRoot(PortfolioPage);
            }
        });
        Keyboard.disableScroll(true);
        // this.data.USER_NAME = 'adib';
        //  this.data.PASSWORD = '454540@EVDQJJX';
        this.data.USER_NAME = 'amine';
        this.data.PASSWORD = '243216@OPNLISI';
        this.api.DQNewSession().subscribe((data: any) => {
            this.common.SESSION_ID = data;
        });
        storage.get('language').then((val) => {
            this.translateService.use(val);
            this.common.onLanguageChange(val);
        });
        this.storage.get('gotUserToken').then((val) => {
            this.userToken = val;
            this.firebase.getToken()
                .then((tokenuser) => {
                    if (this.userToken != true) {
                        this.firebaseprovider.notRegistered(tokenuser, this.type_of_os);
                    }
                }).catch((error) => {
                this.firebaseprovider.onToast(error);
            });
        });
    }
    onForgetPassword() {
        this.navCtrl.push(ForgetpasswordPage)
    }
    Authenticate() {
        // this.user = this.firebaseprovider.login(this.data.USER_NAME, this.data.PASSWORD);
        this.Processing = true;
        this.authenticateprovider.Authenticate(this.data).subscribe((result: any) => {
            this.Processing = false;
            if (result.Is_Authentic) {
                if (this.remember === true) {
                    this.storage.set("userInfo1", this.data).then(() => {
                        this.navCtrl.setRoot(PortfolioPage);
                    });
                }
                else {

                    this.navCtrl.push(PortfolioPage);
                }
            }
            else {
                this.toast.show("Invalid User Name / Password", '2000', 'top').subscribe(() => {
                });
            }
        });
    }
    ProceedToRegister() {
        const alert = this.alertCtrl.create({
            message: 'Do You Have Policy?',
            buttons: [
                {
                    text: 'yes',
                    handler: () => {
                        this.navCtrl.push(RegisterPage);
                    }
                },
                {
                    text: 'No',
                    role: 'cancel',
                    handler: () => {
                    }
                }
            ]
        });
        alert.present();
    }
    presentActionSheet() {
        this.storage.get("UserUID").then((val) => {
            console.log(val)
        });
        let english = this.translateService.instant('english');
        let arabic = this.translateService.instant('arabic');
        let language = this.translateService.instant('language');
        let actionSheet = this.actionSheetCtrl.create({
            title: language,
            buttons: [
                {
                    text: english,
                    handler: () => {
                        //console.log('Destructive clicked');
                        this.common.onLanguageChange("en");
                        this.storage.set('language', 'en');
                    }
                }, {
                    text: arabic,
                    handler: () => {
                        //console.log('Archive clicked');
                        this.common.onLanguageChange("ar");
                        this.storage.set('language', 'ar');
                    }
                }
            ]
        });
        actionSheet.present();
    }

    onFacebook() {
        this.firebaseprovider.onFaceBookLogin();
    }

    onFirebase() {
        this.navCtrl.push(FirebaseanalyticsPage)
    }
}
