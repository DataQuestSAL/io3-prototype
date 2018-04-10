import {Component, OnInit} from '@angular/core';
import {NavController, NavParams} from 'ionic-angular';

@Component({
    selector: 'page-portfolioinformation',
    templateUrl: 'portfolioinformation.html',
})
export class PortfolioinformationPage implements OnInit {
    policy;
    tabs = [];

    constructor(public navCtrl: NavController, public navParams: NavParams) {
    }

    ngOnInit() {
        this.policy = this.navParams.get("policy");
        console.log(JSON.stringify(this.policy.Tabs));
        this.tabs = this.policy.Tabs.split("^",)
        console.log(this.tabs)


    }

}
