import {Component} from '@angular/core';
import {LoadingController, NavController, NavParams, PopoverController} from 'ionic-angular';
import {DataServiceProvider} from '../../providers/data-service';
import {Polcom} from '../../models/polcom.models';
import {Storage} from '@ionic/storage';
import {LogoutPage} from "../logout/logout";
import {AuthenticateProvider} from "../../providers/authenticate.providers";
import {PortfolioinformationPage} from "../portfolioinformation/portfolioinformation";
import {NativeStorage} from "@ionic-native/native-storage";

@Component({
    selector: 'page-portfolio',
    templateUrl: 'portfolio.html',
})
export class PortfolioPage {
    policies: Polcom[] = [];
    user = {};

    constructor(public navCtrl: NavController,
                public navParams: NavParams,
                private api: DataServiceProvider,
                private storage: Storage,
                public popoverCtrl: PopoverController,
                private dataservice: DataServiceProvider,
                private loadCtrl: LoadingController,
                public authenticateprovider: AuthenticateProvider,
                private nativeStorage: NativeStorage) {
        this.storage.get("userInfo1").then((data) => {
            this.user = data;
            if (data != null) {
                this.authenticateprovider.Authenticate(data).subscribe((data) => {
                    this.Get_Portfolio();
                }, (err) => {
                    this.Get_Portfolio();
                })
            }
            else {
                this.Get_Portfolio();
            }
        });
    }

    Get_Portfolio() {
        const load = this.loadCtrl.create({});
        load.present();
        this.api.Get_Portfolio().subscribe((data: any) => {
            this.policies = data;
            this.nativeStorage.setItem('policies', data)
                .then(
                    () => console.log('Stored item!'),
                    error => console.error('Error storing item', error)
                );

            load.dismiss();
        }, (err) => {
            this.nativeStorage.getItem('policies')
                .then(
                    (data) => {
                        this.policies= data;
                    },
                    (error) => {
                        console.error(error)
                    }
                );
            load.dismiss();
        });
    }

    presentPopover(myEvent) {
        let popover = this.popoverCtrl.create(LogoutPage, {user: this.user});
        popover.present({
            ev: myEvent
        });
    }

    onPolicyInformation(policy) {
        this.navCtrl.push(PortfolioinformationPage,{policy})
    }
}
