#!/usr/bin/env python3

import sys
import logging
import requests
import json

global JAVAVXS


class Grdf:
    
    def __init__(self):
        
        self.session = None
        self.auth_nonce = None
        self.pceList = None
        self.measuresList = None
        self.whoiam = None
        
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept':'application/json, */*',
            'Connection': 'keep-alive'
        }
    
    # Login
    def login(self,username,password):
        
        # Get cookie
        req = self.session.get('https://monespace.grdf.fr/client/particulier/accueil')
        
        if not 'auth_nonce' in self.session.cookies:
            raise GazparLoginException("Cannot get auth_nonce.")
        else:
            logging.info("Cookies ok")
            
        self.auth_nonce = self.session.cookies.get('auth_nonce')
        logging.info("auth_nonce: " + self.auth_nonce)

        payload = {
            'email': username,
            'password': password,
            'capp': 'meg',
            'goto': 'https://sofa-connexion.grdf.fr:443/openam/oauth2/externeGrdf/authorize?response_type=code&scope=openid%20profile%20email%20infotravaux%20%2Fv1%2Faccreditation%20%2Fv1%2Faccreditations%20%2Fdigiconso%2Fv1%20%2Fdigiconso%2Fv1%2Fconsommations%20new_meg%20%2FDemande.read%20%2FDemande.write&client_id=prod_espaceclient&state=0&redirect_uri=https%3A%2F%2Fmonespace.grdf.fr%2F_codexch&nonce=' + self.auth_nonce + '&by_pass_okta=1&capp=meg'
        }
        
        # Login step 1
        req = self.session.post('https://login.monespace.grdf.fr/sofit-account-api/api/v1/auth', data=payload, allow_redirects=False)
        if not 'XSRF-TOKEN' in self.session.cookies:
            raise GazparLoginException("Login unsuccessful. Check your credentials.")
        else:
            logging.info("Login sucessfull.")
            
        
        # Login step 2
        req = self.session.get('https://sofa-connexion.grdf.fr:443/openam/oauth2/externeGrdf/authorize?response_type=code&scope=openid%20profile%20email%20infotravaux%20%2Fv1%2Faccreditation%20%2Fv1%2Faccreditations%20%2Fdigiconso%2Fv1%20%2Fdigiconso%2Fv1%2Fconsommations%20new_meg%20%2FDemande.read%20%2FDemande.write&client_id=prod_espaceclient&state=0&redirect_uri=https%3A%2F%2Fmonespace.grdf.fr%2F_codexch&nonce=' + self.auth_nonce + '&by_pass_okta=1&capp=meg')
    
        return req
        
    # Get account informations
    def getWhoami(self):
        
        req = self.session.get('https://monespace.grdf.fr/api/e-connexion/users/whoami')
        logging.info(req.txt)
        
        return req
        
        
    # Get list of PCE
    def getPceList(self):
        
        req = self.session.get('https://monespace.grdf.fr/api/e-conso/pce')
        logging.info(req.txt)
        
        return req
    
    # Get measures of a single PCE for a period range
    def getPceMeasures(self,pce, startDate, endDate):
        
        startDate = '2018-11-27'
        endDate = '2021-11-27'
        req = self.grdf.session.get('https://monespace.grdf.fr/api/e-conso/pce/consommation/informatives?dateDebut=' + startDate + '&dateFin=' + endDate + '&pceList%5B%5D=' + self.pce)
        
            
class Measure:
    
    def __init__(self, measure):
        
        self.volume = None
        self.energy = None
        self.gasDate = None
        self.measure = measure
        
        
    def getVolume():
        print("energy")
        
        
    def getEnergy():
        print("energy")
        
    def getMeasureDate():
        print("energy")
        
        
        
