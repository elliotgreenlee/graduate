% ECE471/571 project 1
% How to estimate two-modal Gaussian
% 
% Assume you've already run "plotsynth.m"

%
clear all;

% following is the estimate from class 0, the red samples
% if you've used the plotsynth.m to plot the samples from the training set
d = 2;    % two-dimensional
mu1 = [0.07595431; 0.68296891];
S1 = [0.15846988, -0.01545041; -0.01545041, 0.02971875];

nr = 1;     % row index
for i=-1.5:0.01:1
  nc = 1;   % column index
  for j=-0.2:0.01:1 
    x = [i;j];
    px1 = 1/((2*pi)^(d/2)*(det(S1))^(1/2)) * exp(-1/2*(x - mu1)'*inv(S1)*(x-mu1));
    px(nr,nc) = px1;
    nc = nc + 1;
 end
 nr = nr + 1;
end

[m,n] = size(px);

xindex = repmat([-1.5:0.01:1]',1,n);
yindex = repmat([-0.2:0.01:1],m,1);

contour(xindex,yindex,px);



