import { Component } from '@angular/core';
import { Platform } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { Keyboard } from "@ionic-native/keyboard";
import { TranslateService } from '@ngx-translate/core';
import {LandingPage} from "../pages/landing/landing";
import {OneSignal} from "@ionic-native/onesignal";
import {TagsPage} from "../pages/tags/tags";

@Component({
  templateUrl: 'app.html'
})
export class MyApp {
 // rootPage:any = LandingPage;
  rootPage:any = TagsPage;

  constructor(platform: Platform,
              statusBar: StatusBar,
              splashScreen: SplashScreen,
              kb: Keyboard,translate: TranslateService,
              private oneSignal: OneSignal) {
    translate.setDefaultLang('en');

    platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
        this.oneSignal.startInit('9977658b-4e06-4a64-b0f9-c3fadc9eaa72', '947181869234');

        this.oneSignal.inFocusDisplaying(this.oneSignal.OSInFocusDisplayOption.InAppAlert);

        this.oneSignal.registerForPushNotifications();


        this.oneSignal.handleNotificationReceived().subscribe(() => {
            // do something when notification is received
        });

        this.oneSignal.handleNotificationOpened().subscribe(() => {
            // do something when a notification is opened
        });

        this.oneSignal.endInit();

      statusBar.styleDefault();
      splashScreen.hide();
      kb.disableScroll(true);
    });
  }
}

