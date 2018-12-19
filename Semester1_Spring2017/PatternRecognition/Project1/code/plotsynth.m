% ECE471/571 project 1
% How to illustrate data points
%

% clear the figure
clf;

% load the training set
load synth.tr;
Tr = synth;

% extract the samples belonging to different classes
I = find(Tr(:,3) == 0);  % find the row indices for the 1st class, labeled as 0
Tr0 = Tr(I,1:2);
save Tr0;                % so that you can use it directly next time 

I = find(Tr(:,3) == 1);  % find the row indices for the 2nd class, labeled as 1
Tr1 = Tr(I,1:2);
save Tr1;

% plot the samples
plot(Tr0(:,1),Tr0(:,2),'r*'); % use "red" for class 0
hold on;           % so that the future plots can be superimposed on the previous ones
plot(Tr1(:,1),Tr1(:,2),'go'); % use "green" for class 1


a1 = -0.83262295;
b1 = 0.44378198;
syms x y
%ezplot(y == a1 * x + b1, [-1.5, 1]);

a2 = -0.13374205;
b2 = 0.56113764;
syms x y
%ezplot(y == a2 * x + b2, [-1.5, 1]);

mu1 = [-0.22147024; 0.32575494];
mu2 = [0.07595431; 0.68296891];
S1 = [0.27459508  0.01113883; 0.01113883  0.03583011];
S2 = [0.15846988 -0.01545041; -0.01545041  0.02971875];
syms x y
%5ezplot((-0.5 * (S1(1,1) * x^2 + S1(2,1) * x * y + S1(1, 2) * x * y + S1(2, 2) * y^2) + (S1(1, 1) * mu1(1) * x + S1(1,2) * mu1(2) * x + S1(2,1) * mu1(1) * y + S1(2, 2) * mu1(2) * y) -0.5 * (mu1' * inv(S1) * mu1) - 0.5 * log(det(S1)) + log(0.5)) - (-0.5 * (S2(1,1) * x^2 + S2(2,1) * x * y + S2(1, 2) * x * y + S2(2, 2) * y^2) + (S2(1, 1) * mu2(1) * x + S2(1,2) * mu2(2) * x + S2(2,1) * mu2(1) * y + S2(2, 2) * mu2(2) * y) -0.5 * (mu2' * inv(S2) * mu2) - 0.5 * log(det(S2)) + log(0.5)) == 0)
% (-0.5 * (S2(1,1) * x^2 + S2(2,1) * x * y + S2(1, 2) * x * y + S2(2, 2) * y^2) + (S2(1, 1) * mu2(1) * x + S2(1,2) * mu2(2) * x + S2(2,1) * mu2(1) * y + S2(2, 2) * mu2(2) * y) -0.5 * (mu2' * inv(S2) * mu2) - 0.5 * log(det(S2)) + log(0.5)) 




