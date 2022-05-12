# PT-2022
A force plate — measure the force and moments
Force: Fx Fy Fz
Moment: Mx, My, Mz (rotation around x, y, z)

N = 2291 participants; 4 trials per leg per participant


Data:
IDinfo file: 15,696 entries, 4 columns (ID, KNEE, TRIAL, tr_length)
                 Trial = trial number
                 tr_length = #frames of data for trial

Discrete file: 15,696 entries, 29 columns (IGRF_impulse, aGRF_impulse....)


Time series data are contained in the following files:
GRFx, GRFy, GRFz, COPx, COPy, Mx, My, and Mz are not time-normalized
AP_GRF_stance_N, ML_GRF_stance_N, V_GRF_stance_N, COPx_stance, and COPy_stance are time-normalized to stance (100 data points representing the time the foot is in contact with the ground)

GRFx,y,z = force in x,y,z
Mx,y,z = moment in x,y,z
COPx,y = center of pressure in x,y


