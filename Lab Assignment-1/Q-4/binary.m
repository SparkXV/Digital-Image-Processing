clc;                    % clearing the output screen

c= imread('lena.jpg');  % Reading the image pixels

cd = double(c);         % storing image information in cd

c1 = mod(cd,2);         % Extracting all bit images one by one
c2=mod(floor(cd/2),2)
c3=mod(floor(cd/4),2)
c4=mod(floor(cd/8),2)
c5=mod(floor(cd/16),2)
c6=mod(floor(cd/32),2)
c7=mod(floor(cd/64),2)
c8=mod(floor(cd/128),2)

cc = (2 * (2 * (2 * (2 * (2 * (2 * (2 * c8 + c7) + c6) + c5) + c4) + c3) + c2) + c1);

subplot (2,5,1);        % pltting original image
imshow(c);
title('Original Image');

% ploting binary images
subplot(2,5,2);
imshow(c1);
title('bit plane -1')

subplot(2,5,3);
imshow(c2);
title('bit plane -2')

subplot(2,5,4);
imshow(c3);
title('bit plane -3')

subplot(2,5,5);
imshow(c4);
title('bit plane -4')

subplot(2,5,6);
imshow(c5);
title('bit plane -5')

subplot(2,5,7);
imshow(c6);
title('bit plane -6')

subplot(2,5,8);
imshow(c7);
title('bit plane -7')

subplot(2,5,9);
imshow(c8);
title('bit plane -8')

subplot(2,5,10);
imshow(cc);
title('Combined image')
