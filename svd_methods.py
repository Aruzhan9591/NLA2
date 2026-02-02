import numpy as np
from scipy.linalg import svd, qr

def classic_svd(A):
    """
    Klasické SVD pomocí SciPy
    """
    U, S, Vt = svd(A, full_matrices=False)
    return U, S, Vt


def randomized_svd(A, k, p=5, q=1, seed=0):
    """
    Jednoduchá implementace randomizovaného SVD (Halko et al.)
    
    k  - cílová hodnost
    p  - oversampling
    q  - počet power iterací
    """
    rng = np.random.default_rng(seed)
    m, n = A.shape
    l = k + p

    # 1) Náhodná projekce
    Omega = rng.normal(size=(n, l))
    Y = A @ Omega

    # 2) Power iterace (zlepšení přesnosti)
    for _ in range(q):
        Y = A @ (A.T @ Y)

    # 3) QR ortogonalizace
    Q, _ = qr(Y, mode="economic")

    # 4) Projekce do menšího prostoru
    B = Q.T @ A

    # 5) SVD malé matice
    U_tilde, S, Vt = svd(B, full_matrices=False)

    # 6) Zpět do původního prostoru
    U = Q @ U_tilde

    return U[:, :k], S[:k], Vt[:k, :]
