import os,sys
import csv, json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import math
import re

LEGEND = []
YAXIS = []
XAXIS = []
dataList = []

with open(sys.argv[2]) as json_file:
    json_data = json.load(json_file)

    #size
    FIG_WIDTH = json_data['size']['figure_width']
    FIG_HEIGHT = json_data['size']['figure_height']
    BAR_WIDTH = json_data['size']['bar_width']

    #fontsize
    YAXIS_FONTSIZE = json_data['fontsize']['yaxis_fontsize']
    XAXIS_FONTSIZE = json_data['fontsize']['xaxis_fontsize']
    YAXIS_LABELSIZE = json_data['fontsize']['yaxis_labelsize']
    XAXIS_LABELSIZE = json_data['fontsize']['xaxis_labelsize']
    TITLE_FONTSIZE = json_data['fontsize']['title_size']
    ANNO_FONTSIZE = json_data['fontsize']['annotation_size']
    LEGEND_FONTSIZE = json_data['fontsize']['legend_fontsize']

    #rotation
    YAXIS_ROTATION = json_data['rotation']['yaxis_rotation']
    XAXIS_ROTATION = json_data['rotation']['xaxis_rotation']
    ANNO_ROTATION = json_data['rotation']['annotation_rotation']

    #color
    GRAY_SCALE = json_data['color']['gray_scale']
    COLOR_MIN = json_data['color']['color_min']
    COLOR_MAX = json_data['color']['color_max']
    R_MIN = json_data['color']['red_min']
    R_MAX = json_data['color']['red_max']
    G_MIN = json_data['color']['green_min']
    G_MAX = json_data['color']['green_max']
    B_MIN = json_data['color']['blue_min']
    B_MAX = json_data['color']['blue_max']
    EDGE_COLOR = json_data['color']['edge_color']

    #visible
    YAXIS_VISIBLE = json_data['visible']['yaxis_visible']
    XAXIS_VISIBLE = json_data['visible']['xaxis_visible']

    #grid
    YGRID_VISIBLE = json_data['grid']['ygrid_visible']
    XGRID_VISIBLE = json_data['grid']['xgrid_visible']
    YGRID_LINESTYLE = json_data['grid']['ygrid_linestyle']
    XGRID_LINESTYLE = json_data['grid']['xgrid_linestyle']
    YGRID_WIDTH = json_data['grid']['ygrid_width']
    XGRID_WIDTH = json_data['grid']['xgrid_width']
    YGRID_COLOR = json_data['grid']['ygrid_color']
    XGRID_COLOR = json_data['grid']['xgrid_color']


    #etc
    YLIMIT_USE = json_data['etc']['ylimit_use']
    YLIMIT_BOTTOM = json_data['etc']['ylimit_bottom']
    YLIMIT_TOP = json_data['etc']['ylimit_top']
    INTERVAL = json_data['etc']['interval']
    BAR_INTERVAL = json_data['etc']['bar_interval']
    UNIT = json_data['etc']['unit']
    XAXIS_TWO_LINES = json_data['etc']['xaxis_two_lines']
    XAXIS_MARGIN = json_data['etc']['xaxis_margin']
    XDEVIDE_STRING = json_data['etc']['xaxis_string_for_devide']
    YLABEL_TWO_LINES = json_data['etc']['ylabel_two_lines']
    YDEVIDE_STRING = json_data['etc']['ylabel_string_for_devide']

    #spine
    SPINE_TOP = json_data['spine']['top']
    SPINE_BOTTOM = json_data['spine']['bottom']
    SPINE_LEFT = json_data['spine']['left']
    SPINE_RIGHT = json_data['spine']['right']

    
    #legend
    LEGEND_EDGE_COLOR = json_data['legend']['edge_color']
    LEGEND_EDGE_WIDTH = json_data['legend']['edge_width']
    LEGEND_VISIBLE = json_data['legend']['visible']
    LEGEND_COL_NUM = json_data['legend']['legend_col_num']
    LEGEND_LOCATION = json_data['legend']['legend_location']
    BBOX_XANCHOR = json_data['legend']['legend_bbox_xanchor']
    BBOX_YANCHOR = json_data['legend']['legend_bbox_yanchor']
    LEGEND_BG_COLOR = json_data['legend']['bg_color']
    LEGEND_BG_ALPHA = json_data['legend']['bg_alpha']
    LEGEND_BORDER_PAD = json_data['legend']['border_pad']

    #range
    YAXIS_MIN = json_data['range']['yaxis_min']
    YAXIS_MAX = json_data['range']['yaxis_max']
    YAXIS_INTERVAL = json_data['range']['yaxis_interval']
    YTICK_LABEL_MIN = json_data['range']['ytick_label_min']
    YTICK_LABEL_MAX = json_data['range']['ytick_label_max']
    YTICK_LABEL_INTERVAL = json_data['range']['ytick_label_interval']

    #bar
    HATCH_USE = json_data['bar']['hatch_use']
    HATCH_PATTERN = json_data['bar']['hatch_pattern']

    #label
    LABEL_INTERVAL = json_data['label']['interval']
    LABEL_USE = json_data['label']['label_use']

    #line
    VERTICAL_LINE = json_data['line']['vertical_line_use']
    VERTICAL_X = json_data['line']['vertical_x']
    VERTICAL_YMIN = json_data['line']['vertical_ymin']
    VERTICAL_YMAX = json_data['line']['vertical_ymax']
    VERTICAL_COLOR = json_data['line']['vertical_color']
    VERTICAL_WIDTH = json_data['line']['vertical_width']

