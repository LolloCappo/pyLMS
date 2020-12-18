import numpy as np
import scipy.io

def pyLMS(filename):
    '''
    Open acquisition .mat files saved from LMS Testlab
    '''
    mat = scipy.io.loadmat(filename)

    if list(mat.keys())[3] == 'Signal':
        domain = 'Time'
    elif list(mat.keys())[3] == 'PSD':
        domain =  'PSD'
    elif list(mat.keys())[3] == 'FRF':
        domain =  'FRF'
    elif list(mat.keys())[3] == 'FrequencySpectrum':
        if str(mat['FrequencySpectrum'][0][0][0][0][0][1][0]) == 'BandOctave1_3':
            domain =  'Octave'
        else:
            domain = 'Spectrum'


    

    ###########################
    if domain == 'Time':
        
        ty = 'Signal'
        x_mag = 'Time'
        
        x = np.ravel(mat[ty]['x_values'])
        x_start = x[0][0][0][0][0][0]
        x_step = x[0][0][0][1][0][0]
        x_numbers = x[0][0][0][2][0][0]
        x_unit = x[0][0][0][3][0][0][0][0]
        x_vect = np.linspace(x_start, x_numbers * x_step, x_numbers)
        
        y = np.ravel(mat[ty]['y_values'])
        y_unit = y[0][0][0][1][0][0][0][0]
        y_conversion = y[0][0][0][1][0][0][1][0][0][1][0][0]
        y_vect = np.ravel(y[0][0][0][0]) * y_conversion 
        z = np.ravel(mat[ty]['function_record'])[0][0][0][0][0]
        
        if y_unit == 'g':
            y_mag = 'Acceleration'
        elif y_unit == 'N':
            y_mag = 'Force'
        elif y_unit == 'Pa':
            y_mag = 'Pressure'
        else:
            y_unit = 'Amplitude'
            
    elif domain == 'PSD':
        
        ty = 'PSD'
        x_mag = 'Frequency'
        
        x = np.ravel(mat[ty]['x_values'])
        x_start = x[0][0][0][0][0][0]
        x_step = x[0][0][0][1][0][0]
        x_numbers = x[0][0][0][2][0][0]
        x_unit = x[0][0][0][3][0][0][0][0]
        x_vect = np.linspace(x_start, x_numbers * x_step, x_numbers)
        
        y = np.ravel(mat[ty]['y_values'])
        y_unit = y[0][0][0][1][0][0][0][0]
        y_conversion = y[0][0][0][1][0][0][1][0][0][1][0][0]
        y_vect = np.ravel(y[0][0][0][0]) * y_conversion 
        z = np.ravel(mat[ty]['function_record'])[0][0][0][0][0]
        
        y_mag = 'Power Spectral Density'

    elif domain == 'FRF':
        
        ty = 'FRF'
        x_mag = 'Frequency'
        y_mag = 'Frequency Response Function'
        
        x = np.ravel(mat[ty]['x_values'])
        x_start = x[0][0][0][0][0][0]
        x_step = x[0][0][0][1][0][0]
        x_numbers = x[0][0][0][2][0][0]
        x_unit = x[0][0][0][3][0][0][0][0]
        x_vect = np.linspace(x_start, x_numbers * x_step, x_numbers)
        
        y = np.ravel(mat[ty]['y_values'])
        y_unit = y[0][0][0][1][0][0][0][0]
        y_conversion = y[0][0][0][1][0][0][1][0][0][1][0][0]
        y_vect = np.ravel(y[0][0][0][0]) * y_conversion 
        z = np.ravel(mat[ty]['function_record'])[0][0][0][0][0]

    elif domain == 'Spectrum':
        
        ty  = 'FrequencySpectrum'  
        x_mag = 'Frequency'
        y_mag = 'Amplitude'
        
        x = np.ravel(mat[ty]['x_values'])
        x_start = x[0][0][0][0][0][0]
        x_step = x[0][0][0][1][0][0]
        x_numbers = x[0][0][0][2][0][0]
        x_unit = x[0][0][0][3][0][0][0][0]
        x_vect = np.linspace(x_start, x_numbers * x_step, x_numbers)
        
        y = np.ravel(mat[ty]['y_values'])
        y_unit = y[0][0][0][1][0][0][0][0]
        y_conversion = y[0][0][0][1][0][0][1][0][0][1][0][0]
        y_vect = np.ravel(y[0][0][0][0]) * y_conversion 
        z = np.ravel(mat[ty]['function_record'])[0][0][0][0][0]
        
        
    elif domain == 'Octave':
        
        ty  = 'FrequencySpectrum'   
        x_mag = 'Frequency'
        y_mag = 'Amplitude'
        
        fcentre = np.round(10**(np.arange(1,50,1) * 0.1),5)
        
        x = np.ravel(mat[ty]['x_values'])
        x_start = np.round(x[0][0][0][0][0][0],5)
        x_numbers = x[0][0][0][2][0][0]
        x_unit = x[0][0][0][1][0]
        index = np.where(fcentre==x_start)[0][0]
        x_vect = np.take(fcentre,np.arange(index,index + x_numbers))
        
        y = np.ravel(mat[ty]['y_values'])
        y_unit = y[0][0][0][1][0][0][0][0]
        y_conversion = y[0][0][0][1][0][0][1][0][0][1][0][0]
        y_vect = np.ravel(y[0][0][0][0]) * y_conversion 
        
        z = np.ravel(mat[ty]['function_record'])[0][0][0][0][0]
        

    if type(z) == str:

        y_mag = y_mag + z                
        
    data = {'x' : x_vect, 'y' : y_vect}
    units = {'x' : x_unit, 'y' : y_unit}
    magnitudes = {'x' : x_mag, 'y' : y_mag}

    out = {'signals': data, 'units': units,'magnitudes': magnitudes}
    
    return  out