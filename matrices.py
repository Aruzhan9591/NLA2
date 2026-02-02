import numpy as np

def get_test_matrices():
    # Pro opakovatelnost výsledků
    np.random.seed(0)

    # 1) Náhodná hustá matice
    A1 = np.random.rand(1000, 500)

    # 2) Matice s nízkou hodností (dobrá pro SVD)
    U_low = np.random.rand(1000, 20)
    V_low = np.random.rand(20, 500)
    A2 = U_low @ V_low

    # 3) Strukturovaná matice (bloková)
    A3 = np.zeros((800, 800))
    for i in range(10):
        A3[i*80:(i+1)*80, i*80:(i+1)*80] = np.random.rand(80, 80)

    return {
        "Random": A1,
        "Low Rank": A2,
        "Structured": A3
    }
