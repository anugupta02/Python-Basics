#Calculate the mean value of a list of numbers
def mean(values):
	return sum(values)/(len(values))
	
#Calculate the variance value of a list of numbers
def variance(values,mean):
	return sum([(x-mean)**2 for x in values])/(len(values)
	
	
#Calculate mean and variance
dataset = [[1,1],[2,3],[4,3],[3,2],[5,5]]
x=[row[0] for row in dataset]
print(x)
y=[row[1] for row in dataset]
print(y)
mean_x, mean_y = mean(x), mean(y)
var_x, var_y = variance(x,mean_x),variance()

print()
print()

#Calculate Variance
#covariance = sum((x(i)-mean(x))*(y(i)-mean(y)))/len(value)

def covariance(x,mean_x,y,mean_y):
    covar=0.0
	for i in range(len(x)):
		covar +=(x[i] - mean_x)*(y[i] - mean_y)
	return covar/len(x)
	
dataset = [[1,1],[2,3],[4,3],[3,2],[5,5]]
x = [row[0] for row in dataset]

y = [row[1] for row in dataset]
mean_x,mean_y=mean(x),mean(y)
var=variance(x,mean_x,y,mean(y))
print('Variance: %.2f' % (covar))

#Calculate Covariance
#covariance=sum((x(i)-mean(x)) * (y(i)-mean(y)))

dataset = [[1,1],[2,3],[4,3],[3,2],[5,5]]
x = [row[0] for row in dataset]

y = [row[1] for row in dataset]
mean_x, mean_y = mean(x), mean(y)
mean_x,mean_y=mean(x),mean(y)
covar=covariance(x,mean_x,y,mean(y))
print('Covariance: %.2f' % (covar))

#Calculate Coefficient
#B1 = sum((x(i) - mean(x))*(y(i) - mean(y)))/sum((x(i)-mean(x))^2)

def coefficients(dataset):
	x= [row[0] for row in dataset]
	y= [row[1] for row in dataset]
	x_mean,y_mean=mean(x),mean(y)
	b1=covariance(x,x_mean,y,y_mean)/variance(x,x_mean)
	b0=y_mean - b1*x_mean
	return[b0, b1]
	
	
#Calculate Coefficients
dataset = [[1,1],[2,3],[4,3],[3,2],[5,5]]
b0,b1 = coefficients(dataset)
print('Coefficients : B0=%.3f, B1=%.3f' % (b0,b1))
	
