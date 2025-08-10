function D = GP_algorithm(x, m, r)
% Input: 
% x: data series (a vector)
% m: embedding dimension
% r: radius of neighborhood
% Output:
% D: correlation dimension estimated by G-P algorithm

% delay-coordinate embedding
N = length(x); % length of data series
X = zeros(m, N-m+1);
for i = 1:m
    X(i, :) = x(i:N-m+i);
end

% calculate distance matrix and count number of neighbors
dist_mat = pdist(X');
num_neigh = sum(dist_mat < r, 2);

% calculate correlation sum
C = 2 * sum(num_neigh) / (N-m+1) / (N-m);

% use G-P formula to estimate correlation dimension
D = log(C) / log(r);

end
