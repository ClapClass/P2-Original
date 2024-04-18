import numpy as np
from matplotlib import pyplot as plt
from kafe2 import HistContainer, HistFit, Plot
from scipy import special



########################################################################################################################################
# TABLE OF CONTENTS #
#####################
#
# - Gaussian model function for photopeaks
# - Model function for compton edges using the complementary error function 'erfc' (Convolution of Gaussian and Heaviside-Step-Function) with a quadratic form correction factor 
# - Fit a photopeak using a Gaussian model function
# - Fit a compton edge using a complementary error function
# - Custom wrapper for fitting a custom function to a histogram using Kafe2, combining all relevant steps
#
########################################################################################################################################



##########################################
# Gaussian model function for photopeaks #
##########################################

def gaussian (x, mu, sigma = 10, baseline = 0, A = 100):
    return  A * np.exp(-(x - mu)**2 / (2 * (sigma**2))) + baseline



################################################################################################################################################################################
# Model function for compton edges using the complementary error function 'erfc' (Convolution of Gaussian and Heaviside-Step-Function) with a quadratic form correction factor #
################################################################################################################################################################################

def compton_edge (x, mu, sigma = 10, baseline = 0, A = 100, B = 1):
    return A * special.erfc((x-mu)/(np.sqrt(2) * sigma)) * (1 + B * (x/mu - 0.5)**2) + baseline



###################################################
# Fit a photopeak using a Gaussian model function #
###################################################

def fit_peak (datax, datay, x1 = None, x2 = None, baseline = 0, showResult = True, label = None, **initparams):
    # Check if a lower x-limit for the fit is given, otherwise use the minimum of the provided dataset
    if x1 == None:
        x1 = min(datax)
    # Check if an upper x-limit for the fit is given, otherwise use the maximum of the provided dataset
    if x2 == None:
        x2 = max(datax)
    # Remove datapoints outside the specified fit range
    datax_clipped = np.delete(datax, np.where((x1 > datax) | (datax > x2)))
    datay_clipped = np.delete(datay, np.where((x1 > datax) | (datax > x2)))
    # Set axis labels
    axislabels = ['Channel', 'Count']
    # Set model LaTeX expression
    modelexpression = 'A \\cdot e^{{\\frac{{-(x-\\mu)^2}}{{2 \\sigma^2}}}} + \\mathrm{{baseline}}'
    # Perform a Gaussian fit on the remaining data, choosing the position of the maximum value in the data as an initial value for the position of the peak and it's value for the height of the peak
    fit = hist_fit_data(datax_clipped, datay_clipped, model = gaussian, limitedparams = ['mu', 'sigma'], fixedparams = [["baseline", baseline]], mu = datax_clipped[np.argmax(datay_clipped)], A = np.max(datay_clipped), label = label, showResult = showResult, axislabels = axislabels, modelexpression = modelexpression, **initparams)
    # Return fit object
    return fit



###########################################################
# Fit a compton edge using a complementary error function #
# ##########################################################

def fit_compton (datax, datay, x1 = None, x2 = None, baseline = 0, showResult = True, label = None, **initparams):
    # Check if a lower x-limit for the fit is given, otherwise use the minimum of the provided dataset
    if x1 == None:
        x1 = min(datax)
    # Check if an upper x-limit for the fit is given, otherwise use the maximum of the provided dataset
    if x2 == None:
        x2 = max(datax)
    # Remove datapoints outside the specified fit range
    datax_clipped = np.delete(datax, np.where((x1 > datax) | (datax > x2)))
    datay_clipped = np.delete(datay, np.where((x1 > datax) | (datax > x2)))
    # Determine an initial value for the position of the compton edge by estimating where the slope is maximal
    dif = np.diff(datay_clipped)
    diffs = []
    for i in range(len(datay_clipped-25)):
        diffs.append(np.abs(np.sum(dif[i:i+25])))
    mu0 = datax_clipped[np.argmax(diffs)]
    # Set axis labels
    axislabels = ['Channel', 'Count']
    # Set model LaTeX expression
    modelexpression = 'A \\cdot \\mathrm{{erfc}}(\\frac{{x-mu}}{{\\sqrt{{2}} \\sigma}}) \\cdot (1 + B (\\frac{{x}}{{mu}} - \\frac{{1}}{{2}})^2) + \\mathrm{{baseline}}'
    # Perform the fit on the remaining data using the estimated position as an initial value
    fit = hist_fit_data(datax_clipped, datay_clipped, model = compton_edge, limitedparams = ['mu', 'sigma', 'B'], fixedparams = [["baseline", baseline]], mu = mu0, A = np.max(datay_clipped), label = label, axislabels = axislabels, modelexpression = modelexpression, showResult = showResult, **initparams)
    # Return fit object
    return fit



#########################################################################################################
# Custom wrapper for fitting a custom function to a histogram using Kafe2, combining all relevant steps #
# ########################################################################################################

def hist_fit_data (x, y, model = None, label = 'data', constraints = [], fixedparams = [], limitedparams = [], parameternames = None, modellabel = None, modelname = None, axislabels = [None, None], modelexpression = None, report = False, showResult = False, **initialvalues):
    # Organise data histogram container
    step = x[1]-x[0]
    data = HistContainer(bin_edges = np.arange(x[0]-0.5*step, x[-1]+step, step = step))
    data.set_bins(y)
    data.label = label  
    data.axis_labels = axislabels
    # Assign data and model to fit
    fit = HistFit(data, model_function = model, density = False)  
    # Assign parameter constraints and set as initial values
    for a in constraints:
        fit.add_parameter_constraint(name = a[0], value = a[1], uncertainty = a[2])
        fit.set_parameter_values(**{a[0]:a[1]})  
    # Assign fixed parameter values (Causes errors concerning non-positive uncertainties)
    for b in fixedparams:
        fit.fix_parameter(name = b[0], value = b[1])   
    # Assign additional initial values
    fit.set_parameter_values(**initialvalues)
    # Limit parameters to be either zero or positive, not negative
    for a in limitedparams:
        fit.limit_parameter(a, lower = 0)
    #Assign parameter names as well as model label, name and expression
    if parameternames != None:
        fit.assign_parameter_latex_names(**parameternames)
    if modellabel != None:
        fit.model_label = modellabel
    if modelname != None:
        fit.assign_model_function_latex_name(modelname)
    if modelexpression != None:
        fit.assign_model_function_latex_expression(modelexpression)
    # Perform fit
    fit.do_fit()  
    # Plot fit results if desired
    if showResult:
        p = Plot(fit)
        p.plot()
        plt.show()
    # Report fit results if desired
    if report:
        fit.report()
    # Return fit
    return fit