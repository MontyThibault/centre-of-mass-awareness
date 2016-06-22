load('calib.mat');

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


% Useful calibration runs
% gridcalibration1466187461 - June 17th, 2016, Medium pressure
% gridcalibration1466434867 - June 20th, 2016, High pressure
% gridcalibration1466448714 - June 20th, 2016, Low pressure
% gridcalibration1466449303 - June 20th, 2016, Very high pressure

% gridcalibration1466527877 - June 21st, 2016, Low pressure
% gridcalibration1466528020 - June 21st, 2016, Low pressure

% gridcalibration1466605224 - June 22nd, 2016, Multisample test


gcs = {};

gcs{1} = gridcalibration1466608773;


for j = 1:numel(gcs)
    gc = gcs{j};
    
    rows = size(gc, 1);

    % Draw displacement vectors
    for i = 1:rows
        row = gc(i, :);

        from = row(1);
        from = from{:};

        to = row(2);
        to = to{:};
        
        if j >= 3
            % Annoying scaling factor from Maya
            to = to / 0.167;
        end

        diff = to - from;

        weight = row(3);
        weight = weight{:};

        target = 1;
        epsilon = 0.95;
        if weight < target - epsilon || weight > target + epsilon
            continue
        end
        
        redComponent = min(1, weight * 3);
        blueComponent = max(0, 1 - (weight * 3));
        q = quiver(from(1), from(2), diff(1), diff(2), 4, 'color', [redComponent, 0.3, blueComponent]);
        
        set(q, 'linewidth', 2);
    end
end

hold off;