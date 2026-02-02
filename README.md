# NLA2 project: SVD Randomized SVD
autor:Aruzhan Abilmazhinova ABI0008

## Popis
Tento projekt porovnava klasicky algoritmus SVD s randomizovanou variantou z hlediska presnosti a vypocetniho casu:
- výpočetního času,
- paměťové náročnosti,
- přesnosti aproximace (relativní chyba ve Frobeniově normě)

Testování je provedeno na 3 různých typech matic:
1) Random – náhodná hustá matice  
2) Low Rank – matice s nízkou hodností (rank ~ 20)  
3) Structured – bloková (strukturovaná) matice  

## Soubory
- `matrices.py` – generování testovacích matic
- `svd_methods.py` – implementace `classic_svd` a `randomized_svd`
- `run_experiments.py` – měření času, paměti, chyby + vytvoření grafu
- `requirements.txt` – seznam knihoven

## Spuštění 
1) Vytvořte a aktivujte virtuální prostředí:
python3 -m venv venv
source venv/bin/activate

Nainstalujte knihovny:
pip install -r requirements.txt

Spusťte experiment:
python run_experiments.py


## Vysledky
Grafy a namerene hodnoty jsou ulozeny ve slozce `results`
Poznámka: V neinteraktivním prostředí se graf nemusí zobrazit na obrazovce,ale vždy se uloží do souboru `results/speed_comparison.png`.