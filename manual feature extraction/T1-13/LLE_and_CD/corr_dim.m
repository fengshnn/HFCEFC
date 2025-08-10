function [D, C] = corr_dim(x, m, r)
% Compute correlation dimension of a time series x
% using box counting method
%
% Inputs:
%   x: time series data (1D array)
%   m: embedding dimension
%   r: size of boxes (scalar)
%
% Outputs:
%   D: correlation dimension
%   C: number of boxes required to cover the attractor

% Embed the time series using time delay embedding
N = length(x);
X = embed(x, m);

% Compute pairwise distances between points in the embedded space
distances = squareform(pdist(X));

% Compute the number of pairs of points whose distance is less than r
n_pairs = sum(sum(distances < r));

% Compute the total number of boxes needed to cover the attractor
N_boxes = floor((N-m+1)/r);

% Compute the correlation dimension
D = log(n_pairs/N_boxes)/log(r);

% Compute the number of boxes needed to cover the attractor
C = N_boxes^D;
end

function X = embed(x, m)
% Embed time series x using time delay embedding
%
% Inputs:
%   x: time series data (1D array)
%   m: embedding dimension
%
% Output:
%   X: embedded time series matrix (m x (N-m+1))

N = length(x);
X = zeros(m, N-m+1);
for i = 1:m
    X(i,:) = x(i:N-m+i);
end
end
