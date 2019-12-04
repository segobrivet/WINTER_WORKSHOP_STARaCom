import matplotlib.pyplot as plt
import numpy as np

def load_flower(m=400, dim=2):
    # input:
    # m = number of examples
    # dim = dimension of the data
    np.random.seed(3)  # for same reproducibility
    nc = int(m/2)  # nb of points for each class
    X = np.zeros((m,dim))
    Y = np.zeros((m,1), dtype='uint8') # labels: red = 0, blue = 1
    f = 4  # nb of diameters in the flower

    for j in range(2):
        ix = range(nc*j,nc*(j+1))
        t = np.linspace(j*3.12,(j+1)*3.12,nc) + np.random.randn(nc)*0.2 # theta
        r = f*np.sin(4*t) + np.random.randn(nc)*0.2 # radius
        X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
        Y[ix] = j
        
    return X, Y


def load_spiral(m=400, dim=2):
    # m = number of points per class
    # dim = dimensionality of the data
    np.random.seed(3)
    nc = int(m / 4)
    K = 4 # number of classes
    X = np.zeros((nc*K,dim)) # data matrix (each row = single example)
    y = np.zeros(nc*K, dtype='uint8') # class labels
    
    for j in range(K):
        ix = range(nc*j,nc*(j+1))
        r = np.linspace(0.0,1,nc) # radius
        t = np.linspace(j*5,(j+1)*5,nc) + np.random.randn(nc)*0.2 # theta

        X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
        y[ix] = j % 2
        
    return X, y


def plot_decision_boundary(model, X, y):
    # Author: Denny Britz
    # https://gist.github.com/dennybritz/ff8e7c2954dd47a4ce5f
    
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    h = 0.1
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[:, 0], X[:, 1], c=y.reshape(len(y)), cmap=plt.cm.Spectral)

