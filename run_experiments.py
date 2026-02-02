import os
import time
import tracemalloc

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from svd_methods import classic_svd, randomized_svd
from matrices import get_test_matrices


def compute_error(A, U, S, Vt):
    A_approx = (U * S) @ Vt
    return np.linalg.norm(A - A_approx, ord="fro") / np.linalg.norm(A, ord="fro")


def measure(func, *args, **kwargs):
    """
    Změří čas běhu a maximální spotřebu paměti
    """
    tracemalloc.start()
    t0 = time.perf_counter()
    out = func(*args, **kwargs)
    t1 = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return out, (t1 - t0), peak / 1024.0  # KB


def main():
    os.makedirs("results", exist_ok=True)

    matrices = get_test_matrices()
    results = []

    k = 20  # cílová hodnost

    for name, A in matrices.items():
        # Klasické SVD
        (Uc, Sc, Vtc), t_c, mem_c = measure(classic_svd, A)
        err_c = compute_error(A, Uc[:, :k], Sc[:k], Vtc[:k, :])

        # Randomizované SVD
        (Ur, Sr, Vtr), t_r, mem_r = measure(randomized_svd, A, k)
        err_r = compute_error(A, Ur, Sr, Vtr)

        results.append([name, t_c, t_r, err_c, err_r, mem_c, mem_r])

    df = pd.DataFrame(
        results,
        columns=[
            "Matrix",
            "Classic Time",
            "Randomized Time",
            "Classic Error",
            "Randomized Error",
            "Classic Memory (KB)",
            "Randomized Memory (KB)",
        ],
    )

    print(df)

    # --- Graf rychlosti ---
    x = np.arange(len(df))
    width = 0.35

    plt.figure()
    plt.bar(x - width / 2, df["Classic Time"], width, label="Klasické SVD")
    plt.bar(x + width / 2, df["Randomized Time"], width, label="Randomizované SVD")
    plt.xticks(x, df["Matrix"])
    plt.ylabel("Čas (s)")
    plt.title("Srovnání rychlosti SVD")
    plt.legend()
    plt.savefig("results/speed_comparison.png", dpi=200, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
