from scipy.special import binom

import numpy as np

import matplotlib.pyplot as plt


def get_head_distrib(n_,k_):
    return lambda p : binom(n_,k_)*(p)**(k_)*(1.-p)**(n_-k_)


if __name__ == "__main__":

    head_bias = np.linspace(0,1,1000)

    p_20_8 = get_head_distrib(20,8)
    p_40_17 = get_head_distrib(40,17)

    p_20_8_ = np.argmax(p_20_8(head_bias))
    p_40_17_ = np.argmax(p_40_17(head_bias))

    print(head_bias[p_20_8_])
    print(head_bias[p_40_17_])

    plt.plot(head_bias,p_20_8(head_bias),'b')
    plt.plot(head_bias[p_20_8_],p_20_8(head_bias[p_20_8_]),'xr')
    plt.plot(head_bias,p_40_17(head_bias),'g')
    plt.plot(head_bias[p_40_17_],p_40_17(head_bias[p_40_17_]),'xr')
    plt.show()
