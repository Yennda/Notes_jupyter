import matplotlib

yellow = '#ffb200'
red = '#DD5544'
blue = '#0284C0'
black = '#000000'    
green = '#008000'
gray = '#555555'
purple = '#DD84C0'

COLORS = [yellow, red, blue, black, green, gray, purple]

def matplotlib_fonts():
    matplotlib.rc('font', family='serif') 
    matplotlib.rc('font', serif='Palatino Linotype') 
    matplotlib.rc('text', usetex='false') 
    matplotlib.rcParams.update({'font.size': 24})

    matplotlib.rcParams['mathtext.fontset'] = 'custom'
    matplotlib.rcParams['mathtext.rm'] = 'Palatino Linotype'
    matplotlib.rcParams['mathtext.it'] = 'Palatino Linotype:italic'
    matplotlib.rcParams['mathtext.bf'] = 'BiPalatino Linotype:bold'