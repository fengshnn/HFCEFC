function [LLE, CD] = LLE_CD(x, m, tau, k)
% LLE_CD calculates the maximum Lyapunov exponent and correlation dimension
% of a time series.
% Inputs:
%   x: the time series
%   m: the embedding dimension
%   tau: the time delay
%   k: the number of nearest neighbors to use for the LLE calculation
% Outputs:
%   LLE: the maximum Lyapunov exponent
%   CD: the correlation dimension

% Embed the time series
E = embed(x, m, tau);

% Calculate the Euclidean distance matrix
D = pdist(E);

% Calculate the neighborhood size for each point
N = zeros(size(E, 1), 1);
for i = 1:size(E, 1)
    N(i) = sum(D((i-1)*(size(E, 1)-i/2)+1:i*(size(E, 1)-i/2)) < max(D)*0.05);
end

% Calculate the LLE
LLE = lyap_k(x, m, tau, k)./tau;

% Calculate the correlation dimension
r_min = min(D(D>0));
r_max = max(D);
r = logspace(log10(r_min), log10(r_max), 20)';
N_r = zeros(length(r), 1);
for i = 1:length(r)
    N_r(i) = sum(sum(D <= r(i)*ones(size(D)) & D > 0)) / 2;
end
CD = polyfit(log(r(N_r>0)), log(N_r(N_r>0)), 1);
CD = CD(1);
end

function [LLE] = lyap_k(x, m, tau, k)
%LYAP_K Calculates the maximum Lyapunov exponent using the method of Rosenstein et al. with k nearest neighbors
%   X: time series
%   m: embedding dimension
%   tau: time delay
%   k: number of nearest neighbors

N = length(x);
% Create the time-delay embedding matrix
X = zeros(m, N-m*tau);
for i = 1:m
    X(i,:) = x((i-1)*tau+1:N-m*tau+i*tau);
end

% Compute the Euclidean distances between all pairs of points
d = pdist(X','euclidean');

% Find the k nearest neighbors of each point
idx = zeros(N-m*tau, k);
for i = 1:N-m*tau
    [~,idx(i,:)] = sort(d(i,:));
    idx(i,:) = idx(i,:) + i;
end

% Compute the average distance between each point and its k nearest neighbors
r = mean(d(idx), 2);

% Compute the maximum Lyapunov exponent
LLE = sum(log(r(2:end)./r(1:end-1))) / ((N-m*tau-k)*tau);

end
