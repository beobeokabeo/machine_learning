function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%



hyp = X * theta;

% skip theta(1) because indexing starts from 0 and we ignore the bias term and indexing starts from 1 in octave
theta_reg = [0;theta(2:end, :)];

J = 1/(2*m) * sum((hyp - y) .^2) + (lambda/ (2*m) ) * (theta_reg' * theta_reg);

% partial derivative of regularized cost
grad = (1/m) * X' * (hyp - y) + (lambda/m) * theta_reg;




% =========================================================================

grad = grad(:);

end
