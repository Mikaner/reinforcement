import numpy as np
import matplotlib.pyplot as plt

class Izhikevich:
    def __init__(self, a, b, c, d):
        """
        Izhikevich neuron model
        :param a: uのスケーリング係数
        :param b: vに対するuの感受性度合い
        :param c: 静止膜電位
        :param d: 発火後の膜電位が落ち着くまでを司る係数
        """
        self.a, self.b, self.c, self.d = a, b, c, d

    def calc(self, inputs, time=300, dt=0.5, tci=10):
        """
        膜電位(Membrane potential) v と回復変数(Recovery variable) u を計算する
        :param inputs:
        :param weights:
        :param time:
        :param dt:
        :param tci:
        :return:
        """
        v = self.c
        u = self.d
        i = 0

        monitor = {'v':[], 'u':[]}

        for t in range(int(time/dt)):
            # uを計算
            du = self.a * (self.b * v - u)
            u += du * dt
            monitor['u'].append(u)

            # vを計算
            dv = 0.04 * v**2 + 5 * v + 140 - u + inputs[t]
            v += dv * dt
            monitor['v'].append(v)

            # 発火処理
            if v >= 30:
                v = self.c
                u += self.d

        return monitor

if __name__=='__main__':
    time = 300
    dt = 0.5
    pre = 50

    # 入力データ
    input_data = np.sin(0.5*np.arange(0,time,dt))
    input_data = np.where(input_data > 0, 20, 0) + 10 * np.random.rand(int(time/dt))
    input_data_2 = np.cos(0.4 * np.arange(0, time, dt) + 0.5)
    input_data_2 = np.where(input_data_2 > 0, 10, 0)
    input_data += input_data_2

    #Izhikevichニューロンの生成
    neuron = Izhikevich(
        a=0.02, 
        b=0.2,
        c=-65,
        d=8
    )
    history = neuron.calc(input_data, time=time, dt=dt)

    plt.figure(figsize=(12,8))

    #入力データ
    plt.subplot(3,1,1)

    plt.plot(input_data)
    plt.xlim(0, time)
    plt.ylim(-1, pre)
    plt.ylabel('Input current')

    # 膜電位
    plt.subplot(3,1,2)
    plt.plot(history['v'])
    plt.ylabel('Membrane potential $v$ [mV]')

    # 膜電位
    plt.subplot(3,1,3)
    plt.plot(history['u'], c='tab:orange')
    plt.xlabel('time [ms]')
    plt.ylabel('Recovery variable $u$')

    plt.show()