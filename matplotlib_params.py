import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# to ignore deprecation warnings
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


# store original plot parameters so that we can revert:
ORIG_CONFIG = dict(matplotlib.rcParams)


def set_my_params(style='seaborn', fontsize=18, lw=2, alw=2, font='serif', figsize=(10,10)):
    """
    set the rc parameters of the matplotlib based on 
    our default configuration    
    """
    # lets build it on top of existing style
    plt.style.use(style)
    
    figw, figh = figsize
    params = {
          'axes.labelsize' : fontsize,
          'axes.titlesize' : fontsize,
          'font.size': fontsize,
          'legend.fontsize' : fontsize,
          'xtick.labelsize' : fontsize,
          'ytick.labelsize' : fontsize,
          'axes.linewidth' : alw,
          'lines.linewidth' : lw,
          'figure.figsize' : [figw, figh],
          'font.family' : font,
          'savefig.bbox' : 'tight',
          'savefig.dpi' : 300  # set to 600 for poster printing or PR
                                  # figures
    }
    
    matplotlib.rcParams.update(params)


def revert_params():
    """
    reverts any changes done to matplotlib parameters and restores
    the state before homogenize_plot was called
    """

    matplotlib.rcParams.update(ORIG_CONFIG)

    
def plot_dummy(ax=None):
    '''
    plot dummy plot
    '''
    # create data
    x = np.linspace(1,5, 100)
    y = np.linspace(1,5, 50)
    yy, xx = np.meshgrid(x,y)
    z = np.sin(xx)**10 + np.cos(10 + yy*xx) * np.cos(xx)
    # plot these
    ax = ax or plt.gca()
    ax.imshow(z);
    ax.plot(np.linspace(20,80,50), np.linspace(10,40,50))
    ax.plot(np.linspace(20,80,50), np.linspace(40,10,50))
    ax.plot(np.linspace(20,80,50), np.repeat(25,50))
    markers = iter(['o','3','X','+','^'])
    for i in range(5):
        xr = np.random.uniform(10,90,40)
        yr = np.random.uniform(10,40,40)
        ax.scatter(xr,yr, s=np.random.randint(20,70,40), marker=next(markers))