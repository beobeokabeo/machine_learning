>> t=[0:0.01:0.98];
>> t
t =

 Columns 1 through 12:

   0.00000   0.01000   0.02000   0.03000   0.04000   0.05000   0.06000   0.07000   0.08000   0.09000   0.10000   0.11000

 Columns 13 through 24:

   0.12000   0.13000   0.14000   0.15000   0.16000   0.17000   0.18000   0.19000   0.20000   0.21000   0.22000   0.23000

 Columns 25 through 36:

   0.24000   0.25000   0.26000   0.27000   0.28000   0.29000   0.30000   0.31000   0.32000   0.33000   0.34000   0.35000

 Columns 37 through 48:

   0.36000   0.37000   0.38000   0.39000   0.40000   0.41000   0.42000   0.43000   0.44000   0.45000   0.46000   0.47000

 Columns 49 through 60:

   0.48000   0.49000   0.50000   0.51000   0.52000   0.53000   0.54000   0.55000   0.56000   0.57000   0.58000   0.59000

 Columns 61 through 72:

   0.60000   0.61000   0.62000   0.63000   0.64000   0.65000   0.66000   0.67000   0.68000   0.69000   0.70000   0.71000

 Columns 73 through 84:

   0.72000   0.73000   0.74000   0.75000   0.76000   0.77000   0.78000   0.79000   0.80000   0.81000   0.82000   0.83000

 Columns 85 through 96:

   0.84000   0.85000   0.86000   0.87000   0.88000   0.89000   0.90000   0.91000   0.92000   0.93000   0.94000   0.95000

 Columns 97 through 99:

   0.96000   0.97000   0.98000

>> y1=sin(2*pi*4*t);
>> plot(t, y1)
>> y2=cos(2*pi*4*t);
>> plot(t, y2)
>> plot(t, y1)
>> plot(t, y1, y2)
>> plot(y1, y2)
>> plot(t, y1)
>> hold on;
>> plot (t, y2,'r');
>> xlabel('time');
>> ylabel('value');
>> legend('sin', 'cos');
>> title('my plot');
>> print -dpng 'myPlot.png'
>> y1 = y1'
y1 =

   0.00000
   0.24869
   0.48175
   0.68455
   0.84433
   0.95106
   0.99803
   0.98229
   0.90483
   0.77051
   0.58779
   0.36812
   0.12533
  -0.12533
  -0.36812
  -0.58779
  -0.77051
  -0.90483
  -0.98229
  -0.99803
  -0.95106
  -0.84433
  -0.68455
  -0.48175
  -0.24869
  -0.00000
   0.24869
   0.48175
   0.68455
   0.84433
   0.95106
   0.99803
   0.98229
   0.90483
   0.77051
   0.58779
   0.36812
   0.12533
  -0.12533
  -0.36812
  -0.58779
  -0.77051
  -0.90483
  -0.98229
  -0.99803
  -0.95106
  -0.84433
  -0.68455
  -0.48175
  -0.24869
  -0.00000
   0.24869
   0.48175
   0.68455
   0.84433
   0.95106
   0.99803
   0.98229
   0.90483
   0.77051
   0.58779
   0.36812
   0.12533
  -0.12533
  -0.36812
  -0.58779
  -0.77051
  -0.90483
  -0.98229
  -0.99803
  -0.95106
  -0.84433
  -0.68455
  -0.48175
  -0.24869
  -0.00000
   0.24869
   0.48175
   0.68455
   0.84433
   0.95106
   0.99803
   0.98229
   0.90483
   0.77051
   0.58779
   0.36812
   0.12533
  -0.12533
  -0.36812
  -0.58779
  -0.77051
  -0.90483
  -0.98229
  -0.99803
  -0.95106
  -0.84433
  -0.68455
  -0.48175

>> plot (t, y1,'b');
>> plot (t, y1,'g');
>> close
>> figure(1); plot(t, y1);
>> figure(2); plot(t, y2);
>> subplot(1,2,1); %divides plot a 1x2 grid, access first element
>> plot(t,y1);
>> subplot(t,y2);
error: subplot: invalid axes handle or RCN argument
error: called from
    subplot at line 164 column 7
