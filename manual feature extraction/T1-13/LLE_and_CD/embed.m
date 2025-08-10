function Y = embed(X, m, tau)
%EMBED Embed time series X into an m-dimensional phase space
%   Y = EMBED(X, M, TAU) embeds the time series X into an m-dimensional
%   phase space with a time lag of TAU. Each row of the output matrix Y
%   contains a single m-dimensional vector.
%
%   Example:
%      X = rand(1000,1);  % generate random time series
%      Y = embed(X, 3, 10); % embed into 3D phase space with lag 10

% Determine length of time series
N = length(X);

% Determine maximum index for which an embedded vector can be constructed
imax = N - (m - 1)*tau;

% Initialize output matrix
Y = zeros(imax, m);

% Construct embedded vectors
for i = 1:imax
    Y(i,:) = X(i + (0:m-1)*tau)';
end

end
