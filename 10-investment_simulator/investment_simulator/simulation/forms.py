from django import forms

class InvestmentSimulationForm(forms.Form):
    suma_initiala = forms.FloatField(label="Suma inițială (lei)", min_value=0, initial=50000)
    aport_lunar = forms.FloatField(label="Aport lunar (lei)", min_value=0, initial=1000)
    ani = forms.IntegerField(label="Durată (ani)", min_value=1, max_value=40, initial=10)
    
    # Parametri pentru imobiliare
    randament_chirie = forms.FloatField(label="Randament chirie anual (%)", min_value=0, max_value=100, initial=5)
    crestere_pret = forms.FloatField(label="Creștere anuală preț imobil (%)", min_value=-10, max_value=20, initial=2)
    cost_mentenanta = forms.FloatField(label="Cost mentenanță/an (%)", min_value=0, max_value=20, initial=1)
    taxare = forms.FloatField(label="Taxare totală/an (%)", min_value=0, max_value=20, initial=1)
    
    # Parametri bursă
    randament_bursa = forms.FloatField(label="Randament bursă anual (%)", min_value=-30, max_value=50, initial=8)
    randament_dividend = forms.FloatField(label="Randament dividend anual (%)", min_value=0, max_value=10, initial=1.5)
    comision = forms.FloatField(label="Comision anual (%)", min_value=0, max_value=5, initial=0.5)
