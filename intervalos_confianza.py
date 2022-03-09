# Confidence interval calculator in Python
# https://towardsdatascience.com/how-to-calculate-confidence-intervals-in-python-a8625a48e62b
# Let’s now calculate the confidence intervals in Python
# using Student’s T distribution and the bootstrap technique.

# Let’s import some useful libraries.
import numpy as np
import scipy.stats as st
from scipy.stats import t
from scipy.stats import norm

# Let’s now simulate a dataset made of 100 numbers
# extracted from a normal distribution.
x = np.random.normal(size = 100)

# Let’s see we want to calculate the 95% confidence interval of the mean value.
# Let’s calculate all the numbers we need according to the formula of confidence intervals.
m = x.mean()
s = x.std()
dof = len(x) - 1
confidence = 0.95

# We now need the value of t.
# The function that calculates the inverse cumulative distribution is ppf.
# We need to apply the absolute value because the cumulative distribution works
# with the left tail, so the result would be negative.
t_crit = np.abs(t.ppf((1 - confidence) / 2, dof))

# Now, we can apply the original formula to calculate the 95% confidence interval.
print(m - s * t_crit / np.sqrt(len(x)), m + s * t_crit / np.sqrt(len(x)))

# We know it’s correct because the normal distribution has 0 mean,
# but if we don’t know anything about the population, we could say that,
# with 95% confidence, the expected value of the population lies between -0.14 and 0.26.

# We could have reached the same result using a bootstrap, which is unbiased.
# In this example, I create 1000 resamples of our dataset (with replacements).
values = [np.random.choice(x, size = len(x), replace = True).mean() for i in range(1000)]
print(np.percentile(values, [100 * (1 - confidence) / 2, 100 * (1 - (1 - confidence) / 2)]))

# As we can see, the result is almost equal to the one we have reached with the closed formula.

# Confidence intervals are easy to calculate and can give a very useful insight
# to data analysts and scientists. They give a very powerful error estimate and,
# if used correctly, can really help us to extract as much information
# as possible from our data.

# define sample data
data = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]

# create 95% confidence interval for population mean weight
n = 20
m = 16.98
dv = 2.19
alfa = 0.05

print(norm.cdf(1 - alfa))

# intervalo = t.interval(alpha = confidence, df = n - 1, loc = m, scale = st.sem(data))
# print(intervalo)