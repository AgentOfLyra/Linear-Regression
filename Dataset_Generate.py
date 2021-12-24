#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import matplotlib.pyplot


# In[7]:


class Dataset_Generate(object):
    """
    input:scope, k
    Scope is the number of train samples in the dataset.
    Parameter "k" is the slope of target function.
    Parameter "b" is the intercept of the taget function.
    """
    def __init__(self, scope, k, b):
        self.k = k
        self.b = b
        self.scope = scope
        x = numpy.linspace(0, 1, num=self.scope)
        x = numpy.expand_dims(x, axis=1)
        self.y = self.k * x + self.b + numpy.expand_dims(numpy.random.rand(numpy.size(x)) - 0.5, axis=1)
#         print(x,self.y)
#         print(numpy.random.rand(numpy.size(x)) - 1)
        self.x = x
    def plotit(self):
        matplotlib.pyplot.scatter(self.x, self.y)
        matplotlib.pyplot.show()
    def return_data(self):
        """
        The result is dictionary.
        {x:,y:}
        """
        return {"x":self.x, "y":self.y}


# In[9]:


# dataset_generate = Dataset_Generate(20, 2, 1)
# dataset_generate.plotit()


# In[ ]:




