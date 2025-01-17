import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# YOU NEED TO CHANGE THIS: copy the result path from above - without the trailing "result.yaml"
test_result_dir = "../results/agent_obs1_weighted-f05d05n0_64a_64c_099gam_00001tau_001alp_0001dec/" \
                  "5node-in2-rand-cap0-2/abc/det-arrival10_det-size001_duration100/" \
                  "2022-06-01_17-11-13_seed2545/test-2022-06-01_17-11-13_seed2545"
# read test results into pandas data frame
test_results = os.path.join(test_result_dir, "metrics.csv")
df = pd.read_csv(test_results)

# let's add a column with the percentage of successful flows (in [0,100]%)
df["success_perc"] = 100 * df["successful_flows"] / df["total_flows"]

X = df["time"]
Y1 = df["success_perc"]
Y2 = df["avg_end2end_delay"]

# create figure instance
fig1 = plt.figure(1)
fig1.set_figheight(11)
fig1.set_figwidth(8.5)

ax = fig1.add_subplot(2, 1, 1)
ax.plot(X, Y1)
plt.xlabel('time')
plt.ylabel('success_perc')

ax_1 = fig1.add_subplot(2, 1, 2)
ax_1 .plot(X, Y2)
plt.xlabel('time')
plt.ylabel('avg_end2end_delay')

plt.savefig(f'{test_result_dir}/agent_obs1_weighted-f05d05n0_64a_64c_099gam_00001tau_001alp_0001dec.png',
            bbox_inches="tight", pad_inches=2, edgecolor='black', transparent=None)

