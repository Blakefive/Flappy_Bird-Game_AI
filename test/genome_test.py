import numpy as np
import tensorflow.keras.backend as K
import tensorflow as tf

class Genome():
  def __init__(self):
    self.fitness = 0
    self.score = 0
    self.w1 = np.array([[ 0.850624  ,  1.10490762, -1.44621053, -0.06239848, -0.30222242,
         1.12278345,  1.35300776, -0.37815641, -0.72169242, -1.21901921],
       [-0.03310376,  0.01429568,  0.89703475,  2.02197199, -1.18468878,
         0.4250798 , -1.50062584,  0.61295983, -0.86696233, -0.21584511],
       [ 0.14540825,  1.16028733, -0.31088923, -0.12714827, -0.87261542,
         0.06592747, -0.41949712, -0.18295315,  0.1367479 ,  1.090919  ]])
    self.w2 = np.array([[-2.12695425, -1.53544276, -0.79980267, -1.57045729, -0.40620545,
         0.16146434, -2.19333134, -1.16360906,  0.89186703,  0.74921277,
        -0.74601689, -1.2614486 ,  0.66513939, -0.0888794 ,  0.35915796],
       [-1.5863136 , -0.25381348, -0.2498434 ,  0.04712139,  1.30056136,
         0.17093201, -0.58716073,  0.26214786, -1.43587007, -0.65737006,
        -0.8716598 ,  1.09213864,  0.15605281, -1.2440056 , -0.66398285],
       [-0.72664256, -0.1940464 , -3.24729798, -1.46121478,  0.40956506,
        -0.61046142,  0.58908755, -0.82212605, -1.53891265,  0.85331211,
        -0.70713577,  0.15950308,  0.03943419, -2.34752302,  0.30893894],
       [ 0.88269683, -1.0936827 , -0.67468445, -1.07512502,  3.06578239,
         0.16722675, -0.54208394, -0.16361497,  0.48170666,  2.04026083,
         0.32940044, -0.12212939, -0.40617475, -0.44356492, -1.57555956],
       [-1.56606039,  0.62634187,  0.01514943, -1.04127888, -0.92179835,
         0.11778595,  0.82962161,  1.05919627, -0.65234619,  2.55364734,
        -1.07632608,  0.2564001 , -0.55685676, -1.00934993,  0.6107165 ],
       [-1.44500213,  0.09480337,  0.67387247,  2.46730477,  1.21796887,
         0.36487743, -0.26091115,  0.58365405, -0.14091037,  0.52940823,
        -2.29236894, -1.21269257,  0.37868954, -1.16452405,  0.27250774],
       [-0.15785961, -0.40316011, -0.11625284, -0.07727121, -1.29268208,
         0.06816179, -1.00035063,  1.01380475,  0.59625243,  0.95096313,
        -1.87275617,  0.22899944,  0.34133278,  0.13167134,  0.34483589],
       [ 1.74710715, -1.27231373, -1.17904751, -0.6356543 ,  0.4403152 ,
         0.03926364,  0.05506448, -0.95033066, -0.27395024, -0.32616897,
        -0.76992701,  0.17333735, -0.93444053,  0.94373057,  0.45630268],
       [ 1.50591715, -0.24555868, -1.00040577, -0.66352845,  0.08290547,
         0.14530991,  0.49390881, -0.49678108, -0.4563849 ,  0.81107468,
         0.9239215 , -0.34225227, -1.18997746, -0.88135723,  0.91696565],
       [-0.25009975,  2.71208788, -0.56150995, -0.07421162, -0.59133396,
        -0.98232773,  0.88386211, -1.60126866, -2.41658916, -0.011642  ,
        -2.43063768, -0.09581238, -0.84345563,  1.50716226,  0.32238147]])
    self.w3 = np.array([[-1.66007976e+00,  2.46657364e-01,  9.17784609e-01,
        -3.54179209e-01, -2.54494989e-01,  9.15576394e-03,
        -3.39673305e-01,  2.18874698e-01,  2.56997124e-02,
         1.15328968e+00, -5.53745676e-01, -1.27807304e+00,
         3.47941799e-01,  1.06711528e+00, -1.35230797e+00,
         4.20828318e-01, -1.27614996e-01,  1.24976563e+00,
         7.34824501e-01, -7.76818529e-01],
       [ 7.71292735e-01, -7.61451123e-01,  3.51315361e-01,
        -1.61136389e-01, -1.35506910e+00, -1.50567278e-01,
        -1.80935328e+00,  4.72763926e-01, -1.17904446e+00,
        -2.81800034e-01, -1.46769891e+00,  3.60851222e-01,
        -3.57683734e-01,  5.32423779e-01,  1.95445750e-01,
         9.40865914e-01,  2.13920130e-01, -4.53479021e-01,
         1.17770890e+00,  1.26192641e-01],
       [-1.27107035e+00, -1.67071585e+00, -1.73663897e+00,
        -9.69790327e-01, -7.96211875e-01,  5.82460872e-01,
         2.62898970e+00,  1.21880732e+00, -1.84656552e-01,
         3.72335604e-01, -2.38816937e+00,  2.24075650e-02,
        -1.26194431e+00,  1.84911056e+00,  3.51123836e-01,
         4.62421794e-01,  6.18488074e-01,  4.42155215e-01,
        -2.54295101e-01,  1.64549423e-01],
       [-1.72639363e-02,  9.94791511e-01, -1.41265475e+00,
        -5.73249872e-01, -1.01725592e-01,  9.25523075e-01,
        -1.28654290e+00, -2.46707149e-01, -1.02559311e-02,
        -3.49785721e-01, -3.92191074e-01,  1.22488861e+00,
        -4.17112945e-01,  5.32975911e-01,  9.96358252e-02,
        -7.95553220e-01,  5.16767013e-01, -2.66470312e+00,
         8.89750854e-01, -9.03246227e-01],
       [-3.12799847e-01,  7.24441386e-01, -5.81067488e-01,
         1.26203122e+00,  1.01479986e+00,  9.02554870e-01,
        -1.42165452e+00, -3.72905486e-01, -1.19705160e+00,
         2.06170994e-01,  8.35753124e-01, -2.90639823e-01,
         5.05071828e-01, -4.43277440e-01, -1.78781640e+00,
         9.21694352e-01, -7.44882203e-01,  2.23504009e+00,
         3.27274724e-01, -7.58068366e-02],
       [-1.14644806e+00, -8.99596729e-01,  1.37050052e-02,
        -1.31596586e-01,  2.01502344e-01,  1.82167582e+00,
         8.33455843e-01, -3.25972528e-01,  4.41256462e-01,
        -1.31393177e-01,  1.42242536e+00,  3.96568276e+00,
         1.48876359e+00, -4.53079686e-01, -1.70445826e+00,
         8.45433174e-02,  2.94800483e-01, -1.46001835e-01,
        -1.95201803e+00, -2.58172226e-01],
       [ 1.52924532e-01, -7.09633765e-01, -4.55714085e-01,
        -2.66420894e-01,  6.51054424e-01, -1.69564584e-01,
         1.29197082e+00, -3.11476051e-01, -2.84835847e-01,
        -3.42177123e-02,  1.38281464e+00, -3.43106168e-01,
         1.52648737e-01,  1.98943859e-01,  1.56509572e+00,
         1.13545002e-01, -1.76347087e+00, -1.21970197e+00,
        -5.34792956e-01, -9.65861339e-01],
       [-5.06541473e-01,  8.07843336e-01,  7.27440408e-01,
         3.10469658e+00,  3.60789734e-01,  7.69733483e-01,
        -1.28550137e-01,  1.94043366e+00, -2.70754631e-01,
         9.70009021e-02, -3.80329953e-01,  3.90080299e-02,
        -1.25056633e+00,  6.33012600e-01,  8.71213548e-01,
         1.97552212e-02,  1.69612417e-02,  9.92926903e-01,
         8.68762619e-01, -1.48050199e-01],
       [-1.22780285e-01,  1.39658078e+00, -4.20910202e-01,
        -9.86435700e-01,  1.06630091e+00,  3.62758366e-01,
        -2.79334097e-01,  2.81758301e-01, -4.85267017e-01,
         8.42777128e-01, -5.55745957e-01,  1.22044758e+00,
        -2.59181441e-01,  5.10402825e-01,  1.35065812e+00,
        -4.57118245e-01,  9.58073851e-01,  7.96488674e-01,
        -3.68618619e-02, -5.64503326e-01],
       [ 1.92455750e+00,  7.64215311e-01,  1.01709018e+00,
        -2.06547220e+00, -1.11074053e+00, -7.15039747e-02,
         4.95787485e-01, -6.34729172e-02,  3.31946671e-01,
        -2.30709820e+00,  1.13090433e+00, -1.14761553e+00,
        -1.59912931e-02, -1.79572170e+00,  3.38548372e-01,
         1.41371217e+00, -3.06867391e-01, -1.89713544e-01,
         1.89956742e-01, -4.38616319e-01],
       [ 1.91357587e+00, -1.57636518e+00,  1.00918486e+00,
         1.92594945e+00,  3.77425588e-01, -3.10245264e-01,
         7.83070948e-01,  8.89833684e-01,  9.67857778e-01,
        -8.60918681e-01,  2.13569343e+00, -1.39153690e+00,
         2.39087897e-03, -2.15965573e-01,  2.30812418e-01,
        -3.06858762e-01,  4.11306742e-01, -5.47473394e-02,
         7.78141189e-01,  5.29792969e-01],
       [ 7.99806965e-02, -1.18986852e+00, -1.88835472e-01,
        -1.91875537e-01, -7.71484736e-01,  3.46320520e-01,
         3.63249817e+00,  1.19797201e+00,  5.48574674e-01,
         3.60484896e-01, -1.92862860e+00, -1.31680556e+00,
         1.24864183e+00,  1.31444165e+00, -3.71580085e-01,
         5.49443321e-01,  9.42866473e-02, -1.16442694e+00,
         1.25869112e+00,  1.71396000e+00],
       [-1.99872107e-01,  5.16483198e-01, -3.54447821e-01,
        -6.05329144e-02, -2.52430380e-01, -5.01726786e-01,
        -3.66208559e-01,  6.86692178e-01, -2.52262712e+00,
        -1.35067632e+00,  7.17410343e-01, -5.79928177e-02,
        -9.63114516e-01, -1.92099947e-01, -8.49791051e-02,
        -2.22100328e-01,  5.65074530e-01, -2.09183773e-01,
         1.27440224e+00,  2.02204389e+00],
       [-5.04259171e-01,  5.02983098e-01,  7.55224404e-01,
        -4.60750649e-01, -8.95964239e-01, -4.52123553e-01,
        -1.25929412e+00,  1.99148699e-01, -2.65456896e-01,
        -1.18887845e+00, -6.42511960e-01, -2.95571523e-01,
        -2.57786898e-01, -2.91113462e-01, -1.84335077e+00,
         1.58784862e+00,  3.62705185e-01, -1.72533134e+00,
         2.71162534e-01, -6.10139809e-01],
       [-5.81814338e-02, -6.06485254e-02, -5.59314517e-01,
        -2.83932048e+00, -1.24005486e+00, -1.31220052e+00,
         5.59272998e-01,  1.34598368e+00,  1.07950996e+00,
         7.14435603e-01,  8.88007261e-01,  6.08721877e-01,
        -3.43455490e-01, -7.83452845e-02,  6.78622467e-01,
        -4.84003259e-01, -4.33225249e-02,  5.98048905e-01,
         3.10862093e-01,  1.67170488e+00]])
    self.w4 = np.array([[-3.53656097e-01,  2.10541588e+00,  1.50213486e+00,
         2.72689001e-01,  2.65024609e+00, -7.39727144e-01,
         2.55833267e-01, -8.55768287e-02,  1.81853707e+00,
         8.00860447e-01],
       [-1.83539523e+00, -8.68059488e-01,  5.59661445e-02,
        -8.45069964e-01, -1.89907007e-01, -9.90630501e-01,
        -1.68768571e+00, -1.01758536e-01,  2.74873999e-02,
         7.30427388e-01],
       [-9.05813614e-01,  1.75674687e+00, -9.72177042e-02,
         1.29524077e+00,  1.17833128e+00,  1.13216225e+00,
        -2.56562526e-01,  5.46653618e-02,  2.78137186e-02,
        -8.35715363e-01],
       [ 2.75774585e-01, -6.72406549e-01, -2.67250403e+00,
         4.97791434e-01, -9.65195243e-01, -1.01300696e+00,
        -7.23750233e-01, -6.38497998e-02,  2.98273233e-01,
         2.39658524e+00],
       [-1.50217937e-01, -1.62742351e-01,  7.33856875e-01,
         2.54470275e-01, -1.01229976e+00, -2.53399427e-01,
         2.75210868e-01,  4.44426041e-01,  1.58176894e+00,
        -6.80794007e-01],
       [ 3.08314086e-01,  4.16464626e-01,  6.05854076e-01,
        -2.88132112e-01, -8.91500735e-01, -1.44970180e-01,
         1.04104628e-02,  6.74074396e-01, -1.98289292e-01,
         2.70343391e-01],
       [-2.26958435e-03, -1.44849875e+00,  2.90634396e+00,
         6.94886679e-02,  1.05361798e-01,  6.50123400e-01,
        -1.14245989e+00,  3.35284946e-01, -9.50577156e-01,
         1.28202089e-01],
       [ 1.54438419e+00, -9.88573500e-01,  2.52759603e+00,
         2.91320095e-01, -2.83148262e-02,  6.24109182e-01,
        -7.85903574e-02,  1.39385606e-01,  5.65614332e-01,
         6.44790223e-01],
       [-7.42194048e-02,  1.52641773e-01, -3.25636053e-01,
        -2.40742320e-01,  8.12633588e-03, -6.41178976e-02,
        -3.09346888e-01, -1.04624722e+00,  1.62539199e+00,
         5.79818338e-01],
       [ 2.85946110e-01, -1.00441850e+00, -8.32260140e-01,
        -6.46495398e-01, -1.60116541e-02, -1.96859899e-01,
         7.14947806e-01,  1.09664831e+00,  5.53082806e-01,
         5.31935256e-01],
       [ 3.40008729e-01, -2.45603897e-01, -2.40471878e+00,
        -6.00314731e-01, -2.88769028e+00, -1.51760012e+00,
        -1.39184730e-01, -9.63774838e-01, -2.75641644e-04,
         2.44830719e-01],
       [-1.38783864e+00,  7.01527981e-01,  5.75558828e-01,
         8.31193240e-04,  2.11865731e-01,  6.67188351e-01,
        -6.23887432e-02,  1.66454595e+00,  1.12661265e-01,
        -5.35455083e-02],
       [ 3.68000252e+00, -3.92469240e-01,  1.23809944e+00,
         2.26829969e+00, -5.37543562e-02, -6.33259647e-01,
         5.33763383e-01,  1.46923675e+00,  6.22216676e-01,
        -5.20067257e-01],
       [-3.67723380e-01,  2.75569683e+00, -5.01207086e-01,
        -9.83943898e-03,  7.94541734e-01,  8.01748994e-02,
        -9.90909692e-01, -8.25756274e-01, -5.28978080e-02,
         2.03084870e-01],
       [-9.22785038e-01, -1.11649876e-01,  1.74077901e+00,
         7.75057087e-01,  3.42216385e-01,  7.94898738e-02,
         5.22022848e-01,  7.01784445e-01, -3.22592071e-01,
        -7.89119483e-01],
       [-2.75524043e-01,  1.08511148e-01,  4.16327688e-01,
         4.29142711e-01,  8.93557287e-01,  1.34842793e-01,
        -2.10507234e+00, -2.66162340e-01, -6.96138419e-01,
         1.53970404e+00],
       [-8.70250235e-01,  1.21432915e+00, -1.29736083e+00,
         3.36031822e-01,  1.05107204e-01, -2.11796468e-02,
         4.21416553e-01, -2.28400907e-01,  8.47922752e-01,
        -6.59790223e-01],
       [-8.55936644e-01,  2.95043243e-01, -3.30638801e+00,
        -1.06576192e+00,  4.91400967e-01,  7.27362705e-01,
        -1.77685092e+00,  8.78819935e-01,  1.68557435e+00,
         1.42388679e+00],
       [ 9.57758075e-01,  1.24434910e+00, -5.00333127e-01,
         1.22512041e+00,  4.42984710e-01,  2.96217398e-01,
        -1.54859676e-01, -5.47757425e-02,  8.50226351e-01,
         4.80233848e-01],
       [-1.11366634e-01,  4.16425009e-01,  3.85076879e-01,
         1.18050503e+00, -3.24237372e+00, -8.78695219e-01,
        -5.25201000e-01,  4.08215230e-01,  6.91264999e-01,
         1.59811487e-01]])
    self.w5 = np.array([[-1.57106039],
       [ 0.37260607],
       [ 0.02917013],
       [-0.2034953 ],
       [-0.01521371],
       [ 0.49398483],
       [ 0.49541441],
       [ 0.03833633],
       [ 0.58262463],
       [ 1.09890658]])

    self.b1 = np.array([-0.31647271,  1.22481041,  1.41395356, -0.92055122,  0.08423259,
       -0.2569094 , -0.30820666, -0.70752495,  0.35060047, -0.81106544])
    self.b2 = np.array([ 0.44284555, -0.4474263 , -1.04607378, -0.27269892, -0.38887388,
       -1.13672855,  0.2781687 , -0.33024842, -0.08446518, -0.92369218,
       -0.47345037,  0.03242487, -0.82840539, -0.61001679,  0.58007355])
    self.b3 = np.array([ 0.94463526, -3.27790412,  2.89582372, -0.24040493,  0.03757196,
        0.42891921, -0.92156633, -0.18467067, -0.1511283 , -0.47858354,
        1.318696  , -0.34457722,  0.50954805,  0.84842122,  2.14907828,
       -0.67260136, -1.08732416,  1.51371509, -0.16757593, -0.35813928])
    self.b4 = np.array([-0.58152813, -0.46926972, -0.2261627 , -0.62277004, -0.12866269,
       -0.44951433, -0.86879674,  0.73135041,  0.39936213,  0.41741063])
    self.b5 = np.array([0.50470538])
    
  def forward(self, inputs):
    net = np.matmul(inputs, self.w1) + self.b1
    net = tf.keras.activations.relu(net)
    
    net = np.matmul(net, self.w2) + self.b2
    net = tf.keras.activations.sigmoid(net)

    net = np.matmul(net, self.w3) + self.b3
    tf.keras.activations.selu(net)

    net = np.matmul(net, self.w4) + self.b4
    net = tf.keras.activations.elu(net, alpha=1.5)

    net = np.matmul(net, self.w5) + self.b5
    net = tf.keras.activations.sigmoid(net)
    
    return self.step_function(net)

  def step_function(self, x):
    return np.array(x>0.5, dtype=np.int64)

