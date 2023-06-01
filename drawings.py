import matplotlib.pyplot as plt

class DrawingPlots():
    def __init__(self, df):
        self.df = df
    
    def scatter(self):
        columns = list(self.df.columns)
        plots = []
        for i in range(len(columns)):
            for j in range(i+1, len(columns)):
                fig, ax = plt.subplots(figsize=(10,6))
                x = self.df[columns[i]]
                y = self.df[columns[j]]
                ax.scatter(x, y)
                ax.set_xlabel(columns[i])
                ax.set_ylabel(columns[j])
                title = f'Scatter plot between {columns[i]} and {columns[j]}'
                ax.set_title(title)
                plots.append(fig)
        return plots