def addList(lines, listName, count, lineNum):
    if listName == 'legends':
        for i in range(lineNum, lineNum+count):
            LEGEND.append(lines[i].strip('\n').split(',')[0])
            dataList.append([])
    elif listName == 'y-axis':
        for i in range(lineNum, lineNum+count):
            YAXIS.append(lines[i].strip('\n').split(',')[0])
    elif listName == 'x-axis':
        for i in range(lineNum, lineNum+count):
            XAXIS.append(lines[i].strip('\n').split(',')[0])
            data = lines[i].strip('\n').split(',')
            for j in range(len(data)-1):
                dataList[j].append(float(data[j+1]))

def readData(csvFileName):

    f = open(csvFileName, 'r', encoding='utf-8')
    lines = f.readlines()

    global mode
    for line in range(len(lines)):
        mode = lines[line].strip('\n').split(',')[0]
        if (mode == 'legends' or mode == 'y-axis' or mode == 'x-axis'):
            count = lines[line+1].strip('\n').split(',')[0]
            addList(lines, mode, int(count), line+2);

def autolabel(ax, rects):
    for idx, rect in enumerate(rects):
        height = rect.get_height()
        if YLIMIT_USE == True:
            height_ = rect.get_height()
            if LABEL_USE == False:
                if height > YLIMIT_TOP:
                    height_ = YLIMIT_TOP
                    ax.text(rect.get_x()+rect.get_width()/2 , height_ + LABEL_INTERVAL, '%.1f' % height + UNIT, ha = 'center', va = 'bottom', size=ANNO_FONTSIZE, rotation = ANNO_ROTATION)
            else:
                if height > YLIMIT_TOP:
                    height_ = YLIMIT_TOP
                if height != 0:
                    ax.text(rect.get_x()+rect.get_width()/2 , height_ + LABEL_INTERVAL, '%.1f' % height + UNIT, ha = 'center', va = 'bottom', size=ANNO_FONTSIZE, rotation = ANNO_ROTATION)
        elif YLIMIT_USE == False:
            ax.text(rect.get_x()+rect.get_width()/2 , height + LABEL_INTERVAL, '%.1f' % height + UNIT, ha = 'center', va = 'bottom', size=ANNO_FONTSIZE, rotation = ANNO_ROTATION)

def main():
    usage = "Usage: python3 stackedbarchart.py [.csv file path]\n \
            [.json file path] [output file path]"

    if len(sys.argv) < 4:
        print(usage)
        sys.exit()

    csvFileName = sys.argv[1]
    jsonFileName = sys.argv[2]
    outputFileName = sys.argv[3]

    if os.path.isfile(csvFileName) == False:
        print("Error: File [" + csvFileName + "] doesn't exist")
        sys.exit()

    if csvFileName[-4:0] == ".csv":
        print("Error: File [" + csvFileName + "] is not a csv file")
        sys.exit()

    name = csvFileName.strip('\n').split('.')[0]

    readData(csvFileName)

    plotBarChart(outputFileName)

def colorSet():

    color = 0
    if len(LEGEND) == 1:
        color = 0
    else:
        color = (COLOR_MAX - COLOR_MIN)/(len(LEGEND)-1)

    if GRAY_SCALE == True:
        R = COLOR_MAX
        G = COLOR_MAX
        B = COLOR_MAX
        R_offset = color
        G_offset = color
        B_offset = color

        return R, G, B, R_offset, G_offset, B_offset

    else: #if GRAY_SCALE == False:
        R = R_MAX
        G = G_MAX
        B = B_MAX
        R_offset = (R_MAX-R_MIN)/(len(LEGEND)-1)    #0.5
        G_offset = (G_MAX-G_MIN)/(len(LEGEND)-1)    #0.0
        B_offset = (B_MAX-B_MIN)/(len(LEGEND)-1)    #0.0

        return R, G, B, R_offset, G_offset, B_offset

def makeBar(ax, x, width):

    value = len(LEGEND)-1
    #color
    R, G, B, R_offset, G_offset, B_offset = colorSet()
    print("Here")
    
    for i in range(len(LEGEND)):
        red = R - i*R_offset
        blue = B - i*B_offset
        green = G - i*G_offset
        if red <= 0:
            red = 0
        if green <= 0:
            green = 0
        if blue <= 0:
            blue = 0

        if HATCH_USE == True:
            rect = ax.bar(INTERVAL*x+(-(len(LEGEND)/2)+i)*(width*(1+BAR_INTERVAL)), dataList[i], width, label = LEGEND[i], color = (red, green, blue, 1), edgecolor=EDGE_COLOR, hatch=HATCH_PATTERN, zorder= 2)
        else:
            rect = ax.bar(INTERVAL*x+(-(len(LEGEND)/2)+i)*(width*(1+BAR_INTERVAL)), dataList[i], width, label = LEGEND[i], color = (red, green, blue, 1), edgecolor=EDGE_COLOR, zorder= 2)
        #print(value*x+(-(len(LEGEND)/2)+i)*(width*(1+BAR_INTERVAL)))
        #print(-(len(LEGEND)/2)+i)
        if LABEL_USE == True:
            autolabel(ax, rect)
        else:
            if (max(dataList[i]) > YLIMIT_TOP) and YLIMIT_USE == True:
                autolabel(ax, rect)




