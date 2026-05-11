import numpy as np
import matplotlib.pyplot as plt

# 定数の設定
H0 = 70  # km/s/Mpc
km_to_Mpc = 3.24078e-20
sec_to_Gyr = 3.17098e-17

# ハッブル定数を Gyr^-1 単位に変換
H0_Gyr = H0 * km_to_Mpc / sec_to_Gyr

# 物質優勢の平坦な宇宙における宇宙年齢 t0 (Gyr)
# t0 = 2 / (3 * H0)
t0 = 2 / (3 * H0_Gyr)

# プロット用のデータの生成 (0 から t0 まで)
t = np.linspace(0, t0, 500)
# スケール因子 a(t) = (t / t0)^(2/3)
a = (t / t0)**(2/3)

# グラフの描画
plt.figure(figsize=(8, 5))
plt.plot(t, a, label=f'Flat matter-only (t0 ≈ {t0:.2f} Gyr)', color='blue')

# グラフの装飾
# plt.title(r'Evolution of Scale Factor $a(t)$ in a Flat Matter-Only Universe', fontsize=12)
plt.xlabel('$t$ (Gyr)', fontsize=10)
plt.ylabel('$a$', fontsize=10)
# plt.axhline(1, color='red', linestyle='--', alpha=0.5, label='a = 1 (Present)')
# plt.axvline(t0, color='gray', linestyle=':', label='Current Age')
# plt.grid(True, which='both', linestyle='--', alpha=0.5)
# plt.legend()
plt.xlim(0, t0 * 1.05)
plt.ylim(0, 1.1)

# 表示
plt.show()

# %%

# 定数
H0 = 70.0  # km/s/Mpc
c = 299792.458  # km/s
t0 = 9.31  # (b)で計算した宇宙年齢 (Gyr)

# t の範囲 (0 から t0)
t = np.linspace(0, t0, 500)

# 固有距離 l(t) の計算
# l(t) = (2c / H0) * (1 - (t/t0)^(1/3))
l_t = (2 * c / H0) * (1 - (t / t0)**(1/3))

# プロット設定
plt.figure(figsize=(8, 5))
plt.plot(t, l_t, color='blue', linewidth=2)
plt.xlabel("$t$ (Gyr)")
plt.ylabel("$l(t)$ (Mpc)")
plt.show()