>> plot(t,y2);
>> plot(t,y1);
>> plot(t,y2);
>> axis([0.5 1 -1 1])
>> help axis
'axis' is a function from the file C:\Users\robk\AppData\Roaming\OCTAVE~1.0\mingw64\share\octave\5.2.0\m\plot\appearance\axis.m


 -- axis ()
 -- axis ([X_LO X_HI])
 -- axis ([X_LO X_HI Y_LO Y_HI])
 -- axis ([X_LO X_HI Y_LO Y_HI Z_LO Z_HI])
 -- axis ([X_LO X_HI Y_LO Y_HI Z_LO Z_HI C_LO C_HI])
 -- axis (OPTION)
 -- axis (OPTION1, OPTION2, ...)
 -- axis (HAX, ...)
 -- LIMITS = axis ()
     Set axis limits and appearance.

     The argument LIMITS should be a 2-, 4-, 6-, or 8-element vector.
     The first and second elements specify the lower and upper limits
     for the x-axis.  The third and fourth specify the limits for the
     y-axis, the fifth and sixth specify the limits for the z-axis, and
     the seventh and eighth specify the limits for the color axis.  The
     special values -Inf and Inf may be used to indicate that the limit
     should be automatically computed based on the data in the axes.

     Without any arguments, 'axis' turns autoscaling on.

     With one output argument, 'LIMITS = axis' returns the current axis
     limits.

     The vector argument specifying limits is optional, and additional
     string arguments may be used to specify various axis properties.

     The following options control the aspect ratio of the axes.

     "square"
          Force a square axis aspect ratio.

     "equal"
          Force x-axis unit distance to equal y-axis (and z-axis) unit
          distance.

     "normal"
          Restore default aspect ratio.

     The following options control the way axis limits are interpreted.

     "auto"
     "auto[xyz]"
          Set the specified axes to have nice limits around the data or
          all if no axes are specified.

     "manual"
          Fix the current axes limits.

     "tight"
          Fix axes to the limits of the data.

     "image"
          Equivalent to "tight" and "equal".

     "vis3d"
          Set aspect ratio modes to "manual" for rotation without
          stretching.

     The following options affect the appearance of tick marks.

     "tic[xyz]"
          Turn tick marks on for all axes, or turn them on for the
          specified axes and off for the remainder.

     "label[xyz]"
          Turn tick labels on for all axes, or turn them on for the
          specified axes and off for the remainder.

     "nolabel"
          Turn tick labels off for all axes.

     Note: If there are no tick marks for an axes then there can be no
     labels.

     The following options affect the direction of increasing values on
     the axes.

     "xy"
          Default y-axis, larger values are near the top.

     "ij"
          Reverse y-axis, smaller values are near the top.

     The following options affects the visibility of the axes.

     "on"
          Make the axes visible.

     "off"
          Hide the axes.

     If the first argument HAX is an axes handle, then operate on this
     axes rather than the current axes returned by 'gca'.

     Example 1: set X/Y limits and force a square aspect ratio

          axis ([1, 2, 3, 4], "square");

     Example 2: enable tick marks on all axes, enable tick mark labels
     only on the y-axis

          axis ("tic", "labely");

     See also: xlim, ylim, zlim, caxis, daspect, pbaspect, box, grid.

Additional help for built-in functions and operators is
available in the online version of the manual.  Use the command
'doc <topic>' to search the manual index.

Help and information about Octave is also available on the WWW
at https://www.octave.org and via the help@octave.org
mailing list.
>> clf %clears figure
>> A = magic(5)
A =

   17   24    1    8   15
   23    5    7   14   16
    4    6   13   20   22
   10   12   19   21    3
   11   18   25    2    9

>> imagesc(A)
>> imagesc(A), colorbar, colormap gray
>> imagesc(A)
>> figure(1); imagesc(A)
>> A(4,5)
ans =  3
>> imagesc(magic(15))
>>
