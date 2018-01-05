import {Injectable, Inject} from '@angular/core';
import 'rxjs/add/operator/map';
import {CommonServiceProvider} from './common-service';
import { Params_GetSignup} from '../models/Params_GetSignup.models'
import {Params_Acquire_PNS_Token} from '../models/Params_Acquire_PNS_Token.models'
import 'rxjs/Rx';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';
import {APP_CONFIG, AppConfig} from "../config/configs";
import {HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable()
export class DataServiceProvider {
    SESSION_ID: string = '';
    url: string = '';
    url1: string = '';
    API: string = '';
    Nodeapi: string = '';
    constructor(private http:HttpClient,
                private common: CommonServiceProvider,
                @Inject(APP_CONFIG) public config: AppConfig) {
        this.API = this.config.apiAddress;
        this.Nodeapi = this.config.apiNode;
    }
    DQNewSession(){
        this.url = this.API + '/DQNewSession'
        const headers = new HttpHeaders({'Content-Type': 'application/json'});
        return this.http.post(this.url, {}, {headers});
    }
    GetSignup(Params: Params_GetSignup){
        this.url = this.API + '/GetSignup';
        const headers = new HttpHeaders({'Content-Type': 'application/json', 'SESSION_ID': this.common.SESSION_ID});
        return this.http.post(this.url, JSON.stringify(Params), {headers});
    }
    Get_Portfolio(){
        this.url = this.API + '/Get_Portfolio';
        const headers = new HttpHeaders({'Content-Type': 'application/json', 'SESSION_ID': this.common.SESSION_ID});
        return this.http.post(this.url, {}, {headers});
    }
    Acquire_PNS_Token(Params: Params_Acquire_PNS_Token) {
        this.url = this.API + '/Acquire_PNS_Token';
        const headers = new HttpHeaders({'Content-Type': 'application/json', 'SESSION_ID': this.common.SESSION_ID});
        return this.http.post(this.url, JSON.stringify(Params), {headers});

    }
    registerInfo(data) {
        this.url1 = this.Nodeapi + 'registerInfo';
        const headers = new HttpHeaders({'Content-Type': 'application/json', 'SESSION_ID': this.common.SESSION_ID});
        return this.http.post(this.url1, JSON.stringify(data), {headers});
    }
}
