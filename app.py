from flask import Flask, render_template, request

import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('randomForest_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Year = int(request.form['year'])
        Year=2021-Year
        
        Kms_Driven=int(request.form['kilometers'])
        Kms_Driven2=np.log(Kms_Driven)
        
        owner_Second =request.form['owner']
        if(owner_Second == 'Second Owner'):
            owner_Second =1
            owner_Third = 0
            owner_Fourth_Above = 0
            owner_TestDrive_Car = 0
        elif(owner_Second  == 'Third Owner'):
            owner_Second =0
            owner_Third = 1
            owner_Fourth_Above= 0
            owner_TestDrive_Car = 0
        elif(owner_Second  == 'Fourth & Above Owner'):
            owner_Second =0
            owner_Third = 0
            owner_Fourth_Above= 1
            owner_TestDrive_Car = 0
        elif(owner_Second  == 'Test Drive Car'):
            owner_Second =0
            owner_Third = 0
            owner_Fourth_Above= 0
            owner_TestDrive_Car = 1
        else :
            owner_Second = 0
            owner_Third = 0
            owner_Fourth_Above= 0
            owner_TestDrive_Car = 0
            
        fuel_Petrol=request.form['fuel_type']
        if(fuel_Petrol=='Petrol'):
                fuel_Petrol=1
                fuel_Diesel=0
                fuel_Electric=0
                fuel_LPG=0
        elif(fuel_Petrol=='Diesel'):
              fuel_Petrol=0
              fuel_Diesel=1
              fuel_Electric=0
              fuel_LPG=0
        elif(fuel_Petrol=='Electric'):
              fuel_Petrol=0
              fuel_Diesel=0
              fuel_Electric=1
              fuel_LPG=0
        elif(fuel_Petrol=='LPG'):
              fuel_Petrol=0
              fuel_Diesel=0
              fuel_Electric=0
              fuel_LPG=1
        else:
              fuel_Petrol=0
              fuel_Diesel=0
              fuel_Electric=0
              fuel_LPG=0
        
        
        Seller_Type_Individual=request.form['seller_type']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual = 1
            Seller_Type_Trustmark_Dealer = 0
        elif(Seller_Type_Individual=='Trustmark Dealer'):
            Seller_Type_Individual = 0
            Seller_Type_Trustmark_Dealer = 1
        else:
            Seller_Type_Individual = 0
            Seller_Type_Trustmark_Dealer = 0
            
        Transmission_Manual=request.form['transmission']
        if(Transmission_Manual=='Manual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
            
            
        prediction=model.predict([[Kms_Driven2,Year,fuel_Diesel,fuel_Electric,fuel_LPG,fuel_Petrol,Seller_Type_Individual,Seller_Type_Trustmark_Dealer,Transmission_Manual,owner_Fourth_Above,owner_Second,owner_TestDrive_Car,owner_Third]])
        output=round(prediction[0],2)
        
        
        return render_template('index.html',prediction_text="The price for your car is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