def plotBarChart(outputFileName):
    
    with PdfPages(outputFileName) as pdf:

        x = np.arange(len(XAXIS))
        width = BAR_WIDTH

        #color
        R, G, B, R_offset, G_offset, B_offset = colorSet()
        fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT))
        

        major_ticks = np.arange(YAXIS_MIN, YAXIS_MAX, YAXIS_INTERVAL)
        ax.set_yticks(major_ticks)

        #grid
        if YGRID_VISIBLE == True:
            ax.grid(axis='y', color = YGRID_COLOR, linestyle = YGRID_LINESTYLE, linewidth = YGRID_WIDTH, zorder=0)
        if XGRID_VISIBLE == True:
            ax.grid(axis='x', color = XGRID_COLOR, linestyle = XGRID_LINESTYLE, linewidth = XGRID_WIDTH, zorder=0)
            #ax.grid(axis='x', color='#BDBDBD', linestyle='-', linewidth=0.5, zorder=0)


        makeBar(ax, x, width)

        if YLABEL_TWO_LINES == True:
            ylabels_new = YAXIS[0].replace(YDEVIDE_STRING, '\n')
            ax.set_ylabel(ylabels_new, fontsize = YAXIS_FONTSIZE)
        else:
            ax.set_ylabel(YAXIS[0], fontsize = YAXIS_FONTSIZE)
            
        #ax.set_ylabel(YAXIS[0], fontsize = YAXIS_FONTSIZE)

        ax.set_title(" ", fontsize = TITLE_FONTSIZE)
        #plt.ylim(ymin=90)
        if YLIMIT_USE == True:
            plt.ylim(ymin = YLIMIT_BOTTOM, ymax= YLIMIT_TOP)

        #x1, x2, y1, y2 = plt.axis()
        #plt.axis([x1,x2,0,160])
        
        if len(LEGEND)%2 == 0:
            ax.set_xticks(INTERVAL*x+((-len(LEGEND)/2)+(len(LEGEND)//2)-0.5)*width*(1+BAR_INTERVAL))
        else:
            ax.set_xticks(INTERVAL*x+((-len(LEGEND)/2)+(len(LEGEND)//2))*width*(1+BAR_INTERVAL))

        #ax.set_xticklabels(XAXIS, fontsize=XAXIS_LABELSIZE, rotation=XAXIS_ROTATION)

        if XAXIS_TWO_LINES == True:
            xlabels_new = [label.replace(XDEVIDE_STRING, '-\n') for label in XAXIS]
            ax.set_xticklabels(xlabels_new)
        else:
            ax.set_xticklabels(XAXIS)
        ax.set_yticklabels([str(round(i,2))+UNIT for i in np.arange(YTICK_LABEL_MIN,YTICK_LABEL_MAX,YTICK_LABEL_INTERVAL)])
        print([str(i)+UNIT for i in np.arange(0.0,2.0,0.2)])
        #ax.set_yticklabels([])

        #ax.set_yticklabels()
        plt.setp(ax.get_xticklabels(), fontsize = XAXIS_LABELSIZE, rotation = XAXIS_ROTATION)
        plt.setp(ax.get_yticklabels(), fontsize = YAXIS_LABELSIZE, rotation = YAXIS_ROTATION)


        ax.margins(x=XAXIS_MARGIN)
        ax.spines['top'].set_visible(SPINE_TOP)
        ax.spines['right'].set_visible(SPINE_RIGHT)
        ax.spines['left'].set_visible(SPINE_LEFT)
        ax.spines['bottom'].set_visible(SPINE_BOTTOM)

        print(LEGEND_LOCATION)
        ax.legend(loc = LEGEND_LOCATION, ncol = LEGEND_COL_NUM, facecolor = LEGEND_BG_COLOR, framealpha = LEGEND_BG_ALPHA, edgecolor = LEGEND_EDGE_COLOR, fontsize = LEGEND_FONTSIZE, bbox_to_anchor=(BBOX_XANCHOR, BBOX_YANCHOR), borderpad=LEGEND_BORDER_PAD)
        if LEGEND_VISIBLE == False:
            ax.get_legend().remove()
    
        if VERTICAL_LINE == True:
            plt.axvline(VERTICAL_X, VERTICAL_YMIN, VERTICAL_YMAX, color = VERTICAL_COLOR, linewidth=VERTICAL_WIDTH)

        fig.tight_layout(pad=0.5) #pad
        plt.show()

        pdf.savefig(fig)


main()



