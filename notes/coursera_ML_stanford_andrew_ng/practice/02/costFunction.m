function [jVal, gradient] = costFunction(theta)

jVal = (theta(1)-5)^2 + (theta(2)-5)^2;

gradient = zeros(2,1); % 2 by 1 vector// 2d vector
gradient(1) = 2*(theta(1)-5);
gradient(2) = 2*(theta(2)-5);
