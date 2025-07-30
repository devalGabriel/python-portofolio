from django.shortcuts import render
from .forms import InvestmentSimulationForm

def home(request):
    return render(request, 'simulation/home.html')

def simulation_form(request):
    if request.method == 'POST':
        form = InvestmentSimulationForm(request.POST)
        if form.is_valid():
            # Trimitem parametrii validați la rezultat (prin sesiune, context, sau direct)
            params = form.cleaned_data
            request.session['sim_params'] = params  # Stocăm în sesiune
            return render(request, 'simulation/result.html', simulate_investment(params))
    else:
        form = InvestmentSimulationForm()
    return render(request, 'simulation/investment_form.html', {'form': form})

# Funcție utilitară pentru calcul simulare (vedeți mai jos)
def simulate_investment(params):
    # Extrage parametrii
    suma_initiala = params['suma_initiala']
    aport_lunar = params['aport_lunar']
    ani = params['ani']
    # ... restul ...
    # Calcul evoluție imobiliar și bursă an de an
    rows = []
    total_imob = suma_initiala
    total_bursa = suma_initiala
    for year in range(1, ani+1):
        # Imobiliare
        venit_chirie = total_imob * params['randament_chirie'] / 100
        total_imob += venit_chirie + aport_lunar * 12
        total_imob += total_imob * params['crestere_pret'] / 100
        total_imob -= total_imob * params['cost_mentenanta'] / 100
        total_imob -= total_imob * params['taxare'] / 100
        # Bursă
        venit_dividend = total_bursa * params['randament_dividend'] / 100
        total_bursa += venit_dividend + aport_lunar * 12
        total_bursa += total_bursa * params['randament_bursa'] / 100
        total_bursa -= total_bursa * params['comision'] / 100
        rows.append({
            'an': year,
            'imobiliar': round(total_imob, 2),
            'bursa': round(total_bursa, 2),
        })
    return {
        'params': params,
        'rows': rows,
        'rez_imobiliar': round(total_imob, 2),
        'rez_bursa': round(total_bursa, 2),
    }

def simulation_result(request):
    params = request.session.get('sim_params')
    if not params:
        return render(request, 'simulation/result.html', {'error': 'Nu există simulare.'})
    results = simulate_investment(params)
    return render(request, 'simulation/result.html', results)
