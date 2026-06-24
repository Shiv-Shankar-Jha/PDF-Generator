from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation = "p", unit = "mm", format = "A4", )

df = pd.read_csv("topics.csv")
# This is a dataframe which reads the csv file and stores the data in a tabular format. The csv file contains the topics and their descriptions.

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_text_color(255, 0, 0)
    # this sets the text color to a shade of gray. The parameters are RGB values.
    # RGB values can vary from 0 to 255, depending on the color you want.

    pdf.set_font(family = "Times", size = 24, style = "B")
    pdf.cell(w = 0, h = 10, txt = row["Topic"], ln = 1, align = "L")
    pdf.line(10, 22, 200, 22)
    # Add line under the topic name. The parameters are x1, y1, x2, y2. The line will be drawn from (x1, y1) to (x2, y2).




# pdf.add_page()
# pdf.set_font(family = "Times", size = 12, style = "B")
# pdf.cell(w = 0, h = 10, txt = "Hello World", ln = 1, align = "L", border=1)
pdf.output("output.pdf")