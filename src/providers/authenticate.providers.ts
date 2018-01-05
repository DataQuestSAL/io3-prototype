import {Inject, Injectable} from '@angular/core';
import 'rxjs/add/operator/map';
import {
    Params_Authenticate,
} from '../models/login.models';

import {CommonServiceProvider} from "./common-service";
import {APP_CONFIG, AppConfig} from "../config/configs";
import {HttpClient, HttpHeaders} from "@angular/common/http";
@Injectable()
export class AuthenticateProvider {
    url: string = '';
    API: string = "";
    constructor(public http: HttpClient,
                private common: CommonServiceProvider,
                @Inject(APP_CONFIG) public config: AppConfig) {
        this.API = this.config.apiAddress;
    }
    Authenticate(Params: Params_Authenticate){
        this.url = this.API + '/Authenticate';
        const headers = new HttpHeaders({'Content-Type': 'application/json', 'SESSION_ID': this.common.SESSION_ID});
        return this.http.post(this.url, JSON.stringify(Params), {headers})
    }
}
