import numpy as np
import matplotlib.pyplot as plt

"""
# How to use:
1. Go to Sample-Factory, actor_critic.py: ActorCriticSeparateWeights: forward function
2. Set a debug point at the first line of the forward function.
    x = self.forward_head(normalized_obs_dict)
3. In PyCharm, go to Console, copy and past code below

tmp_score={}
for i in range(-20, 21):
    normalized_obs_dict['obs'][0][2]=i * 0.1
    x = self.forward_head(normalized_obs_dict)
    x, new_rnn_states = self.forward_core(x, rnn_states)
    result = self.forward_tail(x, values_only, sample_actions=True)
    tmp_score[i] = result['values'].item()

print(tmp_score)

4. Copy and paste the print info and replace v_value dict below. 
"""

v_value = {-20: -0.8389064073562622, -19: -0.7826626300811768, -18: -0.7211709022521973, -17: -0.6561537981033325,
           -16: -0.5925958156585693, -15: -0.5331193208694458, -14: -0.472306489944458, -13: -0.39593398571014404,
           -12: -0.29337072372436523, -11: -0.19148313999176025, -10: -0.12815141677856445, -9: -0.10008419305086136,
           -8: -0.09214044362306595, -7: -0.09645140916109085, -6: -0.10988188534975052, -5: -0.12992823123931885,
           -4: -0.15292489528656006, -3: -0.17494475841522217, -2: -0.19359171390533447, -1: -0.20843374729156494,
           0: -0.2201685905456543, 1: -0.22974956035614014, 2: -0.23797106742858887, 3: -0.24537742137908936,
           4: -0.25230085849761963, 5: -0.25892817974090576, 6: -0.26535236835479736, 7: -0.27160918712615967,
           8: -0.2777014970779419, 9: -0.2836127281188965, 10: -0.28931915760040283, 11: -0.2947978973388672,
           12: -0.30003488063812256, 13: -0.30502963066101074, 14: -0.3097987174987793, 15: -0.3143727779388428,
           16: -0.3187958002090454, 17: -0.3231208324432373, 18: -0.32740604877471924, 19: -0.33171212673187256,
           20: -0.33610010147094727}

x = np.array(list(v_value.keys())) * 0.1

y = np.array(list(v_value.values()))

xmax = x[np.argmax(y)]
ymax = y.max()
text = "x={:.3f}, y={:.3f}".format(xmax, ymax)
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
arrowprops = dict(arrowstyle="->", connectionstyle="angle,angleA=0,angleB=60")
kw = dict(xycoords='data', textcoords="axes fraction",
          arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
plt.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)

plt.ylim((-1.2, 0.2))

plt.plot(x, y)

plt.xlabel('rel height to goal - axis')

plt.ylabel('V value - axis')

plt.title('V value plot')

plt.show()


# {'obs': tensor([[ 6.8707e-02, -8.9396e-02,  1.0000e+00,  1.4326e-01,  7.8522e-02,
#          -1.1874e-01,  9.5626e-01,  2.9245e-01, -5.5469e-03, -2.9246e-01,
#           9.5628e-01, -6.4736e-04,  5.1151e-03,  2.2413e-03,  9.9998e-01,
#           2.8985e-01,  8.6626e-01,  1.2647e-01,  1.1000e+00,  1.1000e+00,
#           1.1000e+00,  1.1000e+00,  1.1000e+00,  1.1000e+00,  1.1000e+00,
#           1.1000e+00,  1.1000e+00]], device='cuda:0')}