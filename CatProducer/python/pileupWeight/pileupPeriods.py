import FWCore.ParameterSet.Config as cms
pileupMap = {
#pileupCalc.py -i Cert_periodB.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 75 --numPileupBins 75 PileUpData.root 
"Cert_periodB":cms.vdouble(
1.827615e+03,6.033210e+04,3.268561e+05,6.323221e+05,1.046370e+06,
1.444898e+06,1.962122e+06,6.460702e+06,2.361713e+07,4.912165e+07,
9.039170e+07,1.420697e+08,1.904642e+08,2.445683e+08,3.137946e+08,
3.878404e+08,4.469793e+08,4.833848e+08,4.997058e+08,4.968971e+08,
4.753253e+08,4.374124e+08,3.873608e+08,3.301836e+08,2.704715e+08,
2.119905e+08,1.580193e+08,1.113574e+08,7.384644e+07,4.595370e+07,
2.681164e+07,1.467945e+07,7.557888e+06,3.670176e+06,1.687226e+06,
7.379710e+05,3.097343e+05,1.269643e+05,5.282669e+04,2.403573e+04,
1.317918e+04,9.090077e+03,7.473316e+03,6.760465e+03,6.400820e+03,
6.201528e+03,6.088534e+03,6.025625e+03,5.989230e+03,5.961484e+03,
5.928096e+03,5.873671e+03,5.794901e+03,5.688414e+03,5.551966e+03,
5.385427e+03,5.190282e+03,4.969206e+03,4.725697e+03,4.463795e+03,
4.187838e+03,3.902266e+03,3.611464e+03,3.319626e+03,3.030648e+03,
2.748045e+03,2.474892e+03,2.213778e+03,1.966797e+03,1.735538e+03,
1.521105e+03,1.324147e+03,1.144897e+03,9.832198e+02,8.386674e+02,
),
"Cert_periodC":cms.vdouble(
9.915644e-02,1.892260e+04,6.859973e+04,1.761899e+05,3.087824e+05,
3.439245e+05,3.458968e+05,7.373282e+05,4.131672e+06,1.820018e+07,
3.671185e+07,4.572336e+07,5.230873e+07,6.470865e+07,7.619611e+07,
8.756544e+07,1.087722e+08,1.356214e+08,1.582765e+08,1.754373e+08,
1.881426e+08,1.944200e+08,1.938966e+08,1.887420e+08,1.797144e+08,
1.651970e+08,1.441769e+08,1.186096e+08,9.234741e+07,6.858256e+07,
4.876523e+07,3.311818e+07,2.139676e+07,1.314795e+07,7.714057e+06,
4.337653e+06,2.339248e+06,1.207654e+06,5.953008e+05,2.795711e+05,
1.248884e+05,5.302153e+04,2.139111e+04,8.205277e+03,2.995302e+03,
1.041708e+03,3.454904e+02,1.093474e+02,3.303566e+01,9.525315e+00,
2.619582e+00,6.864762e-01,1.712164e-01,4.059120e-02,9.135400e-03,
1.949446e-03,3.940223e-04,7.536354e-05,1.363045e-05,2.329851e-06,
3.760037e-07,5.730044e-08,8.191240e-09,1.124603e-09,1.134531e-10,
0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,
0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,
),
#pileupCalc.py -i Cert_periodD.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 75 --numPileupBins 75 PileUpData.root 
"Cert_periodD":cms.vdouble(
2.623263e+02,8.070246e+04,2.185628e+05,4.368467e+05,5.872964e+05,
8.453572e+05,1.232068e+06,1.263695e+06,1.499083e+06,2.484487e+06,
9.414705e+06,4.218878e+07,1.094528e+08,1.741409e+08,2.143541e+08,
2.435430e+08,2.671308e+08,2.840531e+08,2.950131e+08,2.999072e+08,
2.988255e+08,2.926351e+08,2.819071e+08,2.662353e+08,2.451191e+08,
2.190592e+08,1.895582e+08,1.584790e+08,1.275842e+08,9.843488e+07,
7.239964e+07,5.052439e+07,3.333630e+07,2.075135e+07,1.217732e+07,
6.740947e+06,3.528047e+06,1.752893e+06,8.316325e+05,3.794809e+05,
1.677872e+05,7.232500e+04,3.049510e+04,1.257708e+04,5.059536e+03,
1.976582e+03,7.463715e+02,2.712834e+02,9.459838e+01,3.156946e+01,
1.006471e+01,3.061477e+00,8.876642e-01,2.451591e-01,6.445998e-02,
1.612814e-02,3.838612e-03,8.688215e-04,1.869584e-04,3.824108e-05,
7.433602e-06,1.373080e-06,2.408961e-07,4.016503e-08,6.329697e-09,
9.531432e-10,9.763118e-11,0.000000e+00,0.000000e+00,0.000000e+00,
0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,
),
#pileupCalc.py -i Cert_periodE.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 75 --numPileupBins 75 PileUpData.root 
"Cert_periodE":cms.vdouble(
8.447554e+01,6.822833e+04,2.393459e+05,3.421711e+05,5.866281e+05,
7.535163e+05,8.411433e+05,6.881394e+05,8.125562e+05,2.559285e+06,
1.463891e+07,3.827981e+07,5.974146e+07,8.865731e+07,1.310953e+08,
1.721633e+08,1.943444e+08,2.005720e+08,2.015723e+08,2.017724e+08,
2.015965e+08,2.017669e+08,2.034083e+08,2.061524e+08,2.080316e+08,
2.070640e+08,2.023556e+08,1.941046e+08,1.828990e+08,1.691564e+08,
1.530922e+08,1.350455e+08,1.157011e+08,9.600941e+07,7.694766e+07,
5.935811e+07,4.389087e+07,3.097861e+07,2.079561e+07,1.324190e+07,
7.985476e+06,4.557658e+06,2.462167e+06,1.259846e+06,6.112363e+05,
2.815736e+05,1.233553e+05,5.148265e+04,2.050633e+04,7.809503e+03,
2.848456e+03,9.965424e+02,3.347979e+02,1.080863e+02,3.353724e+01,
9.997373e+00,2.860766e+00,7.849088e-01,2.062262e-01,5.182302e-02,
1.244225e-02,2.851855e-03,6.237188e-04,1.301323e-04,2.590152e-05,
4.919309e-06,8.916931e-07,1.542822e-07,2.553012e-08,4.049773e-09,
5.500813e-10,3.917666e-11,0.000000e+00,0.000000e+00,0.000000e+00,
),
#pileupCalc.py -i Cert_periodF.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 75 --numPileupBins 75 PileUpData.root 
"Cert_periodF":cms.vdouble(
1.327849e+03,6.474298e+04,2.157447e+05,2.072951e+05,1.733690e+05,
3.067059e+05,3.762002e+05,3.569894e+05,4.482360e+05,5.224305e+05,
5.820582e+05,8.820893e+05,2.500271e+06,1.099632e+07,3.657540e+07,
7.738787e+07,1.147136e+08,1.398158e+08,1.567663e+08,1.676603e+08,
1.734360e+08,1.786815e+08,1.852753e+08,1.914202e+08,1.956509e+08,
1.966963e+08,1.932943e+08,1.848757e+08,1.718832e+08,1.553376e+08,
1.363330e+08,1.159390e+08,9.528424e+07,7.553291e+07,5.772757e+07,
4.258726e+07,3.039817e+07,2.104814e+07,1.416313e+07,9.262493e+06,
5.877484e+06,3.607561e+06,2.133990e+06,1.212170e+06,6.591530e+05,
3.423034e+05,1.694577e+05,7.986792e+04,3.580400e+04,1.525616e+04,
6.176519e+03,2.375910e+03,8.688822e+02,3.025192e+02,1.005302e+02,
3.200756e+01,9.815002e+00,2.917469e+00,8.465593e-01,2.413794e-01,
6.795729e-02,1.893145e-02,5.214247e-03,1.415529e-03,3.771567e-04,
9.819833e-05,2.488924e-05,6.122257e-06,1.458245e-06,3.359647e-07,
7.458217e-08,1.602791e-08,3.281322e-09,6.338735e-10,1.360151e-10,
),
#pileupCalc.py -i Cert_periodG.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 75 --numPileupBins 75 PileUpData.root 
"Cert_periodG":cms.vdouble(
1.183863e+04,1.618221e+05,3.759272e+05,5.884100e+05,7.732389e+05,
1.069925e+06,1.093821e+06,1.235581e+06,1.494452e+06,3.170813e+06,
1.305357e+07,4.921048e+07,1.080663e+08,1.660827e+08,2.111456e+08,
2.608402e+08,3.085060e+08,3.395703e+08,3.522030e+08,3.574362e+08,
3.682331e+08,3.878519e+08,4.087183e+08,4.235393e+08,4.301041e+08,
4.286325e+08,4.204912e+08,4.067659e+08,3.866189e+08,3.581678e+08,
3.206573e+08,2.756432e+08,2.267288e+08,1.782992e+08,1.341707e+08,
9.679017e+07,6.709308e+07,4.480134e+07,2.889115e+07,1.803620e+07,
1.092465e+07,6.433584e+06,3.690208e+06,2.064174e+06,1.126618e+06,
5.998405e+05,3.112420e+05,1.571436e+05,7.705952e+04,3.663115e+04,
1.684969e+04,7.488534e+03,3.211996e+03,1.328660e+03,5.298761e+02,
2.037364e+02,7.554928e+01,2.703172e+01,9.337945e+00,3.116094e+00,
1.004976e+00,3.133410e-01,9.445707e-02,2.752645e-02,7.752069e-03,
2.108712e-03,5.537063e-04,1.402512e-04,3.424466e-05,8.054752e-06,
1.823908e-06,3.973871e-07,8.328650e-08,1.675451e-08,3.163133e-09,
),

#pileupCalc.py -i Cert_periodH.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 75 --numPileupBins 75 PileUpData.root 
"Cert_periodH":cms.vdouble(
2.234560e+05,3.827209e+05,8.523636e+05,7.372261e+05,9.913621e+05,
1.214641e+06,1.142144e+06,2.128320e+06,3.212411e+06,2.572986e+06,
1.205540e+07,4.156334e+07,7.988703e+07,1.266750e+08,1.900175e+08,
2.575034e+08,3.155103e+08,3.562758e+08,3.800335e+08,3.964937e+08,
4.216183e+08,4.517134e+08,4.650922e+08,4.542813e+08,4.326405e+08,
4.126800e+08,3.960083e+08,3.802456e+08,3.642831e+08,3.478920e+08,
3.307604e+08,3.123545e+08,2.920389e+08,2.693066e+08,2.440423e+08,
2.165747e+08,1.875464e+08,1.578090e+08,1.284217e+08,1.006072e+08,
7.557797e+07,5.428062e+07,3.719436e+07,2.428375e+07,1.509485e+07,
8.929702e+06,5.026546e+06,2.692382e+06,1.372516e+06,6.661460e+05,
3.080065e+05,1.358070e+05,5.719319e+04,2.306173e+04,8.936123e+03,
3.344725e+03,1.217643e+03,4.348645e+02,1.538696e+02,5.451178e+01,
1.954144e+01,7.161801e+00,2.709766e+00,1.067287e+00,4.396363e-01,
1.891714e-01,8.440960e-02,3.862310e-02,1.791038e-02,8.333252e-03,
3.861607e-03,1.773447e-03,8.046747e-04,3.600543e-04,1.587043e-04,
),
}