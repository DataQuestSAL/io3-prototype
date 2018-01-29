import {Component} from '@angular/core';
import {NavController, NavParams} from 'ionic-angular';
import {OneSignal} from "@ionic-native/onesignal";

@Component({
    selector: 'page-tags',
    templateUrl: 'tags.html',
})
export class TagsPage {
    name = "";
    lastname = "";

    constructor(public navCtrl: NavController,
                public navParams: NavParams,
                private oneSignal: OneSignal) {
    }
    onInsertTags() {
        //console.log(this.name)
        this.oneSignal.sendTags({"name": this.name, "lastname": this.lastname});
    }


}
