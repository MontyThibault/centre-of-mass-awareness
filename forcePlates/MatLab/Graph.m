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
% gridcalibration1466448929 - June 20th, 2016, Medium-low pressure
% gridcalibration1466449303 - June 20th, 2016, Very high pressure

gcs = {};
% gcs{1} = gridcalibration1466187461;
% gcs{1} = gridcalibration1466434867;
% gcs{1} = gridcalibration1466448714;
% gcs{1} = gridcalibration1466448929;
gcs{1} = gridcalibration1466449303;

rows = size(gcs{1}, 1);

for j = 1:numel(gcs)
    gc = gcs{j};

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
end

hold off;