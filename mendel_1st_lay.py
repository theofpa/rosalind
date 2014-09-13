k=22.0
m=16.0
n=26.0
sum_f = k+m+n
sum_s  = k+m+n-1
f_k = 1.0 * k/sum_f
f_m = 1.0 * m/sum_f
f_n = 1.0 * n/sum_f
k_k = f_k * (k-1)/sum_s
k_m = f_k * m/sum_s
k_n = f_k * n/sum_s
m_k = f_m * k/sum_s
m_m = f_m * 0.75 * (m-1)/sum_s
m_n = f_m * 0.5 * n/sum_s
n_k = f_n * k/sum_s
n_m = f_n * 0.5 * m/sum_s

total = k_k+ k_m+ k_n+ m_k+ m_m+ m_n+ n_k+ n_m

print total