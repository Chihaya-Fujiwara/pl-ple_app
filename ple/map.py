import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams["xtick.minor.size"] = 3
plt.rcParams["xtick.minor.width"] = 1
#plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定

    
def counter(fig_size_h,fig_size_w,min_em,max_em,min_ex,max_ex,min_inte,max_inte,bins,fs,fig_color,xaxis,yaxis,X,Y,p2):        
    
    @st.cache_data
    def size(fig_size_h,fig_size_w):
        plt.rcParams["figure.figsize"] = (fig_size_h, fig_size_w)
    
    @st.cache_data
    def fontsize(fs):    
        plt.tick_params(labelsize=fs)            

    @st.cache_data
    def em(min_em,max_em):    
        plt.xlim(min_em,max_em)
    
    @st.cache_data
    def ex(min_ex,max_ex):    
        plt.ylim(min_ex,max_ex)
    
    def plot(Y,X,p2,min_inte,max_inte,bins,fig_color):    
        plt.contourf(Y,X,p2,levels=np.linspace(min_inte,max_inte,bins),cmap=fig_color)
        plt.colorbar() 
    
    fig = plt.figure()
    plot(Y,X,p2,min_inte,max_inte,bins,fig_color)
    size(fig_size_h,fig_size_w)
    fontsize(fs)
    
    em(min_em,max_em)
    plt.xlim(min_em,max_em)
    plt.ylim(min_ex,max_ex)  
    plt.ylabel(str(yaxis),fontsize = fs)
    plt.xlabel(str(xaxis),fontsize = fs)
    #left_column.pyplot(fig)
    return(fig)