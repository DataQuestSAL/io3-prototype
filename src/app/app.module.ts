import {BrowserModule} from '@angular/platform-browser';
import {ErrorHandler, NgModule} from '@angular/core';
import {IonicApp, IonicErrorHandler, IonicModule} from 'ionic-angular';
import {SplashScreen} from '@ionic-native/splash-screen';
import {StatusBar} from '@ionic-native/status-bar';
import {Keyboard} from '@ionic-native/keyboard';
import {DatePicker} from '@ionic-native/date-picker';
import {MyApp} from './app.component';
import {HomePage} from '../pages/login/login';
import {DataServiceProvider} from '../providers/data-service';
import {CommonServiceProvider} from '../providers/common-service';
import {FormsModule} from '@angular/forms';
import {Http, HttpModule} from '@angular/http';
import {RegisterPage} from '../pages/register/register';
import {PortfolioPage} from '../pages/portfolio/portfolio';
import {Toast} from '@ionic-native/toast';
import {LandingPage} from '../pages/landing/landing';
import {TranslateStore} from "@ngx-translate/core/src/translate.store";
import {IonicStorageModule} from '@ionic/storage';
import {TranslateModule, TranslateLoader} from '@ngx-translate/core';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';
import {FirebaseanalyticsPage} from "../pages/firebaseanalytics/firebaseanalytics";
import {Firebase} from "@ionic-native/firebase";
import {FirebaseProvider} from '../providers/firebase';
import {AngularFireModule} from 'angularfire2';
import {AngularFireAuthModule} from 'angularfire2/auth';
import {LogoutPage} from "../pages/logout/logout";
import {APP_CONFIG, danny, rony} from "../config/configs";
import {AuthenticateProvider} from '../providers/authenticate.providers';
import {RegisterwithpolicyPage} from "../pages/registerwithpolicy/registerwithpolicy";
import {ForgetpasswordPage} from "../pages/forgetpassword/forgetpassword";
import {RegisterProvider} from '../providers/register-provider';
import {ForgetpasswordProvider} from '../providers/forgetpassword-provider';
import {environment} from "../environments/environment";
import {Facebook} from "@ionic-native/facebook";
import {FCM} from "@ionic-native/fcm";
import {BackgroundMode} from "@ionic-native/background-mode";
import {HttpClientModule} from "@angular/common/http";
import {OneSignal} from "@ionic-native/onesignal";
import {TagsPage} from "../pages/tags/tags";
import {AngularFirestoreModule} from 'angularfire2/firestore';
import {PhonenumberPage} from "../pages/phonenumber/phonenumber";
import {ValidationcodePage} from "../pages/validationcode/validationcode";
import {PortfolioinformationPage} from "../pages/portfolioinformation/portfolioinformation";
import {SpinnerDialog} from "@ionic-native/spinner-dialog";
import {NativeStorage} from "@ionic-native/native-storage";
import {NetworkProvider} from '../providers/network';
import {Network} from "@ionic-native/network";


export function createTranslateLoader(http: Http) {
    return new TranslateHttpLoader(http, './assets/i18n/', '.json');
}

// export function createTranslateLoader(http: Http) {
//     return new TranslateHttpLoader(http, './assets/i18n/', '.json');
// }

export const firebaseConfig = {
    apiKey: "AIzaSyDPPNUCQHs602A0x26OtKXg0k-ofQok_3E",
    authDomain: "client-space-mobile.firebaseapp.com",
    databaseURL: "https://client-space-mobile.firebaseio.com",
    projectId: "client-space-mobile",
    storageBucket: "client-space-mobile.appspot.com",
    messagingSenderId: "947181869234"
};

@NgModule({
    declarations: [
        MyApp,
        LandingPage,
        HomePage,
        RegisterPage,
        PortfolioPage,
        FirebaseanalyticsPage,
        LogoutPage,
        RegisterwithpolicyPage,
        ForgetpasswordPage,
        TagsPage,
        PhonenumberPage,
        ValidationcodePage,
        PortfolioinformationPage
    ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        HttpClientModule,
        IonicStorageModule.forRoot(),
        TranslateModule.forRoot({
            loader: {
                provide: TranslateLoader,
                useFactory: (createTranslateLoader),
                deps: [Http]
            }
        }),
        IonicModule.forRoot(MyApp, {
            scrollPadding: false,
            scrollAssist: true,
            autoFocusAssist: false
        }),
        AngularFireModule.initializeApp(firebaseConfig),
        AngularFireAuthModule,
        AngularFirestoreModule.enablePersistence(),
    ],
    bootstrap: [IonicApp],
    entryComponents: [
        MyApp,
        LandingPage,
        HomePage,
        RegisterPage,
        PortfolioPage,
        FirebaseanalyticsPage,
        LogoutPage,
        RegisterwithpolicyPage,
        ForgetpasswordPage,
        TagsPage,
        PhonenumberPage,
        ValidationcodePage,
        PortfolioinformationPage
    ],
    providers: [
        StatusBar,
        SplashScreen,
        DatePicker,
        Keyboard,
        Toast,
        {provide: ErrorHandler, useClass: IonicErrorHandler},
        DataServiceProvider,
        CommonServiceProvider,
        TranslateStore,
        AuthenticateProvider,
        Firebase,
        FirebaseProvider,
        {provide: APP_CONFIG, useValue: danny},
        AuthenticateProvider,
        RegisterProvider,
        ForgetpasswordProvider,
        Facebook,
        FCM,
        BackgroundMode,
        OneSignal,
        Firebase,
        SpinnerDialog,
        NativeStorage,
        NetworkProvider,
        Network
    ]
})
export class AppModule {
}
