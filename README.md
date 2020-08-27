# Command
> python3 barchart.py [.csv file name] [.json file name] [output file name] 

> python3 stackedbarchat.py [.csv file name] [.json file name] [outuput file name]

csv file is data file.
json file is attributes of graph.

# Python file
## barchart.py

The file "barchart.py" is for drawing a barchart.

 

## stackedbarchart.py

TBC

# json file
> Json file has many attributes for drawing a bar graph.  
> **example.json** is an example about how to fill your json file.

## fontsize

- **yaxis_fontsize**
- **xaxis_fontsize**
- **yaxis_labelsize**
- **xaxis_labelsize**
- **title_size** 

## size

- **figure_width**
- **figure_height**
- **bar_width**

## color

- **gray_scale** 0 or 1
- **color_min**/**color_max** These values available when gray_scale is 1 only (range: 0.0~1.0).
- **red_min**/**red_max**, **green_min**/**green_max**, **blue_min**/**blue_max** These values are available when gray_scale is 0 only (range: 0.0~1.0).
- **edge_color** A border color of the bars.

## rotation
- **yaxis_rotation**
- **xaxis_rotation**
- **annotation_rotation** A value label of bar's rotation
## visible
- **yaxis_visible**
- **xaxis_visible**
## grid
- **ygrid_visible** 0 or 1
- **xgrid_visible** 0 or 1
- **ygrid_linestyle**
```
|  Possible vaules  |  Description   | 
|-------------------|----------------|
|   '-' or 'solid'  |   solid line   |
|  '--' or 'dashed' |   dashed line  |
| '-.' or 'dashdot' |dash-dotted line|
|  ':' or 'dotted'  |   dotted line  |
|'None' or ' ' or ''|  draw nothing  |
```
- **xgrid_linestyle**
```
|  Possible vaules  |  Description   | 
|-------------------|----------------|
|   '-' or 'solid'  |   solid line   |
|  '--' or 'dashed' |   dashed line  |
| '-.' or 'dashdot' |dash-dotted line|
|  ':' or 'dotted'  |   dotted line  |
|'None' or ' ' or ''|  draw nothing  |
```
## spine
> Bar graph's border
- **top** 0 or 1
- **bottom** 0 or 1
- **left** 0 or 1
- **right** 0 or 1

## legend
- **visible** 0 or 1
- **legend_fontsize**
- **edge_color**
- **edge_width**
- **legend_col_num** The number of legend column. ex) 6 legends has 2 coloums -> 3rows and 2columns 
- **legend_location**
```
|location string|location code|
|    'best'     |      0      |
| 'upper right' |      1      |
|  'upper left'	|      2      |
|  'lower left'	|      3      |
| 'lower right'	|      4      |
|    'right'    |      5      |
| 'center left'	|      6      |
| 'center right'|      7      |
| 'lower center'|      8      |
| 'upper center'|      9      |
|    'center'   |      10     |
```
- **legend_bbox_xanchor**
- **legend_bbox_yanchor**
- **bg_color** Background color
- **bg_aplha** Transparency (range 0.0~1.0)
- **border_pad** Border padding

## range
- **yaxis_min**
- **yaxis_max**
- **yaxis_interval**
- **ytick_label_min** 
- **ytick_label_max**
- **ytick_label_interval**

## bar
- **hatch_use** 0 or 1, pattern in bar use or not
- **hatch_pattern** 

## label
- **label_fontsize**
- **label_use**
- **interval** Interval between bar and label

## line
> vertical line in the graph
- **vertical_line use** 0 or 1
- **vertical_x** x location
- **vertical_ymin** y location min
- **vertical_ymax** y location max
- **vertical_color** 
- **vertical_width**


## etc
- **ylimit_use** 0 or 1, use yaxis limit
- **ylimit_bottom** This value is available when ylimit_use is 1 only.
- **ylimit_top** This value is available when ylimit_use is 1 only.
- **interval** interval between x labels.
- **bar_interval** interval between bars if there are several bars at same x label.
- **unit** The character at the end of label value. ex) 10x 20x -> unit is 'x'
- **xaxis_two_lines** 0 or 1, If xaxis are too long, devide it into two lines. 
- **xaxis_string_for_devide** The string of devision criteria for x axis.
- **ylabel_two_lines** 0 or 1, If y label are too long, devide it into two lines.
- **ylabel_string_for_devide** The string of devision criteria for y label.

# csv file
## TBC
