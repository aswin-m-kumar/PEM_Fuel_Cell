data = readmatrix('P curve.csv','NumHeaderLines',5);

V = data(:,1);
j = data(:,2);

% Power density
P_density = V .* j;

% Find Maximum Power Point
[Pmax, idx] = max(P_density);

V_mpp = V(idx);
j_mpp = j(idx);

fprintf('Maximum Power Density = %.4f W/cm^2\n', Pmax);
fprintf('MPP Voltage = %.4f V\n', V_mpp);
fprintf('MPP Current Density = %.4f A/cm^2\n', j_mpp);

% Power density curve
figure;
plot(j, P_density, 'o-', 'LineWidth', 1.5);
hold on;

plot(j_mpp, Pmax, 'ro', ...
    'MarkerSize', 9, ...
    'LineWidth', 2);

grid on;

xlabel('Current Density (A/cm^2)');
ylabel('Power Density (W/cm^2)');
title('PEMFC Power Density Curve');

legend('Power Density', 'Maximum Power Point', ...
       'Location', 'best');

text(j_mpp, Pmax, ...
    sprintf('  MPP: %.3f W/cm^2', Pmax));