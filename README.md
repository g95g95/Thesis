# Thesis
The following program can be used to immediately display the scatter plot we aim to analyze.

# How the repository works
First of all make sure the your data are stored according to the excel file or txt file stored in [Results](https://github.com/g95g95/Thesis.git). Make sure the sintax match perfectly,
otherwise a ValueError will be raised.

Open the file [main_Thesis.py.](https://github.com/g95g95/Thesis.git). At first create an object of the class **ThesisGraph**, defined in [ThesisGraph.py](https://github.com/g95g95/Thesis.git).
Then import the data from the file you prefer, let it be excel or txt, through the method of the class *import_as_txt(excel)*. You should insert the name of the file, in the corresponding argument *filename*.
Such a file has to be always stored in the folder Results, otherwise the program needs to be changed.

Now, if we want to make an usual graph EMF vs Composition of hydrogen you can call the method **plot_P_and_EMF_vs_Ch** which takes several arguments.
You should insert the title (*title*), the Date (*Date*), if you want a logscale on x or y axis (*logscalex(y) = True or False*), the label for the load (unload) measurement (first/second method).
Eventually, if we want to display a cycle of unloading you need to insert the Secondbatchfilename attribute corresponding to the name of the file in which these data are stored (always in ) [Results](https://github.com/g95g95/Thesis.git).
The same can be done for what concerns **plot_T_T0vsCh**. All the graphs will be stored in the folder [Graphs](https://github.com/g95g95/Thesis.git) Here below you can see a preview:

![BOh](https://github.com/g95g95/Thesis/blob/main/Graphs/Test_14_10_2020.png)
