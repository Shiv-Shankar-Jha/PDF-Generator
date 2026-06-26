from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation = "p", unit = "mm", format = "A4", )
pdf.set_auto_page_break(auto=False, margin=0)
# This is a pdf methhod which sets the auto page break to false. 
# This means that the pdf will not automatically add a new page when the content exceeds the page size. 
# The margin parameter is set to 0, which means that there will be no margin on the pages.

df = pd.read_csv("topics.csv")
# This is a dataframe which reads the csv file and stores the data in a tabular format.
#  The csv file contains the topics and their descriptions.

for index, row in df.iterrows():
    # Iterrows is a pnadas dataframe method which iterates over the rows of the dataframe.
    #  It returns an iterator yielding index and row data for each row. 
    pdf.add_page()
    pdf.set_text_color(255, 0, 0)
    # this sets the text color to a shade of gray. The parameters are RGB values.
    # RGB values can vary from 0 to 255, depending on the color you want.

    pdf.set_font(family = "Times", size = 24, style = "B")
    pdf.cell(w = 0, h = 10, txt = row["Topic"], ln = 1, align = "L")

    for i in range(22, 290, 10):
        pdf.line(10, i, 200, i)
    # Adds lines to the master page, 22 is starting point of the line and 290 is the end point of the line(Vertically).
    # The lines are drawn at an interval of 10 mm.

    pdf.line(10, 22, 200, 22)
    # Add line under the topic name. The parameters are x1, y1, x2, y2. The line will be drawn from (x1, y1) to (x2, y2).
    
    pdf.ln(262)
    # this is a pdf method which adds a line break. 
    # The parameter is the height of the line break in mm. In this case, it is set to 262 mm, which is the height of an A4 page.
    pdf.set_font(family = "Times", style = "i", size = 8)
    pdf.set_text_color(216, 83, 42)
    pdf.cell(w= 0, h= 10, txt= row["Topic"], align = "R")

    # These lines adds a footer of text same as topic name at the bottom right side of the page.
    # But this adds footer only in the master page, to write in other pages we need to write the code in the for loop below.

    for i in range(row["Pages"] - 1):
        # row[Pages} is dedined as the number of pages to be created for each topic. The first page is already created,
        # so we need to create (Pages - 1) more pages.
        pdf.add_page()

        pdf.ln(270)      # This is a little to high cause there is no topic written in the blank pages. 270 mm break line is good
        # for the footer of the blank pages.
        pdf.set_font(family = "Times", style = "i", size = 8)
        pdf.set_text_color(216, 83, 42)
        pdf.cell(w= 0, h= 10, txt= row["Topic"], align = "R")

        for i in range(12, 290, 10):
            pdf.line(10, i, 200, i)
    # Adds lines to the master page, 12 is starting point of the line and 290 is the end point of the line(Vertically).
    # The lines are drawn at an interval of 10 mm.

pdf.output("output.pdf")