import numpy as np
from scipy import constants as c
import math as m
from scipy.interpolate import interp1d



class Permeability():
    def __init__(self):
        f= open('gold_pcgrate.txt', 'r')
        contents=f.readlines()

        self.wavelength=[]
        self.epsilon=[]
        self.real=[]
        self.imag=[]

        for line in contents[:-1]:
            line_split=line.split('\t')
            if 0.3<float(line_split[0])<1.5:
                self.wavelength.append(float(line_split[0])/1e6)
                
                eps=(float(line_split[1])+1j*float(line_split[2]))**2
                self.epsilon.append(eps)
                self.real.append(np.real(eps))
                self.imag.append(np.imag(eps))
        
        k=3
        self.sreal=interp1d(self.wavelength, self.real, kind='linear')
        self.simag=interp1d(self.wavelength, self.imag, kind='linear')

    def eps(self, lm):
        return (self.sreal(lm)+1j*self.simag(lm)).conjugate()

def betavector(lm, epd, epm):
    k0=2*m.pi/lm
    epp=epd*epm/(epd+epm)
    beta=k0*(epp**0.5)
    return beta

def prism_angle(alfa_in):
    # input in radians
    # input: angle of incidence on the golden surface
    # output: angle of incidence on the prism
    alfa_4=alfa_in
    theta=62/180*m.pi
    n1=1       #air
    n2=1.51    #prism
    n3=1.51    #glass slide
#     alfa_out=m.asin(n2/n1*m.sin(m.asin(n3/n2*m.sin(alfa_4))-theta))
    alfa_out=m.asin(n2/n1*m.sin(theta-alfa_in))
    return alfa_out/m.pi*180

def setup_angle(alfa_in):
    theta=62
    return theta-prism_angle(alfa_in)
#     return prism_angle(alfa_in)+90-theta

    
def spr_info(lm, p=False):
    
    Theta=62/180*m.pi
    k0=2*m.pi/lm
#     epd=1.333**2 #water
#     epd=1 #air

    epm=metal.eps(lm)
    epm=epm.conjugate()
    epp=epd*epm/(epd+epm)
    na=1
    npr=1.51
    n_slide=1.51
    
    beta=betavector(lm)
    
    
    kz=(beta**2-epd*(k0)**2)**0.5
    alfa_in=m.asin(np.real(beta)/k0/n_slide)
    alfa1=prism_angle(alfa_in)
    alfa=setup_angle(alfa_in)
    

    if p:
        print(lm*1e9)
        print(beta)
        
        print('n = {:.3f}'.format(beta/k0))

        print('lambda_p= {:.3f}'.format(2*m.pi/beta.real*1e9))
        print('L= {:.3f} um'.format(1/(2*beta.imag)*1e6))
        print('z= {:.3f} um'.format(1/kz.real*1e6))
        print('alfa_1= {:.3f} °'.format(alfa1)) #uhel ke kolmici dopadu
        print('alfa= {:.3f} °'.format(alfa)) #uhel k ose setupu

        print('alfa_in= {:.3f} °'.format(alfa_in/m.pi*180)) #uhel dopadu uvnitr krystalu
#     return alfa1/m.pi*180, (Theta+m.asin(na/npr*m.sin(alfa1)))/m.pi*180
    return prism_angle(m.asin(np.real(beta)/k0/n_slide)), setup_angle(m.asin(np.real(beta)/k0/n_slide)), alfa_in/m.pi*180
#     return (Theta+alfa1)/m.pi*180, (Theta+m.asin(na/npr*m.sin(alfa1)))/m.pi*180