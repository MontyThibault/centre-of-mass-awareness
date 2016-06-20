load('calib.mat');

% gridcalibration1466187461

gc = gridcalibration1466187461;

rows = size(gc, 1);

clf;
hold on;

% Draw grid lines
l = 53.0;
w = 44.5;

l_seg = 6;
w_seg = 5;

L = linspace(-l, l, l_seg + 1);
W = linspace(-w, w, w_seg + 1);

% Vertical lines
for w_ = W
    line([w_, w_], [-l, l]);
end

% Horizontal lines
for l_ = L
    line([-w, w], [l_, l_]);
end

% Draw displacement vectors
for i = 1:rows
    row = gc(i, :);
    
    from = row(1);
    from = from{:};
    
    to = row(2);
    to = to{:};
    
    diff = to - from;
    
    weight = row(3);
    weight = weight{:};
    
    q = quiver(from(1), from(2), diff(1), diff(2), 5);
    
    set(q, 'linewidth', weight * 6);
    % set(q, 'color', weight);
end

hold off;