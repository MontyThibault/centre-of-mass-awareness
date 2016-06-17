load('calib.mat');

% gridcalibration1466177615

gc = gridcalibration1466177615;

rows = size(gc, 1);

hold on;

for i = 1:rows
    row = gc(i, :);
    
    from = row(1);
    from = from{:};
    
    to = row(2);
    to = to{:};
    
    diff = to - from;
    
    weight = row(3);
    weight = weight{:};
    
    q = quiver(from(1), from(2), diff(1), diff(2));
    
    set(q, 'linewidth', weight * 30);
    % set(q, 'color', weight);
end

hold off;