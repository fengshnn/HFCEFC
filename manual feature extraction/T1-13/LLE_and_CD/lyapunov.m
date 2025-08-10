function MLE = lyapunov(x, tau, dim)
%LYAPUNOV Compute the maximum Lyapunov exponent of a time series
%   MLE = LYAPUNOV(X, TAU, DIM) computes the maximum Lyapunov exponent of
%   the time series X using time delay TAU and embedding dimension DIM.
%
%   Example:
%      x = rand(1000,1);  % generate random time series
%      tau = 10;  % time delay
%      dim = 3;  % embedding dimension
%      MLE = lyapunov(x, tau, dim);

% Embed time series into phase space
X = embed(x, dim, tau);

% Compute Euclidean distances between all pairs of points in the embedded space
D = pdist(X);

% Compute the number of pairs that remain within a distance threshold
epsilon = mean(D);  % use mean distance as threshold
N = sum(D < epsilon);

% Compute maximum Lyapunov exponent
MLE = log(2)/tau * (1/dim) * log(N/(length(x)-dim*tau));

end
