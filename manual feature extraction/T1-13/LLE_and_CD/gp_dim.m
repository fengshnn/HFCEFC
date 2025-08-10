function [D] = gp_dim(x,m,tau)
%Grassberger, P., & Procaccia, I. (1983). Measuring the strangeness of strange attractors. Physica D: Nonlinear Phenomena, 9(1-2), 189-208.
N = length(x);
M = N-m*tau+1;

% Create the trajectory matrix
X = zeros(M,m);
for i=1:M
    X(i,:) = x((i-1)*tau+1:(i-1)*tau+m);
end

% Compute pairwise distances
d = pdist(X);

% Compute the logarithmically spaced radii
r = logspace(log10(min(d)),log10(max(d)),30);

% Compute the number of points within each radius
nr = zeros(size(r));
for i=1:length(r)
    nr(i) = sum(d <= r(i));
end

% Compute the correlation sum
lnMr = zeros(size(nr));
for i=1:length(nr)
    lnMr(i) = sum(log(nr(i+1:end)));
end

% Fit a line to the correlation sum
p = polyfit(log(r(1:end-1)),lnMr(1:end-1),1);

% The slope of the line is the correlation dimension
D = p(1);

end
