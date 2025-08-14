import matplotlib as mpl
import matplotlib.pyplot as plt


def linestyle_generator():
    """decide of the linestyle of the plots.

    Yields
    ------
    str
        appropriate linestyle for the plot
    """
    linestyles = ['-', '--', '-.', ':']
    line_ID = 0
    while True:
        yield linestyles[line_ID]
        line_ID += (line_ID + 1) % len(linestyles)


def linecolor_generator():
    linecolors = ['r--', 'b--', 'p--']
    line_ID = 0
    while True:
        yield linecolors[line_ID]
        line_ID += (line_ID + 1) % len(linecolors)


def plot_set(fig_ax: plt.Axes, *args: list) -> None:
    """setting the graph properties, but set parameter is as below.

    - xlabel
    - ylabel
    - grid. parameter of grid is ```ls=':'```.

    Parameters
    ----------
    fig_ax : plt.Axes
        instance of Axes.

    *args : list
        list of arguments.
        - args[0] : xlabel
        - args[1] : ylabel
        - args[2] : legend location.
    """
    mpl.rcParams['axes.xmargin'] = 0

    fig_ax.set_xlabel(args[0])
    fig_ax.set_ylabel(args[1])
    fig_ax.grid(ls=':')

    if len(args) == 3:
        fig_ax.legend(loc=args[2])


def bodeplot_set(fig_ax: plt.Axes, *args: list) -> None:
    """drawing the bode line diagram.

    Parameters
    ----------
    fig_ax : plt.Axes
        instance of Axes.

    *args : list
        list of arguments.
        - args[0] : Gain data.
        - args[1] : Phase and Frequency data.
    """
    mpl.rcParams['axes.xmargin'] = 0

    # embeding of x labels and grid properties.
    fig_ax[0].grid(which='both', ls=':', lw=0.5)
    fig_ax[0].set_ylabel('Gain [dB]')

    # embeding of x labels and y labels, grid properties.
    fig_ax[1].grid(which='major', ls=':', lw=1)
    fig_ax[1].set_xlabel('Frequency [Hz]')
    fig_ax[1].set_ylabel('Phase [deg]')

    # show legend.
    if len(args) > 0:
        fig_ax[0].legend(loc=args[0])

    if len(args) > 1:
        fig_ax[1].legend(loc=args[1])
